def oddeven(a):
	if a%2==0:
		print("even");
	else:
		print("odd");
def mul2():
	try:
		b=int(input())
		a=int(input())
		oddeven(b*a)
	except:
		print('invalid');
