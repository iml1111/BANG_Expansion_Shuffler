"""	BANG_Expansion_Shuffler	"""
"""	     	BY IML  		"""
"""	shin10256|gmail.com   	"""	
"""	shino1025.blog.me    	"""
"""	github.com/iml1111   	"""

from os import system
from random import *
from card_list import List, Last_list

min_turn = 10
max_turn = 13

def Game_start():
	system("cls")
	print("\t\t\t\t\tBANG_EXPANSION_SHUFFLER \t\t")
	for i in range(101): print("-",end='')
	print("\n\t\t\t\t\t\t\t [Ver. 0.1]")
	print("\n\t\t\t\t\t\t\t by IML")
	for i in range(101): print("-",end='')
	print()
	print("\t\t\t[*] 본 프로그램은 뱅 확장판 상황 카드 자동 셔플러입니다.\n")
	print("\t\t\t[*] 상황 카드는 총 ",min_turn,"~",max_turn,"장 사이에서 랜덤이며,\n")
	print("\t\t\t[*] 라스트 카드가 나오기 1 턴 전에 알려드립니다.\n")
	print("\t\t\t[*] 게임에 필요한 모든 준비를 마치신 후, \n")
	print("\t\t\t[*] 보완관이 엔터 키를 눌러 게임을 진행해주십시오.\n")
	input("\t\t\t\t\t >> PRESS ENTER KEY <<")


def Game_progress():
	turn = 1
	Total_Turns = randrange(min_turn, max_turn+1) - 1
	Card_List = List
	
	for i in range(111):
		shuffle(Card_List)

	for card in Card_List:

		Game_board(card,turn)

		if turn == Total_Turns:
			print("\n\t\t\t\t!!!! 다음 턴에 라스트 카드가 등장합니다 !!!!")
			for i in range(101): print("-",end='')
		input("\n\t\t\t\t >> Press ENTER Key for Next Turn <<")
		if turn == Total_Turns: break
		else: turn += 1
		

def Last_Game():
	card = choice(Last_list)
	Game_board(card)
	
	print("\n\t\t\t\t\t  !!!! This is Last Card !!!!")
	for i in range(101): print("-",end='')
	input("\n\t\t\t\t >> Press ENTER Key for Game OVER <<")
	system("cls")
	for i in range(5): print("OVER!!!!!!!!!!!!!!!!")
	print("Thank you.")


def Game_board(card, turn=None):
	system("cls")
	print("\t\t\t\t\tBANG_EXPANSION_SHUFFLER \t\t")
	for i in range(101): print("-",end='')
	print("\n")
	if card in Last_list:
		print("\t\t\t\t\t\t\t{TURN of Last}")
	else:
		print("\t\t\t\t\t\t\t{TURN of", turn ,"}")
	print()
	etitle = "<" + card["eng_title"].upper() + ">"
	print("%66s" % etitle)
	htitle = "[" + card["han_title"] + "]\n"
	print("%66s" % htitle)
	dtitle = "-- Description -- "
	print("%72s" % dtitle + "\n")

	description = card["description"].split('.')
	for des in description:
		enter_count = 0
		for i in des: 
			print(i,end='')
			enter_count += 1
			if enter_count >= 50 and\
				(i == ' ' or i == ',' or i ==')'):
				print("")
				enter_count = 0

		if des.find('.') == -1 and len(des) >= 4: print(".")
		else: print("")

	print("\n")
	for i in range(101): print("-",end='')


if __name__ == '__main__':
	Game_start()
	Game_progress()
	Last_Game()

	