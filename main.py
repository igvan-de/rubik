#!/usr/bin/python

from __future__ import print_function
import sys
import matplotlib.colors

def	input(x, cube, n):
	if "F" in x:
		if "\'" in x:
			rotate_front_l(cube, n)
		elif "2" in x:
			print("2e", x)
		else:
			rotate_front_r(cube, n)
	if "B" in x:
		if "\'" in x:
			print(x)
		elif "2" in x:
			print("2e", x)
		else:
			print(x)
	if "R" in x:
		if "\'" in x:
			print(x)
		elif "2" in x:
			print("2e", x)
		else:
			print(x)
	if "L" in x:
		if "\'" in x:
			print(x)
		elif "2" in x:
			print("2e", x)
		else:
			print(x)
	if "U" in x:
		if "\'" in x:
			print(x)
		elif "2" in x:
			print("2e", x)
		else:
			print(x)
	if "D" in x:
		if "\'" in x:
			print(x)
		elif "2" in x:
			print("2e", x)
		else:
			print(x)
	else:
		return

def create_cube(n):
	cube = []
	size = int(n)
	colors = ["\033[41m   \033[0m", "\033[43m   \033[0m", "\033[44m   \033[0m",  "\033[42m   \033[0m", "\33[48;2;255;165;0m   \033[0m", "\033[47m   \033[0m"] #need to find orange ansi code!!
	d = str(colors[0])
	k = 0
	for i in range(6):
		i += 1
		for x in range(size):
			x += 1
			block = []
			for y in range(size):
				y += 1
				block.append(d)
				block.extend([k])
				k += 1 #//needed to give value to blocks on each side of the cube. To swap the colors later! Or check if possible to swap by color and not by index
			cube.append(block)
			if (x * y == size * size):
				if (i == 1):
					d = colors[1]
				if (i == 2):
					d = colors[2]
				if (i == 3):
					d = colors[3]
				if (i == 4):
					d = colors[4]
				if (i == 5):
					d = colors[5]
	return (cube)

def print_cube(cube, size):
	cols = len(cube)
	if cols:
		rows = len(cube[0])
	for x in range(cols):
		for y in range(rows):
			print(cube[x][y], end = " ")
		if ((x + 1) % size == 0):
			print()
		if ((y + 1) % size == 0):
			print()
		print()

def	rotate_front_r(cube, n):
	size = int(n)
	cube[3] = cube[6]		#yellow becomes blue
	cube[6] = cube[17]		#blue becomes white
	cube[9] = cube[3]		#green becomes blue
	cube[15] = cube[10]		#white becomes green
	print_cube(cube, size)

def	rotate_front_l(cube, n):
	size = int(n)
	cube[3] = cube[10]
	cube[6] = cube[4]
	cube[9] = cube[15]
	cube[15] = cube[7]
	print_cube(cube, size)

def	main():
	if len(sys.argv) > 2:
		n = sys.argv[2]
		cube = create_cube(n)
	else:
		cube = create_cube
	for x in sys.argv[1].split():
		input(x, cube, n)

main()