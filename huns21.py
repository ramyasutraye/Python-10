s=raw_input("input:")
n=len(s)
if(1<=N<=100000):
  wo=s.split(" ")
  rev=[w[::-1] for w in wo]
  new=" ".join(rev)
print new
