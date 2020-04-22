from almubots_comm import Comm
import math

def dist(myBot, enBot):
	X = myBot['x'] - enBot['x']
	Y = myBot['y'] - enBot['y']
	return math.sqrt(X*X + Y*Y)

def rotateBot(myBot, closeBot, mainBot):
	X = closeBot['x'] - myBot['x']
	Y = closeBot['y'] - myBot['y']
	vx = closeBot['vx']
	vy = closeBot['vy']
	ang = myBot['angle']

	A = 0 # angle to enemy
	if X!=0: A = math.atan(Y/X)*180/math.pi
	if X<0: A+=180
	A -= ang
	A //=1
	A %= 360
	if A % 10 !=5:

		A = round(A/10,0)
		A %= 36

		if A>18: comm.rotate(-(36-A))
		else: comm.rotate(A)

		if myBot['ammo']<5:
		  if closeBot == mainBot: comm.shoot(1)
		else: comm.shoot(1)

def sgn(val):
	if val > 0:
		return 1
	if val < 0:
		return -1
	return 0


if __name__ == '__main__':
	botNum = 2
	comm = Comm(botNum)

	status = comm.send()
	newX = 0
	while True:
		newX += 1
		if newX == 360: newX = 0
		sinX = sgn(math.sin(newX))
		bots = status['bots']

        # my bot
		myBot = bots[botNum]
		myX = myBot['x']
		myY = myBot['y']

		#enemies
		curBot = {
			'id' : 0,
			'x' : 0,
			'y' : 0,
			'vx' : 0,
			'vy' : 0,
			'angle' : 0,
			'ammo' : 0,
			'life' : 100,
			'shoot' : False,
			'score' : 0
		}
		mainBot = curBot # lowest hp bot
		botID = 0         # lowest hp bot id
		curID = -1
		for bot in bots:
			curID += 1
			if bot == myBot:
				continue
			enemyHP = bot['life']
			if enemyHP < mainBot['life'] and enemyHP > 0:
				 mainBot = bot
				 botID = curID
			if enemyHP == mainBot['life'] and enemyHP > 0:
				if dist(myBot, bot) < dist(myBot, mainBot) and enemyHP > 0:
					mainBot = bot
					botID = curID

		closeBot = mainBot # closest bot
		closeID = 0        # closest bot id
		curID = -1
		for bot in bots:
			curID += 1
			enemyHP = bot['life']
			if bot == myBot:
				continue
			if dist(myBot, bot) < dist(myBot, closeBot) and enemyHP > 0:
				closeBot = bot
				closeID = curID

		# move to enemy
		if dist(myBot,closeBot)>150:
			comm.move(sgn(mainBot['x']-myX),sgn(mainBot['y']-myY))
		else:
			comm.move(-sgn(mainBot['x']-myX),-sgn(mainBot['y']-myY))
		if dist(myBot,mainBot)<300 and mainBot['life']>0:
			closeBot = mainBot

		rotateBot(myBot, closeBot, mainBot) # rotate rifle


		status = comm.send()

