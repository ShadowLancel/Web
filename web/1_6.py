from typing import ForwardRef


def cache_fn(n):
	def	cache(f):
		memor = dict()
		def func():
			if any(memor) == False or memor['count'] == n:
				memor["cache"] = f()
				memor["count"] = 1
				print("use")
			else:
				memor["count"] = memor["count"] + 1
			return memor["cache"]
		return func
	return cache

@cache_fn(n = 10)
def	get_num():
	return (123)


for i in range(1, 10):
	get_num()