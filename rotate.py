class Rotate():

	def __init__(self, sides):
		self.sides = sides

	def turn_row_right(self, value):
		for i in range(3):
			left = self.sides['L'].colour[value]
			self.sides['L'].colour[value] = self.sides['F'].colour[value]
			self.sides['F'].colour[value] = self.sides['R'].colour[value]
			self.sides['R'].colour[value] = self.sides['B'].colour[value]
			self.sides['B'].colour[value] = left
			value = value * 2

	def turn_row_left(self, value):
		for i in range(3):
			left = self.sides['B'].colour[value]
			self.sides['B'].colour[value] = self.sides['R'].colour[value]
			self.sides['R'].colour[value] = self.sides['F'].colour[value]
			self.sides['F'].colour[value] = self.sides['L'].colour[value]
			self.sides['L'].colour[value] = left
			value = value * 2

	def turn_column_right(self, value):
		for i in range(3):
			left = self.sides['F'].colour[value]
			self.sides['F'].colour[value] = self.sides['D'].colour[value]
			self.sides['D'].colour[value] = self.sides['B'].colour[value]
			self.sides['B'].colour[value] = self.sides['U'].colour[value]
			self.sides['U'].colour[value] = left
			value = value * 8

	def turn_column_left(self, value):
		for i in range(3):
			left = self.sides['U'].colour[value]
			self.sides['U'].colour[value] = self.sides['B'].colour[value]
			self.sides['B'].colour[value] = self.sides['D'].colour[value]
			self.sides['D'].colour[value] = self.sides['F'].colour[value]
			self.sides['F'].colour[value] = left
			value = value * 8

	def turn_special_right_f(self):
		temp = self.sides['R'].colour[1]
		self.sides['R'].colour[1] = self.sides['U'].colour[64]
		self.sides['R'].colour[8] = self.sides['U'].colour[128]
		self.sides['R'].colour[64] = self.sides['U'].colour[256]
		self.sides['D'].colour[4] = temp
		self.sides['D'].colour[2] = temp
		temp = self.sides['D'].colour[1]
		self.sides['D'].colour[1] = self.sides['D'].colour[2]
		self.sides['L'].colour[256] = temp
		self.sides['L'].colour[32] = temp
		temp = self.sides['L'].colour[4]
		self.sides['L'].colour[4] = self.sides['L'].colour[32]
		self.sides['U'].colour[64] = temp
		self.sides['U'].colour[128] = temp
		self.sides['U'].colour[256] = temp

	def rows_operations(self, operation):
		if operation == 'U':
			value = 1
			self.turn_row_right(value)
		if operation == 'U\'':
			value = 1
			self.turn_row_left(value)
		if operation == 'E':
			value = 8
			self.turn_row_right(value)
		if operation == 'E\'':
			value = 8
			self.turn_row_left(value)
		if operation == 'D':
			value = 64
			self.turn_row_right(value)
		if operation == 'D\'':
			value = 64
			self.turn_row_left(value)

	def column_operations(self, operation):
		if operation == 'L':
			value = 1
			self.turn_column_right(value)
		if operation == 'L\'':
			value = 1
			self.turn_column_left(value)
		if operation == 'M':
			value = 2
			self.turn_column_right(value)
		if operation == 'M\'':
			value = 2
			self.turn_column_left(value)
		if operation == 'R':
			value = 4
			self.turn_column_right(value)
		if operation == 'R\'':
			self.turn_column_right()

	def special_operations(self, operation):
		if operation == 'F':
			value = 64
			self.turn_special_right_f()
		if operation == 'S':
			value = 8
			self.turn_special_right_S()
		if operation == 'B':
			value = 1
			self.turn_special_right_B()
