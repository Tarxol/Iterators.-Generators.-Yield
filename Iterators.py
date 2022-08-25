class FlatIterator:
	def __init__(self, n: []):
		self.new_list = n
		self.index = 0
		self.merger_list= []
	def __iter__(self):
		self.d = (len(self.new_list))
		self.e = 0
		for a in self.new_list:
			self.merger_list.extend(a)
		return self
	def __next__(self):
		x = None
		len_list = (len(self.merger_list)-1)
		if len_list >= self.index:
			x = self.merger_list[self.index]
			self.index += 1
			return x
		raise StopIteration

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

for item in FlatIterator(nested_list):
	print(item)

print('-' * 20)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

