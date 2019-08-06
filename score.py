#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : score.py
# Create date : 2019-08-06 15:07
# Modified date : 2019-08-06 16:49
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from methods.hmm_cut import HmmCut
from methods.maxmatch import CutWords
from methods.max_ngram import MaxProbCut
from methods.biward_ngram import BiWardNgram
import time


def hmm_test(sentence):
    print("HMM Word Segment:")
    cuter = HmmCut()
    seglist = cuter.cut(sentence)
    print(seglist)

def max_prob_cut_test(sentence):
    print("Max ngram Word Segment:")
    cuter = MaxProbCut()
    seglist = cuter.cut(sentence)
    print(seglist)

def biward_ngram_test(sentence):
    print("Biward ngram Word Segment:")
    cuter = BiWardNgram()
    seglist = cuter.cut(sentence)
    print(seglist)

def maxmatch_test(sentence):
    cuter = CutWords()

    print("max forward Word Segment:")
    seglist = cuter.max_forward_cut(sentence)
    print(seglist)

    print("max backward Word Segment:")
    seglist = cuter.max_backward_cut(sentence)
    print(seglist)

    print("max biward Word Segment:")
    seglist = cuter.max_biward_cut(sentence)
    print(seglist)

def item_test(sentence):
    print(sentence)
    hmm_test(sentence)
    max_prob_cut_test(sentence)
    biward_ngram_test(sentence)
    maxmatch_test(sentence)

def get_score(testfile, mode):

    hmm_cuter = HmmCut()
    maxmatch_cuter = CutWords()
    maxngram_cuter = MaxProbCut()
    biwardngram_cuter = BiWardNgram()

    start_time = time.time()
    count = 1
    count_right = 0
    count_split = 0
    count_gold = 0
    process_count = 0
    with open(testfile) as f:
        for line in f:
            process_count += 1
            if process_count % 1000 == 0:
                print(process_count)
            line = line.strip()
            goldlist = line.split(' ')
            sentence = line.replace(' ','')
            if mode == 'hmm':
                inlist = hmm_cuter.cut(sentence)
            elif mode == 'forward':
                inlist = maxmatch_cuter.max_forward_cut(sentence)
            elif mode == 'backward':
                inlist = maxmatch_cuter.max_backward_cut(sentence)
            elif mode == 'biward':
                inlist = maxmatch_cuter.max_biward_cut(sentence)
            elif mode == 'maxngram':
                inlist = maxngram_cuter.cut(sentence)
            elif mode == 'biwardngram':
                try:
                    inlist = biwardngram_cuter.cut(sentence)
                except:
                    pass
            count += 1
            count_split += len(inlist)
            count_gold += len(goldlist)
            tmp_in = inlist
            tmp_gold = goldlist

            for key in tmp_in:
                if key in tmp_gold:
                    count_right += 1
                    tmp_gold.remove(key)

        P = count_right / count_split
        R = count_right / count_gold
        F = 2 * P * R / (P + R)

    end_time = time.time()
    cost = (end_time - start_time)
    print(P, R, F, cost)

    return P, R, F, cost
