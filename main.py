import sys
import turtle
from cube import Cube

def input_check(arguments, valid):
	for arg in arguments:
		if arg not in valid:
			return False
	return True

def play_game(argvs, cube, valid):
	# solver = Solved()
	if len(argvs) > 0:
		arguments = argvs.split()
		if input_check(arguments, valid) == True:
			for operation in arguments:
				cube.turn(operation)
				# if solver.solved(cube) == False: to give player opportunity to check the cube during game
				# 	return play_game(input())
				cube.draw(-250, 0, 40)
			return(play_game(input(), cube, valid))
		else:
			print("Wrong input, please give correct input")
			return(play_game(input(), cube, valid))
	else:
		print("No input given")
		return(play_game(input(), cube, valid))

def main(argvs):
	cube = Cube()
	valid = "U U' U2 U2' Uw u u' R R'R2 R2' Rw r r' F F' F2 F2' Fw f f' \
	D D' D2 D2' Dw d d'L L' L2 L2' Lw l l' B B' B2 B2' Bw b b' M M' E E' S S'"
	if argvs.lower() == 'yes':
		cube.random_display(-250, 0, 40, valid.split())
		cube.draw(-250, 0, 40)
		play_game(input(), cube, valid)
	if argvs.lower() == 'no':
		print("let the algorithm beat this rubiks")
		# solver = Solved()
		# solver(cube.random())

if __name__ == "__main__":
	main(input("Do you want to play a game or see an algorithm beat this rubiks?\n\
Say 'yes' to play self, say 'no' to let an algortihm play\n"))

			# self.sides['L'].colour[1] = self.sides['F'].colour[1]
