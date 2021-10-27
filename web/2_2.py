class Matrix:
	def __init__(self, *args):
		self.matrix = []
		if (len(args) > 1):
			for var in args:
				self.matrix.append(var)
		else:
			self.matrix = args[0]
	def print_matrix(self):
		for var in self.matrix:
			for item in var:
				print(item, end= " ")
			print()

	## Операции сравнения ##
	def __eq__(self, other):
		return not self.determinant() - other.determinant()

	def __ne__(self, other):
		return self.determinant() - other.determinant() == 0

	def __gt__(self, other):
		return self.determinant() > other.determinant()

	def __lt__(self, other):
		return self.determinant() < other.determinant()

	def __ge__(self, other):
		return self.determinant() >= other.determinant()

	def __le__(self, other):
		return self.determinant() <= other.determinant()

	## Сложение Матриц ##
	def __add__(self, other):
		result = [[] * len(self.matrix)]* len(self.matrix)
		for i in range(len(self.matrix)):    
			for j in range(len(self.matrix[0])): 
				result[i][j] + other.matrix[i][j] 
		return result

	## Умножение Матриц ##
	def __mul__(self, other):
		result_matrix = [[0 for i in range(len(self.matrix))] for i in range(len(other.matrix))]
		for i in range(len(self.matrix)):
			for j in range(len(other.matrix[0])):
				for k in range(len(other.matrix)):
					result_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
		return result_matrix

	## Определение детерменанта ##
	def det2(self):
		return (self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0])
	def minor(self, i, j):
		matrix = []		
		for y in range(len(self.matrix)):
			if (y != i):
				matrix.append([
					self.matrix[y][x]
					for x in range(len(self.matrix[y]))
						if (x != j)
				])
		return matrix 
	def determinant(self):
		size = len(self.matrix)
		ret = 0
		if size == 2:
			return self.det2()
		for j in range(size):
			matrix = Matrix(self.minor(0, j))
			ret += (-1) ** j * self.matrix[0][j] * matrix.determinant()
		return ret

ob = Matrix([1, 2, 3], [2, 3, 1], [2, 1, 4])
ob.print_matrix()
print(ob.determinant())
print(ob > ob)

m = Matrix(ob * ob)

m.print_matrix()