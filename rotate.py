class Rotate():

	def __init__(self, sides):
		self.sides = sides

	def turn_row(self, value):
		for i in range(3):
			left = self.sides['L'].colour[value]
			self.sides['L'].colour[value] = self.sides['F'].colour[value]
			self.sides['F'].colour[value] = self.sides['R'].colour[value]
			self.sides['R'].colour[value] = self.sides['B'].colour[value]
			self.sides['B'].colour[value] = left
			value = value * 2

	def turn_column(self, value):
		for i in range(3):
			left = self.sides['F'].colour[value]
			self.sides['F'].colour[value] = self.sides['D'].colour[value]
			self.sides['D'].colour[value] = self.sides['B'].colour[value]
			self.sides['B'].colour[value] = self.sides['U'].colour[value]
			self.sides['U'].colour[value] = left
			value = value * 8

	def rows_operations(self, operation):
		if operation == 'U':
			value = 1
			self.turn_row(value)
		if operation == 'E':
			value = 8
			self.turn_row(value)
		if operation == 'D':
			value = 64
			self.turn_row(value)

	def column_operations(self, operation):
		if operation == 'L':
			value = 1
			self.turn_column(value)
		if operation == 'M':
			value = 2
			self.turn_column(value)
		if operation == 'R':
			value = 4
			self.turn_column(value)
