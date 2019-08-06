# word_segment

Chinese WordSegment based on algorithms including Maxmatch (forward, backward, bidirectional), HMM, N-gram.
And Proformance compare.

# How to run?

```shell
bash run.sh
```

This command will create the environment that needed by the models.  
This project is created on the purposes of easy-on-run.  
If you want to know the details about the models, just read code.  

# Content

## MaxMatch：  
   dict.txt: 分词用词典位置  
   max_forward_cut：正向最大匹配分词  
   max_backward_cut：逆向最大匹配分词  
   max_biward_cut：双向最大匹配分词  

## HMM:  
   hmm_train.py:基于人民日报语料29W句子，训练初始状态概率，发射概率，转移概率  
             data:训练语料，放在 ./data/train.txt  
             model: 保存训练的概率模型，训练完成后可直接调用     
                  trans_path = './model/prob_trans.model'  
                  emit_path = './model/prob_emit.model'  
                  start_path = './model/prob_start.model'  

   hmm_cut.py:基于训练得到的model，结合viterbi算法进行分词    

## N-gram  

  ngram_train.py:基于人民日报语料29W句子，训练词语出现概率，2-gram条件概率  
  data: 训练语料，放在 ./data/train.txt  
  model: 保存概率模型，训练完成后可直接调用  
  word_path = './model/word_dict.model' (词语出现概率)  
  trans_path = './model/trans_dict.model'（2-gram条件概率）  
  max_ngram.py: 最大化概率2-gram分词算法  
  biward_ngram.py: 基于ngram的前向后向最大匹配算法  

## compare

1. test corpus：微软评测语料，3985 sentences   

2. proformance compare  

| Algorithm | Precision | Recall | F1-score | Cost-Time |
| --- | :---: | --- | --- | --- |
| HMM | 0.65| 0.75| 0.70 | 1.43s |
| MaxForward | 0.76 | 0.87 | 0.81 |107.74s |
| MaxBackward | 0.76 | 0.87 | 0.81 | 124.09s |
| MaxBiWard |0.76 | 0.87 | 0.81 | 229.00s|
| MaxProbNgram | 0.76 | 0.87 | 0.81 | 3.54s|
| MaxBiwardNgram | 0.74 | 0.86 | 0.80 | 0.94s|

3. result compare  

```shell
上午九点，在位于湖北潜江中国最大的小龙虾交易市场，商户们正在把早上刚刚收上来的小龙虾分拣、装箱、打包，准备发往全国各地。
HMM Word Segment:
['上午', '九点', '，', '在', '位', '于', '湖北', '潜江', '中国', '最大', '的', '小龙虾', '交易', '市场', '，', '商户', '们', '正在', '把', '早', '上', '刚', '刚收', '上来', '的', '小龙虾', '分', '拣', '、', '装箱', '、', '打包', '，', '准备', '发往', '全国', '各地', '。']
Max ngram Word Segment:
['上午', '九', '点', '，', '在', '位于', '湖北', '潜', '江', '中国', '最', '大', '的', '小', '龙虾', '交易', '市场', '，', '商', '户', '们', '正在', '把', '早上', '刚刚', '收', '上来', '的', '小', '龙虾', '分', '拣', '、', '装', '箱', '、', '打', '包', '，', '准备', '发', '往', '全国', '各地', '。']
Biward ngram Word Segment:
['上午', '九', '点', '，', '在', '位于', '湖北', '潜', '江', '中国', '最', '大', '的', '小', '龙虾', '交易', '市场', '，', '商', '户', '们', '正在', '把', '早上', '刚刚', '收', '上来', '的', '小', '龙虾', '分', '拣', '、', '装', '箱', '、', '打', '包', '，', '准备', '发', '往', '全国', '各地', '。']
max forward Word Segment:
['上午', '九', '点', '，', '在', '位于', '湖北', '潜', '江', '中国', '最', '大', '的', '小', '龙虾', '交易', '市场', '，', '商', '户', '们', '正在', '把', '早上', '刚刚', '收', '上来', '的', '小', '龙虾', '分', '拣', '、', '装', '箱', '、', '打', '包', '，', '准备', '发', '往', '全国', '各地', '。']
max backward Word Segment:
['上午', '九', '点', '，', '在', '位于', '湖北', '潜', '江', '中国', '最', '大', '的', '小', '龙虾', '交易', '市场', '，', '商', '户', '们', '正在', '把', '早上', '刚刚', '收', '上来', '的', '小', '龙虾', '分', '拣', '、', '装', '箱', '、', '打', '包', '，', '准备', '发', '往', '全国', '各地', '。']
max biward Word Segment:
['上午', '九', '点', '，', '在', '位于', '湖北', '潜', '江', '中国', '最', '大', '的', '小', '龙虾', '交易', '市场', '，', '商', '户', '们', '正在', '把', '早上', '刚刚', '收', '上来', '的', '小', '龙虾', '分', '拣', '、', '装', '箱', '、', '打', '包', '，', '准备', '发', '往', '全国', '各地', '。']
```

