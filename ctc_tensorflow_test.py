import os
import operator
import random
import time
import io

import numpy as np
import tensorflow as tf

from audio_reader import AudioReader
from file_logger import FileLogger
from utils import FIRST_INDEX, sparse_tuple_from
from utils import convert_inputs_to_ctc_format


sample_rate = 16000
# Some configs
num_features = 26  # log filter bank or MFCC features
# Accounting the 0th index +  space + blank label = 28 characters
num_classes = ord('z') - ord('a') + 1 + 1 + 1

# Hyper-parameters
num_epochs = 1
num_hidden = 256
batch_size = 346

num_examples = 1
num_batches_per_epoch = 10

audio = AudioReader(audio_dir=None, cache_dir='test_1_cache', sample_rate=sample_rate)

file_logger = FileLogger('out_test.tsv', ['curr_epoch', 'train_cost', 'train_ler', 'val_cost', 'val_ler'])

def next_batch(bs=batch_size, train=True):
    x_batch = []
    y_batch = []
    seq_len_batch = []
    original_batch = []
    i=0
    for k in range(bs):
        ut_length_dict = dict([(k, len(v['target'])) for (k, v) in audio.cache.items()])
        utterances = sorted(ut_length_dict.items(), key=operator.itemgetter(0))
        test_index = 346
        if train:
            utterances = [a[0] for a in utterances[test_index:]]
        else:
            utterances = [a[0] for a in utterances[:test_index]]
        training_element = audio.cache[utterances[i]]
        target_text = training_element['target']
        audio_buffer = training_element['audio']
        x, y, seq_len, original = convert_inputs_to_ctc_format(audio_buffer,
                                                               sample_rate,
                                                               'whatever',
                                                               num_features)
        x_batch.append(x)
        y_batch.append(y)
        seq_len_batch.append(seq_len)
        original_batch.append(original)
        i+=1

    y_batch = sparse_tuple_from(y_batch)
    seq_len_batch = np.array(seq_len_batch)[:, 0]
    for i, pad in enumerate(np.max(seq_len_batch) - seq_len_batch):
        x_batch[i] = np.pad(x_batch[i], ((0, 0), (0, pad), (0, 0)), mode='constant', constant_values=0)

    x_batch = np.concatenate(x_batch, axis=0)
    return x_batch, y_batch, seq_len_batch, original_batch


def decode_batch(d, original, phase='training'):
    for jj in range(batch_size):  # just for visualisation purposes. we display only 2.
        values = d.values[np.where(d.indices[:, 0] == jj)]
        str_decoded = ''.join([chr(x) for x in np.asarray(values) + FIRST_INDEX])
        # Replacing blank label to none
        str_decoded = str_decoded.replace(chr(ord('z') + 1), '')
        # Replacing space label to space
        str_decoded = str_decoded.replace(chr(ord('a') - 1), ' ')
        print(str_decoded)
        output_txt = io.open("output.txt", "a", encoding="utf-8")
        result = str(jj+1) + ' ' + str_decoded + '\n'
        output_txt.writelines(result)
        output_txt.close()


def run_ctc():
    # make sure the values match the ones in generate_audio_cache.py
    merged = tf.summary.merge_all()
    with tf.Session() as session:
        saver = tf.train.import_meta_graph('model_lstm/network-1000.meta')
        saver.restore(session, tf.train.latest_checkpoint('model_lstm/'))
        
        graph = tf.get_default_graph()
        inputs, targets, seq_len, original = next_batch(train=False)
        input_x = graph.get_operation_by_name("inputs").outputs[0]
        val_feed = {"inputs:0": inputs, "seq_len:0": seq_len}
        logits = graph.get_tensor_by_name("logits:0")
   
        decoded, log_prob = tf.nn.ctc_greedy_decoder(logits, seq_len)
        
        d = session.run(decoded[0], feed_dict=val_feed)
        decode_batch(d, original, phase='validation')


if __name__ == '__main__':
      run_ctc()
