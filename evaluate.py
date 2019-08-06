#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : eval.py
# Create date : 2019-08-06 13:18
# Modified date : 2019-08-06 16:44
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from score import get_score
from score import item_test

def run_eval():
    '''
    0.647781443332231 0.751431565552603 0.6957674364205794 1.453401803970337
    0.7561888945873121 0.8691474231820053 0.8087429315200878 105.16041398048401
    0.756098554597748 0.8682866125229237 0.8083184530290493 121.29132223129272
    0.7572781508769642 0.8693719824843744 0.8094628264770966 226.5253984928131
    0.760764030300562 0.8739005950821512 0.8134171725177012 3.427755832672119
    0.742910027361983 0.8637486432875482 0.7987851308320643 0.9492778778076172
    '''
    testfile = './data/test.txt'
    P, R, F, cost = get_score(testfile, 'hmm')
    P, R, F, cost = get_score(testfile, 'forward')
    P, R, F, cost = get_score(testfile, 'backward')
    P, R, F, cost = get_score(testfile, 'biward')
    P, R, F, cost = get_score(testfile, 'maxngram')
    P, R, F, cost = get_score(testfile, 'biwardngram')

def run_test():
    sentence = '上午九点，在位于湖北潜江中国最大的小龙虾交易市场，商户们正在把早上刚刚收上来的小龙虾分拣、装箱、打包，准备发往全国各地。'
    item_test(sentence)

def run():
    run_eval()
    run_test()

#   if __name__ == "__main__":
#       run_eval()
#       run_test()
