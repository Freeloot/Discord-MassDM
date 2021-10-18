
import discord
import time
import ctypes
import click
import os
import json

windowSize = 'mode 70,20'
os.system(windowSize)
ctypes.windll.kernel32.SetConsoleTitleW("Infamy.py")
click.clear()
client = discord.Client()



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

		print(colours.GREEN + """ ___  ________   ________ ________  _____ ______       ___    ___ 
|\  \|\   ___  \|\  _____\\   __  \|\   _ \  _   \    |\  \  /  /|
\ \  \ \  \\ \  \ \  \__/\ \  \|\  \ \  \\\__\ \  \   \ \  \/  / /
 \ \  \ \  \\ \  \ \   __\\ \   __  \ \  \\|__| \  \   \ \    / / 
  \ \  \ \  \\ \  \ \  \_| \ \  \ \  \ \  \    \ \  \   \/  /  /  
   \ \__\ \__\\ \__\ \__\   \ \__\ \__\ \__\    \ \__\__/  / /    
    \|__|\|__| \|__|\|__|    \|__|\|__|\|__|     \|__|\___/ /     
                                                     \|___|/ 
[Support] discord.gg/2NWpB3vRdy
		""" + colours.DEFUALT)

	print(" ")
	print(colours.WHITE + 'ᴡᴇʟᴄᴏᴍᴇ ᴘʟᴀʏᴇʀ.')
	print('ᴜsᴇ ᴀᴛ ʏᴏᴜʀ ᴏᴡɴ ʀɪsᴋ !')
	print('')
	print('')
	print('1) MassDM Friends list')
	print('')
	global choice
	choice = input("-> ")


	def dmfriends():
		message = input('-> Enter Message: ')
		print(" " + colours.DEFUALT)
		click.clear()

		@client.event
		async def on_connect():
			for user in client.user.friends:
				try:
					await user.send(message)
					print(f'-> messaged: {user.name}')
				except:
					print(f"-> unable to message {user.name}")
			input('Execution Completed...\n')
			click.clear()
		
	if choice == '1':
		dmfriends()
	elif choice == "2":
		print('testing')


	client.run(auth, bot=False)
Main()

print('')
print('ɢᴀᴍᴇ ᴏᴠᴇʀ !')
print('')
exit()
