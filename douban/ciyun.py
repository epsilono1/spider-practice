# coding: utf-8
import csv
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def ciyun():
    with open('./comments.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        columns = [row[-1] for row in reader]
        content = ''.join(columns)
        # 分词
        cut_text = ' '.join(jieba.cut(content))

        # 加载停用词库
        with open('./停用词库.txt', 'r', encoding='utf-8') as uselessfile:
            stopwords = uselessfile.read().split('\n')

        # 生成词云图
        wc = WordCloud(
            # 不指定字体路径，会出现口字乱码
            font_path='C:/Windows/Fonts/STXINGKA.TTF',
            width=700,
            height=500,
            stopwords=stopwords
        ).generate(cut_text)

        # 保存词云图
        wc.to_file('词云图.jpg')

        # 显示词云图方案1: WordCloud
        # img = wc.to_image()
        # img.show()

        # 显示词云图方案2：matplotlib.pyplot
        # 插值：双线性插值
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.show()


ciyun()
