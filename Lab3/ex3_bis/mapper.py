#!/usr/bin/python3
import sys
for reducer_trigger in sys.stdin:
	trigger = reducer_trigger.strip()
	trigger = trigger.split("\t")
	print("{trigger}\t{count}".format(trigger=trigger, count=1))