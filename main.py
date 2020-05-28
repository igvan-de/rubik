import sys
import turtle
from cube import Cube

def input_check(arguments):
	valid = "U U' U2 U2' Uw u u' R R'R2 R2' Rw r r' F F' F2 F2' Fw f f' \
		D D'D2 D2' Dw d d'L L'L2 L2' Lw l l'B B'B2 B2' Bw b b' M M'E E'S S'"
	for arg in arguments:
		if arg not in valid:
			return False
	return True

def play_game(argvs):
	if len(argvs) > 0:
		arguments = argvs.split()
		if input_check(arguments) == True:
			for operation in arguments:
				# cube.turn(operation)
				x = -250
				y = 0
				size = 40
				cube.draw(x, y, size)
		else:
			print("Wrong input, please give correct input")
			return main(input())
	else:
		print("No input given")
		return main(input())


def main(argvs):
	cube = Cube()
	if argvs.lowercase = "yes":
		cube.random()
		play_game(input())
	if args.lowercase = "no":


if __name__ == "__main__":
	main(input("Do you want to play a game or see an algorithm beat this rubiks?\n"))
