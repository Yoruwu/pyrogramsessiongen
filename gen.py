import asyncio
import os

# checks if pyrogram is installed or not
try:
	import pyrogram
except:
	print("\nPyrogram Not Found! Installing it via pip...")
	os.system("pip3 install pyrogram")
	print("\nPyrogram Installed Successfully!")

# imports pyrogram client
from pyrogram import Client as c

# clears screen for better looks
os.system("clear")

# prints colored text
def print_line1(text):
	print("\033[38;5;226m{}\033[0m".format(text))	# yellow

def print_line2(text):
	print("\033[38;5;082m{}\033[0m".format(text))	# green

def print_line3(text):
	print("\033[38;5;208m{}\033[0m".format(text))	# light pink

# prints banner
print_line1("\nPyrogram Session String Generator\n")
print_line2("\nVERSION: Alpha - 0.0.3\n")
print_line3("\nCREATED BY: @Yoruwu\n")
print(f"\nYou can get ID and Hash on the official telegram website.\n")

#input filds for api id and hash
API_ID = input("\nEnter Your API_ID:\n > ")
API_HASH = input("\nEnter Your API_HASH:\n > ")

# prints instructions for pyrogram auth
print("\n\n Enter Telegram Phone number when asked.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)

# pyrogram magic
async def main():
	await i.start()
	ss = await i.export_session_string()
	print("\nHERE IS YOUR SESSION STRING/ID, COPY IT, DON'T SHARE!!\n")
	print(f"\n{ss}\n")


asyncio.run(main())
