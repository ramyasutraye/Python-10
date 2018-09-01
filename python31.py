first = raw_input('Enter a ch:')
if first in ('a', 'e', 'i', 'o', 'u'):
	 print "vowel"
elif first in('!', '@', '#', '$', '%', '^', '&', '(', ')'):
	print "invalid"
else:
	print "consonant"
