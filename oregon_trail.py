from random import random, randint

class Inventory(object):	
	
	def __init__(self):
	
		# oxen, water, medicine, tools
		self.bag = [2, 2, 2, 2]
		self.total = 8
		
	def inven_check(self):
		
		print "Oxen: %d" % self.bag[0]
		print "Water: %d" % self.bag[1]
 		print "Medicine: %d" % self.bag[2]
		print "Tools: %d" % self.bag[3]
		
		if self.total == 0:
			return 'dead'
		
	def inven_change(self, increment):
		
		# which to change?
		choice = randint(0,3)
		while self.bag[choice] == 0:
			choice = randint(0,3)
		
		self.bag[choice] += increment
		self.total += increment
		
		for i in range(4):
			if self.bag[i] < 0:
				self.bag[i] = 0
			if self.total < 0:
				self.total = 0
				
	def is_dead(self):
		
		if self.total == 0:
			return True

class Area(object):
	
	def enter(self):
		print "Why are you here?"
		pass
		
	def roll_create(self):
		return randint(1,6)
	
		
class Death(object):

	deaths = {
	'dysentery':"You have died of dysentery!",
	'bite':"You have died of a rattlesnake bite!",
	'drown':"You have drowned.",
	'starve':"You have died of starvation."
	}
	
	death_names = ['dysentery','bite','drown','starve']
	
	def choose_death(self):
		
		num = randint(0,3)
		death_choice = self.death_names[num]
		return self.deaths.get(death_choice)
	
	
class Trail(Area):
	
	def enter(self):
		print "You are on the trail."
		
		roll_1 = self.roll_create()		
		roll_2 = self.roll_create()
		while (roll_1 == roll_2):
			roll_2 = self.roll_create()
		
		print "Roll the correct number to continue without losing resources."
		
		roll_match = int(raw_input("Choose a number to match the dice.\n> "))
		
		print "The dice showed %d and %d." % (roll_1,roll_2)
		
		if (roll_match == roll_1) or (roll_match == roll_2):
			print "You have rolled a %d. You are safe." % roll_match
			return "progress"
		else:
			print "Oh no! You rolled a %d. You have lost a resource." % roll_match
			return "failure"
			
			
	
class River(Area):
		
	def enter(self):
		print "You have reached a river." 
		
		roll_1 = 4
		roll_2 = 6
		
		print "Roll the correct number to continue without losing resources."
		
		roll_match = int(raw_input("Choose a number to match the dice.\n> "))
		
		print "The dice showed %d and %d." % (roll_1,roll_2)
		
		if (roll_match == roll_1) or (roll_match == roll_2):
			print "You have rolled a %d. You are safe." % roll_match
			return "progress"
		else:
			print "Oh no! You rolled a %d. You have lost a resource." % roll_match
			return "river"
			
		
class Town(Area):
	
	def enter(self):
		print "You have reached a town!"
		return "town"

class Fort(Area):
	
	def enter(self):
		print "You have entered a fort!"
		return "fort"
		
class Engine(object):
	
	areas = {
	'trail':Trail(),
	'river':River(),
	'town':Town(),
	'fort':Fort()
	}
	
	def __init__(self):
		self.start = 'trail'
		self.inventory = Inventory()
		self.death = Death()
		
	def next_scene(self,next):
		return self.areas.get(next)
		
	def assign_death(self, type):
		self.death_type = self.death.choose_death(type)	
		
	def choose_area(self):
		
		prob = random()
		
		if (prob >= 0) and (prob <= 0.45):
			return 'trail'
		elif (prob > 0.45) and (prob <= 0.75):
			return 'river'
		elif (prob > 0.75) and (prob <= 0.90):
			return 'town'
		elif (prob > 0.90) and (prob <= 1.00):
			return 'fort'
		else:
			print "Weary traveller, nowhere to go!"

			
	def play(self):
		current_area = self.next_scene(self.start)
		
		turns = 0
		
		while (turns < 50):
			print "\n\n",'*-'*20
			outcome = current_area.enter()
			
			if (outcome == "failure"):
				self.inventory.inven_change(-1)
				self.inventory.inven_check()
				
			elif (outcome == "river"):
				self.inventory.inven_change(-1)
				self.inventory.inven_check()
				next_area = self.choose_area()
				current_area = self.next_scene(next_area)
				turns += 1
				print "Trail Completed: %d/50" % turns
				
			elif (outcome == "town") or (outcome == "fort"):
				self.inventory.inven_change(2)
				self.inventory.inven_check()
				next_area = self.choose_area()
				current_area = self.next_scene(next_area)
				turns += 1
				print "Trail Completed: %d/50" % turns
				raw_input("Press enter to continue")
			
			elif (outcome == "progress"):
				next_area = self.choose_area()
				current_area = self.next_scene(next_area)
				self.inventory.inven_check()
				turns += 1
				print "Trail Completed: %d/50" % turns
				
			else:
				print "Godspeed traveller. You're stuck."
				
			if (self.inventory.is_dead()):
				print "\n\n"
				print self.death.choose_death()
				print "Game Over."
				exit(0)
				
		
game = Engine()
game.play()
