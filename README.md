# ctc_tensorflow_taiwanese_speech
Taiwanese Recognizable speech using tensorflow CTC, Deep Learning taiwanese recognization homework 2 at NTUT.

Step1. create dir and go to dir.

``` bash
$ mkdir ctc_tensorlow_speech
```

``` bash
$ cd ctc_tensorlow_speech
```

Step2. run bash file with convert audo sample rate 16.

``` bash
$ chmod +x 22k_16k.sh
```

``` bash
$ ./22k_16k.sh
```

result: generate 16k audo wave file to train/wav48/p255/wav and train/wav48/p255/wav.

Step3. run python csv convert txt file.
``` bash
$ chmod +x HW2_csv2txt.py
```

``` bash
$ chmod +x HW2_test_csv2txt.py
```

``` bash
$ python3 HW2_csv2txt.py
```

``` bash
$ python3 HW2_test_csv2txt.py
```

Step4. run tensorflow network example.(CNN, ResNet, LSTM, CNN-LSTM) 

4-1. CNN
``` bash
$ chmod +x ctc_tensorflow_save_model_cnn.py
```

``` bash
$ python3 ctc_tensorflow_save_model_cnn.py
```

4-2. Resnet
``` bash
$ chmod +x ctc_tensorflow_save_model_resnet.py
```

``` bash
$ python3 ctc_tensorflow_save_model_resnet.py
```

4-3. LSTM
``` bash
$ chmod +x ctc_tensorflow_save_model_lstm.py
```

``` bash
$ python3 ctc_tensorflow_save_model_lstm.py
```

4-4. CNN-LSTM
``` bash
$ chmod +x ctc_tensorflow_save_model_cnn_lstm.py
```

``` bash
$ python3 ctc_tensorflow_save_model_cnn_lstm.py
```

Step.5 model result plot.
``` bash
$ chmod +x data_plot.py
```

``` bash
$ python3 data_plot.py
```

Step.6 load model and test.

``` bash
$ chmod +x ctc_tensorflow_test.py
```

``` bash
$ python3 ctc_tensorflow_test.py
```

Step7. convert txt to csv file.
``` bash
$ chmod +x HW_text2csv.py
```

``` bash
$ python3 HW_text2csv.py
```
