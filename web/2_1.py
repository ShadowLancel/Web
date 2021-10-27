import math

class Sphere:
	def __init__(self, r = 1, x = 0, y = 0, z = 0):
		self.r = r
		self.x = x
		self.y = y
		self.z = z
	def get_volume(self):
		return (4 * math.pi * self.r ** 3) / 3
	def get_square(self):
		return 4 * math.pi * self.r ** 2
	def get_radius(self):
		return self.r
	def get_centre(self):
		return tuple(self.x, self.y, self.z)
	def set_radius(self, r):
		self.r = r
	def set_center(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	def is_point_inside(self, x, y, z):
		return ((x - self.x) ** 2 + (y - self.y) ** 2 + (z - self.z) ** 2) < self.r **2

ob = Sphere()
while(1):
	try:
		r = int(input("Введите радиус: \n"))
		x = int(input("Введите x: \n"))
		y = int(input("Введите y: \n"))
		z = int(input("Введите z: \n"))
		ob = Sphere(r, x, y, z)
		print("Объем: ", ob.get_volume())
		print("Площадь: ", ob.get_square())
		print("проверка наличия точки внутри сферы:")
		x = int(input("Введите x: \n"))
		y = int(input("Введите y: \n"))
		z = int(input("Введите z: \n"))
		print(ob.is_point_inside(x, y, z))
	except:
		break