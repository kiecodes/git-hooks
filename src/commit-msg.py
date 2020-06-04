#!/usr/bin/python

import sys
import re
from submodules.rules import rules
from phue import Bridge

HUE_ACTIVE = False
HUE_BRIDGE_IP = "<enter your ip here>"
HUE_INDICATOR_LIGHT_NAME = "<enter the name of the light you want to control from this hook here>"

def main():
	with open(sys.argv[1], "r") as fp:
		lines = fp.readlines()

		for idx, line in enumerate(lines):

			if line.strip() == "# ------------------------ >8 ------------------------":
				break

			if line[0] == "#":
				continue

			if not line_valid(idx, line):
				hue_red()
				show_rules()
				sys.exit(1)

	hue_green()
	sys.exit(0)

def line_valid(idx, line):
	if idx == 0:
		return re.match("^[A-Z].{,48}[0-9A-z \t]$", line)
	elif idx == 1:
		return len(line.strip()) == 0
	else:
		return len(line.strip()) <= 72

def show_rules():
	print(rules)

def hue_red():
	if not HUE_ACTIVE:
		return 

	b = Bridge(HUE_BRIDGE_IP)
	b.connect()
	b.set_light(HUE_INDICATOR_LIGHT_NAME, 
		{
			"on":True,
			"bri":254,
			"xy":[0.6809, 0.3011]
		}
	)

def hue_green():
	if not HUE_ACTIVE:
		return 

	b = Bridge(HUE_BRIDGE_IP)
	b.connect()
	b.set_light(HUE_INDICATOR_LIGHT_NAME, 
		{
			"on":True,
			"bri":254,
			"xy":[0.188071151799067,0.7032850275650089]
		}
	)

if __name__ == "__main__":
	main()