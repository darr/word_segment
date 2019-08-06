#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : hmm_cut.py
# Create date : 2019-08-06 13:40
# Modified date : 2019-08-06 16:16
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

class HmmCut:
    def __init__(self):
        trans_path = './model/prob_trans.model'
        emit_path = './model/prob_emit.model'
        start_path = './model/prob_start.model'
        self.prob_trans = self.load_model(trans_path)
        self.prob_emit = self.load_model(emit_path)
        self.prob_start = self.load_model(start_path)

    def load_model(self, model_path):
        '''加载模型'''
        f = open(model_path, 'r')
        a = f.read()
        word_dict = eval(a)
        f.close()
        return word_dict

    def viterbi(self, obs, states, start_p, trans_p, emit_p):  # 维特比算法（一种递归算法）
        '''verterbi算法求解'''
        # 算法的局限在于训练语料要足够大，需要给每个词一个发射概率,.get(obs[0], 0)的用法是如果dict中不存在这个key,则返回0值
        V = [{}]
        path = {}
        for y in states:
            V[0][y] = start_p[y] * emit_p[y].get(obs[0], 0)  # 在位置0，以y状态为末尾的状态序列的最大概率
            path[y] = [y]

        for t in range(1, len(obs)):
            V.append({})
            newpath = {}
            for y in states:
                state_path = ([(V[t - 1][y0] * trans_p[y0].get(y, 0) * emit_p[y].get(obs[t], 0), y0) for y0 in states if V[t - 1][y0] > 0])
                if state_path == []:
                    (prob, state) = (0.0, 'S')
                else:
                    (prob, state) = max(state_path)
                V[t][y] = prob
                newpath[y] = path[state] + [y]

            path = newpath  # 记录状态序列
        (prob, state) = max([(V[len(obs) - 1][y], y) for y in states])  # 在最后一个位置，以y状态为末尾的状态序列的最大概率
        return (prob, path[state])  # 返回概率和状态序列

    def cut(self, sent):
        '''分词主控函数'''
        prob, pos_list = self.viterbi(sent, ('B', 'M', 'E', 'S'), self.prob_start, self.prob_trans, self.prob_emit)
        seglist = list()
        word = list()
        for index in range(len(pos_list)):
            if pos_list[index] == 'S':
                word.append(sent[index])
                seglist.append(word)
                word = []
            elif pos_list[index] in ['B', 'M']:
                word.append(sent[index])
            elif pos_list[index] == 'E':
                word.append(sent[index])
                seglist.append(word)
                word = []
        seglist = [''.join(tmp) for tmp in seglist]

        return seglist

'''
def test():
    sentence = '上午九点，在位于湖北潜江中国最大的小龙虾交易市场，商户们正在把早上刚刚收上来的小龙虾分拣、装箱、打包，准备发往全国各地。'
    print("HMM Word Segment:")
    cuter = HmmCut()
    seglist = cuter.cut(sentence)
    print(seglist)

'''
