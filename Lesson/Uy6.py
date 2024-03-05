import os
from random import *
os.system("cls")


class CounterStrike:
	def __init__(self):
		self._t_health = 100
		self._ct_health = 100
		self._cnt = 1
		self._t_wins = 0
		self._ct_wins = 0

	def newGame(self):
		input("Press Enter To Start New Game -> ")
		self._t_health = 100
		self._ct_health = 100
		self._cnt = 1
		self._t_wins = 0
		self._ct_wins = 0

	def damage(self, side):
		if side == "ct":
			attack = randint(35, 90)
			self._ct_health -= attack

			if self._ct_health <= 0:
				self._cnt += 1
				self._t_wins += 1
				self.tab()

		elif side == "t":
			attack = randint(35, 90)
			self._t_health -= attack

			if self._t_health <= 0:
				self._cnt += 1
				self._ct_wins += 1
				self.tab()

	def tab(self):
		print(f"Terrorists {self._t_wins}:{self._ct_wins} Counter-Terrorists")
	
	def result(self):
		if self._t_wins > self._ct_wins:
			print("****************\n*Terrorists Win*\n****************")
		elif self._ct_wins > self._t_wins:
			print("************************\n*Counter-Terrorists Win*\n************************")
		else:
			print("******\n*Draw*\n******")

class CounterTerrorist(CounterStrike):
	def __init__(self):
		self._ct_cnt = 1

class Terrorist(CounterStrike):
	def __init__(self):
		self._t_cnt = 0


game = CounterStrike()
ct = CounterTerrorist()
t = Terrorist()

game.newGame()
if t._t_cnt < 1:
	print("Wait Terrorists")
	t._t_cnt += 1

while game._cnt <= 15:
	damage = randint(0, 10)
	if damage % 2 == 0:
		game.damage("ct")
	else:
		game.damage("t")

game.result()