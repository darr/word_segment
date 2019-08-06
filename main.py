#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-08-06 16:23
# Modified date : 2019-08-06 16:24
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import train
import eval

def run():
    train.run()
    eval.run()

if __name__ == "__main__":
    run()

