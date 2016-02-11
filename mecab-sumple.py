# -*- coding: utf-8 -*- 

from natto import MeCab

nm = MeCab()
#print(nm)

content = ""
fileName = '/Users/kojimakeito/Desktop/result2.txt'
result = open(fileName, 'w')
result.write("")

with MeCab('-F%f[1]') as nm:
	f = open('/Users/kojimakeito/Desktop/result.txt', 'r')
	for line in f:
		text = line
		for n in nm.parse(text, as_nodes=True):
			content += ',%s' % n.surface
			result.writelines(n.surface)
			#print n


f.close()
result.close()


		
print "COMPLATE!!!!"
