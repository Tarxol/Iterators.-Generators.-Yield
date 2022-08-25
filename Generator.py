
def flat_generator(n: []):
	for a in n:
		for b in a:
			yield b

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

for item in  flat_generator(nested_list):
	print(item)