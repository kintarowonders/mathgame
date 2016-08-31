import myPythonFunctions

name = input("Enter your name: ")
score = myPythonFunctions.getUserPoint(name)
newUser = 0
if (score == -1):
	print("Welcome to your first game.")
	score=0
	newUser = 1

redo = False
while(True):
	if (redo == False):
		questionString = myPythonFunctions.generateQuestion()
	redo = False
	returned = myPythonFunctions.askQuestion(questionString)
	if (returned == 1):
		score = score + 1
		myPythonFunctions.updateUserPoints(newUser, name, score)
		if (newUser == 1):
			newUser = 0
	if (returned == -1): #This runs if the input isn't an integer
		redo = True
