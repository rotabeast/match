from random import *
import csv

def who_are_you(dict):
	human = raw_input('Who are you?\n')
	if human in dict.viewvalues():
		matched_name = (dict[human])
		print("You got matched with: " + matched_name)
	else:
		print("Not a person in the system!\nDo you want to add a new one?")
		do_you_want_a_new_human = raw_input('Y/N: ')
		if do_you_want_a_new_human == 'Y':
			add_new_user()
		else:
			print("No new name added. Bye!")

def add_new_user():
	new_human = raw_input("Enter new persons name: ")
	f = open("app/data/humans.txt", "a")
	f.write(new_human+",")
	f.close()
	print(new_human + " added to database.")
	start_again = raw_input("Do you want to start over? Y/N:")
	if start_again == 'Y':
		do_the_work(people)
	else:
		print("Bye!")

def do_the_work(p):
	shuffle(p)
	#pairs = open("app/data/pairings.csv", "w") //will write the sorted pairs to CSV for parity checking
	people.append(p[0])
	dict = {}
	for i in range(len(p) - 1):
		dict.update({p[i]:p[i+1]})
		#pairs.write(p[i] + "," + p[i + 1] + "\n") //write the pairs
	who_are_you(dict) #pass array to function

text_file = open("app/data/humans.txt", "r") #TODO: use database & input from UI
people = text_file.read().split(',')
text_file.close()
do_the_work(people)
