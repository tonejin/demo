#! python3
# _*_ coding:utf-8 _*
# _Author_  : Jin Tone
# _Date_    : 2018/2/26

# 解决8皇后的问题 page:178
import random


def conflict(state, nextX):
	nextY = len(state)
	for i in range(nextY):
		if abs(state[i] - nextX) in (0, abs(nextY - i)):
			return True
	return False


def queens(num=8, state=()):
	for pos in range(num):
		if not conflict(state, pos):
			# print(conflict(state, pos))
			if len(state) == num - 1:
				yield (pos,)
			else:
				for result in queens(num, state + (pos,)):
					yield ((pos,) + result)


def prettyprint(solution):
	def line(pos, length=len(solution)):
		return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)
	
	for pos in solution:
		print(line(pos))


# prettyprint(random.choice((list(queens(8)))))

# print(len(list(queens(9))))

# print(list(queens(4,(1,3,0))))
def printqueens(num=4):
	li = list(queens(num))
	print("Total solutions: %d" %len(li))
	# for i in li:
	# 	print(i)
	li2=random.choice(li)
	prettyprint(li2)
	print(li2)

queen = 6
printqueens(queen)

# print((list(queens(queen))))