# ccbert
适用于中国海关的BERT预训练过程。
与原版BERT差异：
1. 删除判断两条句子是否是上下文的预训练任务。
2. 新增判断商品要素名称和要素内容是否对齐任务。
3. MARK单词操作，加强MARK整个要素内容操作。


优势：
相比较于原版BERT和RoBERTa，在海关税率预测任务中，使用新预训练任务和预训练数据的CC-BERT取得了最优效果，比BERT和RoBERT提升2.11%。适用于多种以海关语料为基础的自然语言处理任务。
