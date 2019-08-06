#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : train.py
# Create date : 2019-08-06 14:32
# Modified date : 2019-08-06 16:22
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from methods.ngram_train import TrainNgram
from methods.hmm_train import HmmTrain

def do_ngram_train():
    train_data_path = './data/train.txt'
    wordict_path = './model/word_dict.model'
    transdict_path = './model/trans_dict.model'
    trainer = TrainNgram()
    trainer.train(train_data_path, wordict_path, transdict_path)

def do_hmm_train():
    train_filepath = './data/train.txt'
    trans_path = './model/prob_trans.model'
    emit_path = './model/prob_emit.model'
    start_path = './model/prob_start.model'
    trainer = HmmTrain()
    trainer.train(train_filepath, trans_path, emit_path, start_path)

def run():
    do_ngram_train()
    do_hmm_train()
