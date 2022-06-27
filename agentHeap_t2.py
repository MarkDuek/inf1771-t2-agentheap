import numpy as np 
import time
import pandas

class AgentHeap:

	def __init__(self, file):
		self.index = 1
		self.file = file
		self.arr = self.readFile()

	def outOfIndex(self):
		try:
			self.arr[self.index]
			# print(self.index, "==> NO IndexError")
			return False
		except IndexError:
			# print(self.index, "==> IndexError")
			return True

	def indexValid(self):
		if self.outOfIndex() or self.arr[self.index] == ["-", "-"]:
			# print(self.index, self.arr[self.index], "==> Invalid Index")
			return False
		else:
			# print(self.index, self.arr[self.index], "==> Valid Index")
			return True
		return

	def populateNone(self):
		# print("populate", self.index, self.arr)
		for i in range(0, (len(self.arr)*2-len(self.arr))):
			self.arr.append(["-", "-"])


	def writeFile(self):
		fileObj = open(self.file, "w")
		for line in self.arr:
			fileObj.write(line[0])
			fileObj.write(",")
			fileObj.write(line[1])
			fileObj.write('\n')
		return

	def readFile(self):
		print(self.file)
		fileObj = open(self.file, "r")
		fileArr = []
		for line in fileObj.readlines():
			fileArr.append(line.strip().split(","))
			fileObj.close()
		return fileArr

	def insertAQ(self, a, q):
		if self.outOfIndex():
			self.populateNone()
		self.arr[self.index][0] = q
		self.arr[self.index][1] = "q"

		self.index = self.index*2
		if self.outOfIndex():
			self.populateNone()		
		self.arr[self.index][0] = a
		self.arr[self.index][1] = "a"


def validAnswer(inp):
	if inp != "n" and inp != "y":
		print("É 'y'(YES) or 'n'(NO) cara...")
		return False
	return True

def introGame():
	print("\nolá.")
	time.sleep(2)
	print("vamos jogar um jogo...")
	time.sleep(2)
	print("pense em um animal.")
	time.sleep(1)

def outroGame():
	time.sleep(1)
	print(":D")
	time.sleep(1)
	print("obrigado por jogar!!\n")
	time.sleep(1)	

def newAnswer():
	print("\n.")
	time.sleep(0.5)
	print(".")
	time.sleep(0.5)
	print(".")
	time.sleep(0.5)
	print("que tal você me ensinar?")
	time.sleep(1)


def runGame(file):
	#introduce game
	introGame()

	#init agent with file
	agentHeap = AgentHeap(file)	

	#game cycle begins
	while True:
		# print("INDEX", agentHeap.index, agentHeap.arr)

		inp = input(agentHeap.arr[agentHeap.index][0]+" (y/n) :")
		
		#break
		if inp == "break":
			print(agentHeap.arr)
			break

		#verify input
		if not validAnswer(inp):
			continue 

		#yes or no cycle
		elif inp == "y":
			print("YES")
			if agentHeap.arr[agentHeap.index][1] == "a":
				time.sleep(1)
				print("\nacertei!")
				break

			else:
				agentHeap.index = agentHeap.index*2
				continue

		elif inp == "n":
			print("NO")
			agentHeap.index = agentHeap.index*2 + 1
			if agentHeap.indexValid():
				continue

			else:
				print("não tenho resposta... :(")
				newAnswer()
				inpA = input("em que animal voce pensou?")
				inpQ = input("que pergunta você faria para distingui-lo?")
				agentHeap.insertAQ(inpA, inpQ)
				agentHeap.writeFile()
				# print("WRITE", agentHeap.arr)
				break

	outroGame()
	return

def main():
	
	runGame("agent_0.1") 

	return 

if __name__ == "__main__":
    main()


