#!/usr/bin/python

from __future__ import print_function
import sys

def	input(x):
	if x == "F":
		print(x)
	if x == "B":
		print(x)
	if x == "R":
		print(x)
	if x == "L":
		print(x)
	if x == "U":
		print(x)
	if x == "D":
		print(x)
	if x == "F2":
		print(x)
	if x == "B2":
		print(x)
	if x == "R2":
		print(x)
	if x == "L2":
		print(x)
	if x == "U2":
		print(x)
	if x == "D2":
		print(x)
	if x == "F'":
		print(x)
	if x == "B'":
		print(x)
	if x == "R'":
		print(x)
	if x == "L'":
		print(x)
	if x == "U'":
		print(x)
	if x == "D'":
		print(x)
	else:
		return

def create_cube(n):
	cube = []
	d = 0
	size = int(n)
	for i in range(6):
		for x in range(size):
			block = []
			for y in range(size):
				block.append(d)
				d += 1
			cube.append(block)
	print_cube(cube, size, x, y)

def print_cube(cube, size, x, y):
	cols = len(cube)
	rows = 0
	if cols:
		rows = len(cube[0])
	var = (x + 1) * (y + 1) / size * size
	for x in range(cols):
		for y in range(rows):
			print(cube[x][y], end = " ")
		if ((x + 1) % size == 0):
			print()
		# print("x = ", x)
		# print("y = ", y)
		print()
	# print("var = ", var)

def	main():
	for x in sys.argv[1].split():
		input(x)
	if len(sys.argv) > 2:
		n = sys.argv[2]
		create_cube(n)
	else:
		create_cube

main()