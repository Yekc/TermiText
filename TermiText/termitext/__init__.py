import platform
from os import system
import time
import sys

__version__ = "0.1.9"

class colors:
    reset = "\033[0m"
    bold = "\033[01m"
    disable = "\033[02m"
    underline = "\033[04m"
    reverse = "\033[07m"
    strikethrough = "\033[09m"
    invisible = "\033[08m"
    class fg:
        black = "\033[30m"
        red = "\033[31m"
        green = "\033[32m"
        orange = "\033[33m"
        blue = "\033[34m"
        purple = "\033[35m"
        cyan = "\033[36m"
        lightgrey = "\033[37m"
        darkgrey = "\033[90m"
        lightred = "\033[91m"
        lightgreen = "\033[92m"
        yellow = "\033[93m"
        lightblue = "\033[94m"
        pink = "\033[95m"
        lightcyan = "\033[96m"
    class bg:
        black = "\033[40m"
        red = "\033[41m"
        green = "\033[42m"
        orange = "\033[43m"
        blue = "\033[44m"
        purple="\033[45m"
        cyan = "\033[46m"
        lightgrey = "\033[47m"

def color(text = "", color = "", highlight = ""):
	if color =="red":
		result = colors.fg.red
	elif color =="lightred":
		result = colors.fg.lightred
	elif color =="orange":
		result = colors.fg.orange
	elif color =="yellow":
		result = colors.fg.yellow
	elif color =="lightgreen":
		result = colors.fg.lightgreen
	elif color =="green":
		result = colors.fg.green
	elif color =="lightcyan":
		result = colors.fg.lightcyan
	elif color =="cyan":
		result = colors.fg.cyan
	elif color =="lightblue":
		result = colors.fg.lightblue
	elif color =="blue":
		result = colors.fg.blue
	elif color =="pink":
		result = colors.fg.pink
	elif color =="purple":
		result = colors.fg.purple
	elif color =="black":
		result = colors.fg.black
	elif color =="darkgrey":
		result = colors.fg.darkgrey
	elif color =="lightgrey":
		result = colors.fg.lightgrey
	else:
		result = ""

	if highlight =="red":
		result += colors.bg.red
	elif highlight =="orange":
		result += colors.bg.orange
	elif highlight =="green":
		result += colors.bg.green
	elif highlight =="blue":
		result += colors.bg.blue
	elif highlight =="purple":
		result += colors.bg.purple
	elif highlight =="cyan":
		result += colors.bg.cyan
	elif highlight =="black":
		result += colors.bg.black
	elif highlight =="lightgrey":
		result += colors.bg.lightgrey
	else:
		result += ""

	result += text + colors.reset
	return result

def format(text = "", style = ""):
	if style =="bold":
		result = colors.bold
	elif style =="disable":
		result = colors.disable
	elif style =="underline":
		result = colors.underline
	elif style =="reverse":
		result = colors.reverse
	elif style =="strikethrough":
		result = colors.strikethrough
	elif style =="invisible":
		result = colors.invisible
	else:
		result = ""

	result += text + colors.reset
	return result

def slprint(text):
	print(text, end = "")

def get_os():
		plat = platform.system()
		if plat == "Linux":
			return "linux"
		elif plat == "Darwin":
			return "mac"
		elif plat == "Windows":
			return  "nt"

def clear():
	pass
	os = get_os()
	if os in ("linux", "mac"):
		system("clear")
	else:
		system("cls")

def slowprint(text = "", waitfor = 0.1, slice = ""):
	for i in text:
		try:
			sys.stdout.write(i + slice)
		except:
			sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(waitfor)
