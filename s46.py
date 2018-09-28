import re
s=raw_input("enter the input:")
new=re.sub('[\w]+','',s)
print len(new)
