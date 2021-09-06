#Libraries
import discord
import time
import ctypes
import click

#Program
ctypes.windll.kernel32.SetConsoleTitleW("Infamy's Messenger.py")
click.clear()

class colours:
	GREEN = '\033[32m' 
	WHITE = '\033[37m'
	DEFUALT = '\033[m'
	BLACK = '\033[30m' # Kinda Usesless for black terminals
	RED = '\033[31m'
	BLUE = '\033[34m'
	YELLOW = '\033[33m'

def Main():
	print(colours.GREEN + """██╗███╗░░██╗███████╗░█████╗░███╗░░░███╗██╗░░░██╗
██║████╗░██║██╔════╝██╔══██╗████╗░████║╚██╗░██╔╝
██║██╔██╗██║█████╗░░███████║██╔████╔██║░╚████╔╝░
██║██║╚████║██╔══╝░░██╔══██║██║╚██╔╝██║░░╚██╔╝░░
██║██║░╚███║██║░░░░░██║░░██║██║░╚═╝░██║░░░██║░░░
╚═╝╚═╝░░╚══╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░╚═╝░░░
[Support] discord.gg/FmFKUAPagK
	""" + colours.DEFUALT)

        
	client = discord.Client()
	print(" ")
	print(colours.BLUE + 'ᴡᴇʟᴄᴏᴍᴇ ᴘʟᴀʏᴇʀ.')
	print('ᴜsᴇ ᴀᴛ ʏᴏᴜʀ ᴏᴡɴ ʀɪsᴋ !')
	print(' ')
	message = input('Enter Message: ')
	AUTH = input('Enter Token: ')
	print(" " + colours.DEFUALT)
	click.clear()

	@client.event
	async def on_connect():
		for user in client.user.friends:
			try:
				await user.send(message)
				print(f'messaged: {user.name}')
			except:
				print(f"unable to message {user.name}")
		print(' ')
		print('ɢᴀᴍᴇ ᴏᴠᴇʀ !')
		print('Window Closing In T -10')
		time.sleep(10)
		exit()

	client.run(AUTH, bot=False)

Main()
