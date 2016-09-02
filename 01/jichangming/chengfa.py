#encoding: utf-8

num = range(10)
nummax = 0
for x in num:
	if x > 0:
		for y in range(x+1):
			if y > 0:
				nummax = x * y
				print '%s * %s = %s' % (x, y , nummax) , 
		print '\n' 	

	



		

			