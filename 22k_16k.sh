#!/usr/bin/env bash

input_train_wav=/home/scl/taiwanese/train
input_test_wav=/home/scl/taiwanese/test

output_train_wav=/home/scl/Hw2/train
ouput_test_wav=/home/scl/Hw2/test

for train_wav in $(seq 1 3119)
do
      echo "Proceessing wave file train ${train_wav}.wav ."
      sox ${input_train_wav}/${train_wav}.wav -r 16000 -e signed-integer -b 16 ${output_train_wav}/p225_${train_wav}.wav
done

for test_wav in $(seq 1 346)
do
      echo "Proceessing wave file test ${test_wav}.wav ."
      if [ "${test_wav}" -lt "10" ]
      then
          sox ${input_test_wav}/${test_wav}.wav -r 16000 -e signed-integer -b 16 ${ouput_test_wav}/p225_000${test_wav}.wav
      elif [ "${test_wav}" -lt "100" ] && [ "${test_wav}" -ge "10" ]
      then
          sox ${input_test_wav}/${test_wav}.wav -r 16000 -e signed-integer -b 16 ${ouput_test_wav}/p225_00${test_wav}.wav
      elif [ "${test_wav}" -lt "1000" ] && [ "${test_wav}" -ge "100" ]
      then 
          sox ${input_test_wav}/${test_wav}.wav -r 16000 -e signed-integer -b 16 ${ouput_test_wav}/p225_0${test_wav}.wav
      fi
done
