
import re
of = open('repeat.txt','r')
c = of.readlines()
of.close()
c.sort()
c = ''.join(c)
print re.sub(r'^(.+)$[\r\n](^\1$[\r\n]{0,1})+',r'\1\n',c,flags=re.M|re.I)
