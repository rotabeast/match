from random import *
import csv#the user database

def who_are_you(dict):#define the function and pass array from dictionary into it
	human = raw_input('Who are you?\n')#ask the user who they are
	if human in dict.viewvalues():#If person is already a user
		matched_name = (dict[human])#call out a person from the array
		print("You got matched with: " + matched_name)#and concatenate that to the string
	else:
		print("Not a person in the system!\nDo you want to add a new one?")#if not in the list, ask them to create themselves as a user
		do_you_want_a_new_human = raw_input('Y/N: ')
		if do_you_want_a_new_human == 'Y':
			add_new_user()#If Yes, create a new user
		else:
			print("No new name added. Bye!")#If no, shut down

def add_new_user():
	new_human = raw_input("Enter new persons name: ")#Pass the name that is entered into the variable new_human
	f = open("app/data/humans.txt", "a")#open the database file and store it in the variable f
	f.write(new_human+",")#add the person to the database
	f.close()#close the file/variable
	print(new_human + " added to database.")#Print that a new human was added to the database
	start_again = raw_input("Do you want to start over? Y/N:")#Re-start the process
	if start_again == 'Y':
		do_the_work(people)#If yes, go to do_the_work
	else:
		print("Bye!")#If no, print Bye!

def do_the_work(p):
	shuffle(p)#Take in the variable p, and shuffle it's contents
	#pairs = open("app/data/pairings.csv", "w") //will write the sorted pairs to CSV for parity checking
	people.append(p[0])#append the results to people
	dict = {}#dict is declared
	for i in range(len(p) - 1):#iterate through the amount of people less 1
		dict.update({p[i]:p[i+1]})#update the dictionary with the new values/users
		#pairs.write(p[i] + "," + p[i + 1] + "\n") //write the pairs
	who_are_you(dict) #pass array to function

text_file = open("app/data/humans.txt", "r") #TODO: use database & input from UI
people = text_file.read().split(',')#read the file and take a comma as being the separation value
text_file.close()#close the file
do_the_work(people)#tell python where to start from
