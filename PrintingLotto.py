#All right reserved by Taehwan Kim and FOX
import random
import time,sched
import sys
from Error import *


def making_list(length=45): # to make integer list
	lst = []

	for num in range(1,length+1):
		lst.append(num)

	return lst

def auto_select(): # to choose automatic numbers
	numbers = random.sample(making_list(45),6)
	print "Your numbers:",sorted(numbers)
	return numbers

def isUnique(lst): # to check unique list
	s1 = set(lst)

	if len(s1) < len(lst): 
	# if list has distinct number, 
	# length of it's set will be reduced.
		return False
	else:
		return True

def manual_select():
	try:
		numbers = raw_input("Please input your lucky six numbers ")	
		selection = [int(num) for num in numbers.split(' ')]

		for n in selection:
		 	if n < 1 or n > 45:
		 		raise OverRangeError()

		if len(selection) is not 6:
			raise NotSixError()
		elif not isUnique(selection):
			raise DistinctError()
			
		result = selection
	except ValueError:
		print("YOUR INPUT IS SOME WRONG")
		result = manual_select()
	except NotSixError:
		result = manual_select()
	except DistinctError:
		result = manual_select()
	except OverRangeError:
		result = manual_select()

	return result

def drawing():
	print "NOW DRAWING!!"
	lst = making_list()
	result = []
	ball = 0 # ball is exactly same as real lotto games.

	printPeriod(5)

	for i in range (0,7):
		ball = random.choice(lst) 
		result.append(ball)
		lst.remove(ball) # to remove distinct drawing result

	return result

def printPeriod(num=10):
	period = "."

	while num > 0:
		period += "."
		num-=1

	print period

def printDrawing(lst,i=0):
	s = sched.scheduler(time.time, time.sleep)

	if i==len(lst):
		print "FINISHED"
	else:
		if i==len(lst)-1:
			print "BOUNUS NUMBER is {0}".format(lst[i])
		else:	
			print "NUMBER {0} is {1}".format(i+1,lst[i])
			s.enter(1,0,printPeriod,())
			s.run()

		printDrawing(lst,i+1)

def checking(player,result):
	setPlayer =  set(player)
	setResult =  set(result)
	interSection = setPlayer & setResult
	length = len(interSection)

	if length == 6:
		print "1st : p=1/8,145,060"
	elif length == 5 and result[6] in interSection:
		print "2nd : p=1/1,357,510"
	elif length == 5:
		print "3rd : p=1/35,724"
	elif length == 4:
		print "4th : p=1/733 50,000won"
	elif length == 3:
		print "5th : p=1/45 5000won"
	else:
		print "Failed..."

	print "You matched {0} numbers.".format(length)

def main():
	print "Welcome to FOXLotto"
	player = []

	try:
		size = input("How many lotto want you buy?... ")
	except:
		print "You inputed string or not declared variables."
		print "Buy lotto one paper automatically..."
		size = 1

	while size > 0:
		mode = raw_input("Do you want automatic select? (y or n) ")

		if mode.upper() == "Y":
			player.append(auto_select())
		elif mode.upper() == "N":
			player.append(manual_select())
		else:
			print "You inputed wrong and just do auto_selection"
			printPeriod(15)

		size-=1

	result = drawing()
	printDrawing(result)

	for numbers in player:
		checking(numbers,result)
		print "Your numbers:",sorted(numbers)
		print "Result:",sorted(result)

if __name__ == "__main__":
	main()