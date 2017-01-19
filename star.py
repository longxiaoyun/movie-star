#encoding=utf-8
import jieba

from matplotlib import pyplot as plt

from matplotlib.font_manager import *

#定义自定义字体，文件名从1.b查看系统中文字体中来
myfont = FontProperties(fname='msyh.ttf')
#解决负号'-'显示为方块的问题  
matplotlib.rcParams['axes.unicode_minus']=False  


# 导入自定义字典
jieba.load_userdict('user_dict.txt')

def fenci(txt):
	seg_generator = jieba.cut(txt, cut_all=False)



def data():

	with open ('star.txt') as f:

		t1 = f.readlines()

	txt = r' '.join(t1)

	seg_list=jieba.cut(txt, cut_all=False)

	txt = r' '.join(seg_list)

	# print '------------------->',txt

	return txt



def wf():
	# 计算词频
	hist={}
	for word in jieba.cut(data()):
		hist[word]=hist.get(word,0)+1

	# print 'hist==========>:',hist
	# 对词频排序
	hist_sort=sorted(hist.iteritems(), key=lambda d: d[1], reverse=True)

	# print 'hist_sort=====>',hist_sort

	# print 'keys===>',hist_sort[1][1]

	plot(hist_sort)
	

def plot(result_dict):
	#调节图形大小，宽，高
	plt.figure(figsize=(6,9))

	#定义饼状图的标签，标签是列表
	print '标签====>:',result_dict[1][0]
	print '标签====>:',result_dict[2][0]
	print '标签====>:',result_dict[3][0]
	print '标签====>:',result_dict[4][0]
	print '标签====>:',result_dict[5][0]

	# labels = [result_dict[1][0],result_dict[2][0],result_dict[3][0],result_dict[4][0],result_dict[5][0]]
	labels = ['1 star','2 star','3 star','4 star','5 star']

	
	#每个标签占多大，会自动去算百分比
	sizes = [result_dict[1][1],result_dict[2][1],result_dict[3][1],result_dict[4][1],result_dict[5][1]]

	colors = ['red','yellowgreen','lightskyblue','aliceblue','chocolate']
	#将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
	explode = (0.05,0,0,0,0)
	patches,l_text,p_text = plt.pie(sizes,explode=explode,labels=labels,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 90,pctdistance = 0.6)

	#labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
	#autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
	#shadow，饼是否有阴影
	#startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
	#pctdistance，百分比的text离圆心的距离
	#patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本


	# plt.title("Baiduren Comment")
	plt.title(u'摆渡人影评',fontproperties=myfont)
	# 设置x，y轴刻度一致，这样饼图才能是圆的
	plt.axis('equal')
	plt.legend()
	plt.show()


wf()




