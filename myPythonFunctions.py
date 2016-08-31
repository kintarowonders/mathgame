import random
import os
import sys

def getUserPoint(userName):
	try:
		f = open("userScores.txt",'r')
	except IOError:
		f = open("userScores.txt",'w')
		f.close()
		f = open("userScores.txt",'r')
	found = 0
	for line in f:
		content = line.split(',')
		if (content[0] == userName):
			print ("Welcome back", userName)
			found = 1
			f.close()
			return int(content[1])
	if (found == 0):
		return -1

def updateUserPoints(newUser, userName, score):
	tmp = open("userScores.tmp",'w')
	f = open("userScores.txt",'r')

	for line in f:
		content = line.split(',')
		currentUser = content[0]
		newScore = content[1]
		if (newUser ==  False):
			if (currentUser == userName):
				newScore = score
		entry = userName + "," + str(newScore) + "\n"
		tmp.write(entry)

	if (newUser == True):
		entry = userName + "," + str(score) + "\n"
		tmp.write(entry)
	f.close()
	tmp.close()
	os.remove('userScores.txt')
	os.rename('userScores.tmp', 'userScores.txt')	

def generateQuestion():
	operatorDict = {1: '+', 2: '-', 3: '*', 4: '/', 5: '**'}
	operandList = []
	operatorList = []
	for index in range(5):
		operandList.append(random.randint(1, 10))
	exponent = 0
	for index in range(5):
		if (exponent==0):		
			operator = random.randint(1,5)
		else:
			operator = random.randint(1,4)
		if (operator == 5):
			exponent=1
		operatorList.append(operatorDict[operator])
	
	questionString = ""
	i = 0
	for operand in operandList:
		if (i == 4):
			questionString = questionString + str(operand)
		else:
			questionString = questionString + str(operand) + operatorList[i]
		i = i + 1
	if (eval(questionString) > 50000):
		questionString = generateQuestion() #yay recursion
	if (eval(questionString) < 0):
		questionString = generateQuestion() #yay recursion
	return questionString

def questionEval(questionString, userAnswer):
	if (round(eval(questionString)) == round(userAnswer)):
		return 1;
	else:
		return 0;

def askQuestion(questionString):
	questionStringBefore = questionString
	questionString = questionString.replace("**", "^")
	question = "Solve this problem, or type exit or skip: " + questionString + " = "
	try:
		theInput = input(question)
		answer = int(theInput)
	except ValueError:
		if (theInput == "exit"):
			sys.exit()
		if (theInput == "skip"):
			return -2
		print ("You didn't enter a number.")
		return -1
	if (questionEval(questionStringBefore, answer) == 1):
		print ("Correct")
		return 1
	else:
		print ("Incorrect")
		return 0
