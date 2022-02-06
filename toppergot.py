# For Topper
# A small gift from Ashutosh

def formedby(e, s):
	# print('e:',e,type(e))
	# print('s:',s,type(s))

	for i in e:
		if i in s:
			f = True
		else:
			return False
	return True

			

def stum(n):
	
	result = nf(n, n)
	return result
	

def nf(n, length):
	
	if n == 0: return [""]
	if n == 1: return ["1", "0", "8"]
	
	middles = nf(n - 2, length)
	result = []
	
	for middle in middles:
		if n != length:			
			result.append("0" + middle + "0")

		result.append("8" + middle + "8")
		result.append("1" + middle + "1")
		result.append("9" + middle + "6")
		result.append("6" + middle + "9")
	return result

# Yaha se start h Topper
if __name__ == '__main__':
	
	j = int(input())
	r = stum(4)
	s = []
	for i in r:
		if formedby(str(i), str(j)):
			# print('l: ', i)
			s.append(i)
	if len(s) == 0:
		s.append(-1)

	# Done
	sp = ''
	for i in s:
		sp+=(i+',')

	for i in range(len(sp)-1):
		print(sp[i],end='')
	print()
	# s = list(map(int, s))
	# s = str(s)


	# for i in range(2,len(s)-1):
	# 	print(s[i])
	# print(s)

	# if len(i) > 1:
	# 	for i in s:
	# 		print(i,end=',')
	# elif len(s)==1:
	# 	print(s[0])

	# else:
	# 	print('Unexpected Material')
		
