def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
		
	print(tuple(l))
		
printValues()
#############
ls = [*range(1, 21)]

x = filter(lambda x:x%2==0, ls)
print(list(x))
#############
x = map(lambda x:x**2, filter(lambda x:x%2==0, [1,2,3,4,5,6,7,8,9,10]))
print(list(x))
###############
def square(x):
  return x * x

x = map(lambda x:x*x, [1,2,3,4,5,6,7])
print(list(x))