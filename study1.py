def checkIndex(key):
	if not isinstance(key, (int, key)):
		raise TypeError
	if key < 0:
		raise IndexError


class ArithmeticSequence(object):
	def __init__(self, start=0, step=1):
		self.start = start
		self.step = step
		self.changed = {}
	
	def __getitem__(self, key):
		checkIndex(key)
		try:
			return self.changed[key]
		except KeyError:
			return self.start + key * self.step
	
	def __setitem__(self, key, value):
		checkIndex(key)
		self.changed[key] = value


s = ArithmeticSequence()
print(s[0])


##################
class TestIterator(object):
	value = 0
	
	def __next__(self):
		self.value += 1
		if self.value > 10: raise StopIteration
		return self.value
	
	def __iter__(self):
		return self


ti = TestIterator()

nested = [[1, 2], [3, 4], [5]]
nested = (['foo', ['bar', ['baz']]], [1, 2], [3, 4], [5])

nested = ([1])


def flatten(nested):
	try:
		try:
			nested + ""
		except TypeError:
			pass
		else:
			raise TypeError
		for sublist in nested:
			for element in flatten(sublist):
				yield element
	except TypeError:
		yield nested


for num in flatten(nested):
	print(num)  # num


def repeater(value):
	while True:
		new = (yield value)
		if new is not None: value = new


r = repeater(42)


