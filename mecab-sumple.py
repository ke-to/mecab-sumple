# -*- coding: utf-8 -*- 

from natto import MeCab
import re

nm = MeCab()
#print(nm)

content = ""
fileName = raw_input("Output File name write now! > ")
fileName2 = raw_input("Input file name write now! > ")

result = open(fileName, 'w')
result.write("")

with MeCab('-F%f[1]') as nm:
	f = open(fileName2, 'r')
	for line in f:
		text = line
		for n in nm.parse(text, as_nodes=True):
			if re.compile('形容詞|感動詞|固有名詞').search(n.feature):
				content += ',%s' % n.surface
				result.writelines(',%s' % n.surface)
				print n.surface


f.close()
result.close()


		
print "COMPLATE!!!!"
