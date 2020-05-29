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

	def turn_column_right(self, value1, value2):
		for i in range(3):
			right = self.sides['U'].colour[value1]
			self.sides['U'].colour[value1] = self.sides['B'].colour[value2]
			self.sides['B'].colour[value2] = self.sides['D'].colour[value1]
			self.sides['D'].colour[value1] = self.sides['F'].colour[value1]
			self.sides['F'].colour[value1] = right
			value1 = value1 * 8
			value2 = value2 * 8

	def turn_column_left(self, value1, value2):
		for i in range(3):
			left = self.sides['U'].colour[value1]
			self.sides['U'].colour[value1] = self.sides['B'].colour[value2]
			self.sides['B'].colour[value2] = self.sides['D'].colour[value1]
			self.sides['D'].colour[value1] = self.sides['F'].colour[value1]
			self.sides['F'].colour[value1] = left
			value1 = value1 * 8
			value2 = value2 * 8

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

	def turn_special_right_s(self):
		temp = self.sides['R'].colour[2]
		self.sides['R'].colour[2] = self.sides['U'].colour[8]
		self.sides['R'].colour[16] = self.sides['U'].colour[16]
		self.sides['R'].colour[128] = self.sides['U'].colour[32]
		self.sides['D'].colour[8] = temp
		self.sides['D'].colour[16] = temp
		temp = self.sides['D'].colour[32]
		self.sides['D'].colour[32] = self.sides['D'].colour[16]
		self.sides['L'].colour[128] = temp
		self.sides['L'].colour[16] = temp
		temp = self.sides['L'].colour[2]
		self.sides['L'].colour[2] = self.sides['L'].colour[16]
		self.sides['U'].colour[8] = temp
		self.sides['U'].colour[16] = temp
		self.sides['U'].colour[32] = temp

	def turn_special_right_b(self):
		temp = self.sides['R'].colour[4]
		self.sides['R'].colour[4] = self.sides['U'].colour[1]
		self.sides['R'].colour[32] = self.sides['U'].colour[2]
		self.sides['R'].colour[256] = self.sides['U'].colour[4]
		self.sides['D'].colour[256] = temp
		self.sides['D'].colour[128] = temp
		temp = self.sides['D'].colour[64]
		self.sides['D'].colour[64] = self.sides['D'].colour[128]
		self.sides['L'].colour[64] = temp
		self.sides['L'].colour[8] = temp
		temp = self.sides['L'].colour[1]
		self.sides['L'].colour[1] = self.sides['L'].colour[8]
		self.sides['U'].colour[1] = temp
		self.sides['U'].colour[2] = temp
		self.sides['U'].colour[4] = temp

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
			value1 = 1
			value2 = 4
			self.turn_column_left(value1, value2)
		# if operation == 'L\'':
		# 	value = 1
		# 	self.turn_column_left(value)
		# if operation == 'M':
		# 	value = 2
		# 	self.turn_column_right(value)
		# if operation == 'M\'':
		# 	value = 2
		# 	self.turn_column_left(value)
		if operation == 'R':
			value1 = 4
			value2 = 1
			self.turn_column_right(value1, value2)
		# if operation == 'R\'':
		# 	self.turn_column_right()

	def special_operations(self, operation):
		if operation == 'F':
			value = 64
			self.turn_special_right_f()
		if operation == 'S':
			value = 8
			self.turn_special_right_s()
		if operation == 'B':
			value = 1
			self.turn_special_right_b()
