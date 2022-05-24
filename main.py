
def remove_duplicates_from_array(array):
	array_ = []
	n_ = ""
	for n in array:
		if n not in array_:
			for i in n:
				if i != " ":
					n_ += i
			array_.append(n_)
			n_ = ""
			
	return array_

def remove_diacritics(name):
	name_ = ""
	name__ =""
	update = {"ď":"d","č": "c", "š": "s", "ž": "z", "ý":"y" , "á": "a" , "í" : "i" , "é" : "e" , "ú" : "u" , "ä" : "a" , "ô" :"o" , "Č": "C", "Š": "S", "Ž": "Z", "Ý": "Y" , "Á": "A" , "Í" : "I" , "É" : "E" , "Ú" : "U" , "Ä" : "A" , "Ô" :"O" , "Ď" : "D"}
	for n in name:
		if n in update:
			name_ += update[n]
		else:
			name_ += n
	name__ = name_.upper()
	return name_ , name__

def add_diacritics(name):
	name_ = ""
	possibly = []
	c = 0
	update = {"d":"ď" , "c": "č" , "s": "š" , "z": "ž" , "y":"ý" , "a": "ä" , "i" : "í" , "e" : "é" , "u" : "ú" , "a" : "á" , "o" :"ô" , "C": "Č", "S": "Š", "Z": "Ž", "Y": "Ý" , "A": "Á" , "I" : "Í" , "E" : "É" , "U" : "Ú" , "A" : "Ä" , "O" :"Ô" , "D" : "Ď"}

	while c < len(name):
		for n in range(0,c):
			try:
				if name[n] != " ":
					name_ += update[name[n]]
					update.pop(name[n])
			except:
				if name[n] != " ":
					name_ += name[n]
		for n in range(c,len(name)):
			name_ += name[n]
		c += 1
		if len(possibly) == 0:
			possibly.append(name_)
		for r in possibly:
			if name_ in possibly:
				break
			elif name_ != name:
				possibly.append(name_)
				possibly.append(name_.upper())
		name_ = ""
	possibly.pop(0)
	return possibly

def add_diacritics_reversed(name):
	name_ = ""
	possibly = []
	c = 0
	update = {"d":"ď" , "c": "č" , "s": "š" , "z": "ž" , "y":"ý" , "a": "ä" , "i" : "í" , "e" : "é" , "u" : "ú" , "a" : "á" , "o" :"ô" , "C": "Č", "S": "Š", "Z": "Ž", "Y": "Ý" , "A": "Á" , "I" : "Í" , "E" : "É" , "U" : "Ú" , "A" : "Ä" , "O" :"Ô" , "D" : "Ď"}
	name = name[::-1]
	while c < len(name):
		for n in range(0,c):
			try:
				if name[n] != " ":
					name_ += update[name[n]]
					update.pop(name[n])
			except:
				if name[n] != " ":
					name_ += name[n]
		for n in range(c,len(name)):
			name_ += name[n]
		c += 1
		if len(possibly) == 0:
			possibly.append(name_)
		for r in possibly:
			if name_[::-1] in possibly:
				break
			elif name_ != name:
				possibly.append(name_[::-1])
				possibly.append(name_[::-1].upper())
		name_ = ""
	possibly.pop(0)
	return possibly
def name_input():
	name = input("What is your name? ")
	name = name.lower()
	name_ = ""
	name_Upper = name.upper()
	c = 0
	for n in name:
		if n != " ":
			if c == 0:
				name_ += n.upper()
				c += 1
			else:
				name_ += n
	name_1  , name_2 = remove_diacritics(name_)
	name_3 = add_diacritics(name)
	array = []
	result = []
	for n in name_3:
		previous = []
		if previous != add_diacritics(n):
			array .append(add_diacritics(n))
			previous = add_diacritics(n)
	name_4 = add_diacritics_reversed(name)
	for n in name_4:
		previous = []
		if previous != add_diacritics_reversed(n):
			array .append(add_diacritics_reversed(n))
			previous = add_diacritics_reversed(n)
	result.append(name_)
	result.append(name_Upper)
	result.append(name_1)
	result.append(name_2)
	for n in name_3:
		result.append(n)
	for n in name_4:
		result.append(n)
	for n in array:
		for r in n:
			result.append(r)
	result = remove_duplicates_from_array(result)
	for n in result:
		p =  add_diacritics_reversed(n)
		p2 = add_diacritics(n)
		for r in p:
			result.append(r)
		for r in p2:
			result.append(r)
	return remove_duplicates_from_array(result)


print(name_input())
print(name_input())
print(name_input())