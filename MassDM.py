""" BY INFAMY """
import discord
import time
import ctypes
import click
import os
import json

windowSize = 'mode 85,20'
os.system(windowSize)
ctypes.windll.kernel32.SetConsoleTitleW("Infamy")
click.clear()
client = discord.Client()

try:
	os.system('cls')
except:
	pass

class colours:
	GREEN = '\033[32m' 
	WHITE = '\033[37m'
	DEFUALT = '\033[m'
	BLACK = '\033[30m'
	RED = '\033[31m'
	BLUE = '\033[34m'
	YELLOW = '\033[33m'

def Main():



	global auth
	auth = None
	filename = 'token.json'
	with open(filename) as f:
		config = json.load(f)
		auth = config.get('token')

		print(colours.GREEN + """
                              |\      _,,,---,,_
                        ZZZzz /,`.-'`'    -.  ;-;;,_
                             |,4-  ) )-,_. ,\ (  `'-'
                            '---''(_/--'  `-'\_)  Infamy

                        [Support] discord.gg/g7up26STds
		""" + colours.GREEN)
	try:
		ctypes.windll.kernel32.SetConsoleTitleW(f"{os.getlogin()} | Token: {auth}")
	except:
		ctypes.windll.kernel32.SetConsoleTitleW(f"Infamy's Client | Token: {auth}")

	print('')
	print('')


	def dmfriends():
		print(" " + colours.GREEN)
		message = input('Infamy' + colours.WHITE + '@' + colours.GREEN + 'message: ' + colours.GREEN)
		click.clear()

		@client.event
		async def on_connect():
			for user in client.user.friends:
				try:
					await user.send(message)
					print('Infamy' + colours.WHITE + '@' + colours.GREEN + 'messaged: ' + user.name + colours.WHITE )
				except:
					print('Infamy' + colours.WHITE + '@' + colours.GREEN + 'unable to message: ' + user.name + colours.WHITE )
			print(colours.GREEN + 'Execution Completed...\n' + colours.DEFUALT)
		
	dmfriends()


	client.run(auth, bot=False)
Main()
