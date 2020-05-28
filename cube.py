import turtle
from rotate import Rotate

class Cube_side:

	def __init__(self, side, colour):
		self.side = side
		self.centre = colour
		self.colour = {
			1 : colour,
			2 : colour,
			4 : colour,
			8 : colour,
			16 : colour,
			32 : colour,
			64 : colour,
			128 : colour,
			256 : colour
		}

	def draw_square(self, x, y, size , colour):
		turtle.penup()
		turtle.goto(x, y)
		turtle.pendown()
		turtle.color("black", colour)
		turtle.begin_fill()
		for i in range(4):
			turtle.forward(size)
			turtle.left(90)
		turtle.end_fill()

	def draw_side(self, x, y, size):
		self.draw_square(x, y, size, self.colour[1])
		self.draw_square(x + size, y, size, self.colour[2])
		self.draw_square(x + (2 * size), y, size, self.colour[4])
		self.draw_square(x, y - size, size, self.colour[8])
		self.draw_square(x + size, y - size, size, self.colour[16])
		self.draw_square(x + (2 * size), y - size, size, self.colour[32])
		self.draw_square(x, y - (2 * size), size, self.colour[64])
		self.draw_square(x + size, y - (2 * size), size, self.colour[128])
		self.draw_square(x + (2 * size), y - (2 * size), size, self.colour[256])

class Cube:

	def __init__(self):
		self.sides = {
		'L' : Cube_side('L', "orange"),
		'F' : Cube_side('F', "green"),
		'R' : Cube_side('R', "red"),
		'B' : Cube_side('B', "blue"),
		'U' : Cube_side('U', "white"),
		'D' : Cube_side('D', "yellow") }
		self.turns = Rotate(self.sides)

	def draw(self, x, y, size):
		window = turtle.Screen()
		turtle.speed(0)
		turtle.pensize(2)
		turtle.tracer(0, 0)
		side_size = size * 3
		self.sides['L'].draw_side(x, y, size)
		self.sides['F'].draw_side(x + side_size, y, size)
		self.sides['R'].draw_side(x + (2 * side_size), y, size)
		self.sides['B'].draw_side(x + (3 * side_size), y, size)
		self.sides['U'].draw_side(x + side_size, y + side_size, size)
		self.sides['D'].draw_side(x + side_size, y - side_size, size)
		turtle.hideturtle()
		turtle.update()

	def turn(self, operation):
		rows = "U U' U2 U2' Uw u u' D D' D2 D2' Dw d d'B B'B2 B2' Bw b b' E E'"
		column = "R R'R2 R2' Rw r r' L L'L2 L2' Lw l l' M M'"
		special = "F F' F2 F2' Fw f f' B B'B2 B2' Bw b b' S S'"
		if operation in rows:
			self.turns.rows_operations(operation)
		if operation in column:
			self.turns.column_operations(operation)
		if operation in special:
			self.turns.special_operations(operation)
		turtle.update()
