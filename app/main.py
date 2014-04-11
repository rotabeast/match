from random import *
import csv

def who_are_you(dict):
	human = raw_input('Who are you?\n')
	if human in dict.viewvalues():
		matched_name = (dict[human])
		print("You got matched with: " + matched_name)
	else:
		print("Not a person in the system!")

def do_the_work(p):
	shuffle(p)
	#pairs = open("app/data/pairings.csv", "w")
	people.append(p[0])
	dict = {}
	for i in range(len(p) - 1):
		dict.update({p[i]:p[i+1]})
		#pairs.write(p[i] + "," + p[i + 1] + "\n")
	who_are_you(dict)

text_file = open("app/data/humans.txt", "r")
people = text_file.read().split(',')
do_the_work(people)
