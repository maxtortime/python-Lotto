#All right reserved by Taehwan Kim and FOX
import random
import time,sched
import sys

MAXSIZE = 5
s = sched.scheduler(time.time, time.sleep)

class player():
	pass

class Error(Exception):
	pass

class NotSixError(Error):
	def __init__(self):
		print "NotSixError"
class DistinctError(Error):
	def __init__(self):
		print "You inputs distinct numbers"

def making_list(length=45): # to make integer list
	lst = []

	for num in range(1,length+1):
		lst.append(num)

	return lst

def auto_select(): # to choose automatic numbers
	return random.sample(making_list(45),6)

def isUnique(lst):
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

		if len(selection) is not 6:
			raise NotSixError()
		elif not isUnique(selection):
			raise DistinctError()
			
		result = selection
	except ValueError:
		print("Your input is wrong...")
		result = manual_select()
	except NotSixError:
		result = manual_select()
	except DistinctError:
		result = manual_select()

	return result

def drawing():
	lst = making_list()
	result = []
	ball = 0 # ball is exactly same as real lotto games.

	printPeriod(5)

	for i in range (0,7):
		ball = random.choice(lst) 
		result.append(ball)
		lst.remove(ball) # to remove distinct drawing result

	return result

def printPeriod(num = 5):
	period = "."

	while num > 0:
		period += "."
		num-=1

	print period

def printDrawing(i,lst):
    if i==len(lst):
        print "FINISHED"
        return lst
    else:
    	if i==len(lst)-1:
    		print "BOUNUS NUMBER is {0}".format(lst[i])
    	else:	
        	print "NUMBER {0} is {1}".format(i+1,lst[i])
        	s.enter(1,0,printPeriod,())
        	s.run()

        printDrawing(i+1,lst)

def checking(player,result):
	setPlayer =  set(player)
	setResult =  set(result)
	interSection = setPlayer & setResult

	if len(interSection) == 6:
		print "1st : p=1/8,145,060"
	elif len(interSection) == 5 and result[6] in interSection:
		print "2nd : p=1/1,357,510"
	elif len(interSection) == 5:
		print "3rd : p=1/35,724"
	elif len(interSection) == 4:
		print "4th : p=1/733 50,000won"
	elif len(interSection) == 3:
		print "5th : p=1/45 5000won"
	else:
		print "Failed..."

def main():
	player = []
	print "Welcome to FOXLotto"

	# try:
	# 	size = input("How many lotto want you buy?...(~5) ")
	# except:
	# 	print "You inputed string or not declared variables."
	# 	print "Buy lotto one paper automatically..."
	# 	size = 1

	mode = raw_input("Do you want automatic select? (y or n) ")

	if mode.upper() == "Y":
		player = auto_select()
	elif mode.upper() == "N":
		player = manual_select()
	else:
		print "You inputed wrong and just do auto_selection"
		printPeriod(15)

	print "NOW DRAWING!!"
	result = printDrawing(0,drawing())
	checking(player,result)

	print "Your numbers: ",sorted(player)
	print "Result : ",sorted(result)

main()