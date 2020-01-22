import re
import collections #词频统计
import numpy as np 
import jieba #结巴分词
import wordcloud #词云展示
from PIL import Image 
import matplotlib.pyplot as plt

#读取文件
f = open('聊天记录.txt', encoding='utf-8')
string_data = f.read()
f.close()
#文本预处理，删除聊天记录中的日期时间/换行缩进/特殊符号
pattern = re.compile(r'(\d+-\d+-\d+ \d+:\d+:\d+)|(\t|\n|\[|\]|\_)')
string_data = re.sub(pattern, '', string_data)
#文本分词
word_list_exact = jieba.cut(string_data, cut_all = False) # 精确模式分词
object_list = []
#自定义移除词库，包含各种ID/备注/常用助词副词/标点及空格/图片表情等
remove_words = [u'她的ID', u'你的ID', u'她的备注', u'的', u'，', u'和', u'是', u'对', u'💕',
                u'能', u'都', u'。', u' ', u'、', u'中', u'在', u'了', u'时候', u'今天',
                u'要', u'人', u'找', u'这', u'还有', u'你', u'我', u'嗯', u'啊', u'先',
                u'如果', u'我们', u'呢', u'嘛', u'吗', u'呀', u'你们', u'不过', u'咋',
                u'啦', u'什么', u'嘞', u'不', u'哦', u'去', u'吧', u'这么', u'说', u'会',
                u'个', u'知道', u'小妹', u'：', u'=', u'~', u'很', u'有', u'哈', u'就',
                u'还是', u'不会', u'现在', u'那', u'应该', u'也', u'表情', u'可以', u'上',
                u'点', u'刚刚', u'图片', u'还', u'太', u'多', u'跟', u'然后', u'得', u'?',
                u'？', u'没'] 
for word in word_list_exact: #将不在移除词库中的词添加到object_list
    if word not in remove_words:
        object_list.append(word) 
#词频统计
word_counts = collections.Counter(object_list)
word_counts_top10 = word_counts.most_common(10) #检查词频前10数据
print (word_counts_top10)
#生成词云
mask = np.array(Image.open('timg.jfif')) #词云背景
wc = wordcloud.WordCloud(
    scale=16,   #分辨率
    font_path='C:/Windows/Fonts/simhei.ttf', #字体
    mask=mask, #背景
    max_words=350, #最大词数
    max_font_size=250 #最大字体
)
wc.generate_from_frequencies(word_counts)   #生成词云
image_colors = wordcloud.ImageColorGenerator(mask)  #从背景图建立颜色方案
wc.recolor(color_func=image_colors) #将词云颜色设置为背景图方案
plt.imshow(wc) #显示词云
plt.axis('off') #关闭坐标轴
plt.show() #显示图像
