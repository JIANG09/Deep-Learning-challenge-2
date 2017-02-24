# -*- coding: utf-8 -*-
#python2
from  collections  import Counter
#打开文件，读取文件
txt = "happiness_seg.txt"
with open (txt) as f:
    text = f.read()

#删除文件中标点
punct = [", ", "。", "“", "”" , "？","; ", "：", "（", "）", "__", " "]
text_no_punct = text.replace (punct[0],"")
text_no_punct = text_no_punct.replace(punct[1],"")
text_no_punct = text_no_punct.replace(punct[2],"")
text_no_punct = text_no_punct.replace(punct[3],"")
text_no_punct = text_no_punct.replace(punct[4],"")
text_no_punct = text_no_punct.replace(punct[5],"")
text_no_punct = text_no_punct.replace(punct[6],"")
text_no_punct = text_no_punct.replace(punct[7],"")
text_no_punct = text_no_punct.replace(punct[8],"")
text_no_punct = text_no_punct.replace(punct[9],"")
text_no_punct = text_no_punct.replace(punct[10],"")

final_list = text_no_punct.split()

#构造二元词组
def word_group (word_list):
    for i  in range(len(word_list)-1):
        word_list[i]  = word_list[i] +' ' +  word_list[i+1]
        return word_list

#计算频率最高的词并输出
word_counts = Counter(word_group(final_list))
top_10 = word_counts.most_common(10)

print top_10
