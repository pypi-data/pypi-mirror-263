# !usr/bin/env python
# -*- coding:utf-8 -*-

'''
 Author       : Huang zh
 Email        : jacob.hzh@qq.com
 Date         : 2024-03-21 17:42:49
 LastEditTime : 2024-03-21 20:26:10
 FilePath     : \\hzh\\pdf2txt.py
 Description  : 
'''

from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import word_tokenize
from pypdf import PdfReader
from tqdm import trange

def get_pdf_txt(path):
    all_txt = []
    reader = PdfReader(path)
    number_of_pages = len(reader.pages)
    for i in trange(number_of_pages):
        page = reader.pages[i]
        text = page.extract_text()
        text = text.replace('-\n', '').replace('\n',' ')
        all_txt.append(text)
    return ' '.join(all_txt)

def process(text):
    # nltk.download('stopwords')
    # nltk.download('punkt')

    # 加载停用词列表
    stop_words = list(set(stopwords.words('english')))
    stop_words.extend(['int', 'float', 'llm', 'llms', 'cnn', 'rnn', 'lstm', 'rnns', 'bert', 'gpt', 'gpt1', 'gpt2',
                        'gpt3', 'chatgpt', 'gpt4', 'elmo', 'TrafficBERT', 'arXiv', 'nlp', 'acm', 'frp','rmspe',
                        'marre', 'rmsle', 'tnr', 'fnr', 'tpr', 'sft', 'emnlp'])
    
    # 分词
    words = word_tokenize(text)

    # 去除停用词
    filtered_words = [word for word in words if word.lower() not in stop_words and word.lower().isalpha()]
    filtered_words = [word for word in filtered_words if len(word) > 2]
    return filtered_words



def count_and_sort_words(text):
    # 使用Counter统计单词出现的次数
    word_count = Counter(text)
    # 按照出现频率进行排序
    sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
    return sorted_word_count

def write_word_count_to_file(word_count, output_file, counts=3):
    all_count = 0
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, count in word_count.items():
            if count >= counts:
                all_count += 1
                file.write(f"{word}\n")
    print(f"共{all_count}个单词")


def get_words_from_pdf(pdf_path, output_path):
    text = get_pdf_txt(pdf_path)
    process_text = process(text)
    sort_words = count_and_sort_words(process_text)
    write_word_count_to_file(sort_words, output_path)

if __name__ == '__main__':
    pdf_path, output_path = '123.pdf', './cs.txt'
    get_words_from_pdf(pdf_path, output_path)
    
