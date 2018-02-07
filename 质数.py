
class Number(object):
	def check(self):
		#检查数字是否为质数
		n = int(input('请输入要检查的数字：') )
		s = 0
		for i in range(2,n):
			if n % i == 0:
				s += 1
				break
		if n == 1:
			print('\n __ 不是质数 __ \n')
		elif s == 0:
			print('\n __ 是质数 __ \n')
		else:
			print('\n __ 不是质数 __ \n')

	def range_1(self):
		#遍历范围内的质数
		a = int(input('请输入开头：',))
		z = int(input('请输入结尾：',))
		s = 0

		if a == 1:
		  #避免出现1这个非质数最后输出为质数
			a = 2

		for j in range(a,z+1):
		#j 是遍历范围
			for i in range(2,j):
			# i 是从2到自身的遍历除法过程。
				if j % i == 0:
				#若余数为0则不是质数 就把s变成 1 break
					s += 1
					break
			if s == 0:
			#最后遍历完 s没有变成1 则是质数
				print(j)
			s = 0 #最后把s还原成0

	def separate(self):
		'''分解质因数'''
		n = int(input('请输入数字：'))
		k = 2 #假设为最小质数
		l = [] #因数列表，把解出来的因数都放里面
		
		end = n
		while n > 1:
		#当 n > k 时正面有可能被分解
			if n % k == 0:
			# 当k 为 n 的 因数时 把分解的因数 k 放出 l 中
				l.append(k)
				n /= k
			else:
			# 若不行 k慢慢累加 
				k += 1
		if len(l) == 0:
			print ('这个数字为质数，不能分解')
		else:
			print ('%d =' %end,end=(' '))
			for j in range(len(l)):
				#最后把因数列表 l 打印出来
				if j == len(l)-1:
					#排除最后的一个 乘号
					p = '%d' % int(l[j])
				else:
					p = '%d * ' % int(l[j])
				print (p , end = ' ')
		print ('\n最后除完后的数为:',int(n))

	def start(self):
		i = int(input('>'))
		if i == 1 :
			run.check()
		elif i == 2:
			run.range_1()
		elif i == 3:
			run.separate()
		else:
			run.start()
run  = Number()
while True:
	print ('-------------- \n--------------')
	print ('检查是否为质数:1')
	print ('遍历范围内的质数范围:2')
	print ('分解质因数:3')
	run.start()

