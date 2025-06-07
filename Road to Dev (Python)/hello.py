def world():
	print("Hello, World!")
shark = "Sammy"
class Octopus:
	def __init__(self, name, color):
		self.name = name
		self.color = color
	def printthis(self):
		print("This octopus is " + self.name + ". Oh look! His ink is " + self.color)
	def __str__(self):
		return f"Octopus(name={self.name}, color={self.color})"
x = Octopus("Chloe", "blue")
x.printthis()