#-*- coding: UTF-8 -*-
import json
import codecs


data = []
with open('comments.json') as f:
    for line in f:
        data.append(json.loads(line))



file_object = codecs.open('star.txt', 'w' ,"utf-8")

for item in data:

    # str = "%s#_#%s#_#%s#_#%s#_#%s\r\n" % (item['parentTitle'],item['parentLink'],item['author'],item['link'],item['title'].strip())
    if len(item['user_score'])>0:

		str = "%s" % json.dumps(item['user_score'][-1],ensure_ascii=False)

		# print '========',json.dumps(item['user_score'][-1],ensure_ascii=False)

		newStr = str.replace(" ","").replace("\t","").replace("\\n","").replace("\"","").strip()

		print '==============',newStr

		file_object.write(newStr)

file_object.close()
print "success"