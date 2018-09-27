import re
string=raw_input("input:")
line=0
for spl in re.findall('\s+', string):
  line+=len(spl)
print line
