import random 
def merge_sort(a):
	n=len(a)
	if n<2
	return a
	l=merge_sort(a[:n//2])
	r=merge_sort(a[n//2:n])
	i=j=0
	res=[]
	while i<len(l) or j<len(r):
		if not i<len(l):
			res.append(r[j])
			j+=1
		elif not j<len(r):
			res.append(l[i])
			i+=1
		elif l[i]<r[j]:
			res.append(l[i])
		else:
			res.append(r[j])
			j+=1
			return res
A  = LinkedList()
 
for i in range ( 0, 10 ) : 
  A.add ( int ( random.uniform ( 0, 10 ) ) )
 
print A
A=merge_sort(A)
print A
