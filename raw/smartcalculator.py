# responses that calculator will give 
response=['Welcome to smart calculator','My name is Cavill', 
		'I am glad that I was able to help you','Sorry ,this is beyond my ability'] 

# fetching tokens from the text command 
def operations_from_text(text): 
	l=[] 
	for t in text.split(' '): 
		try: 
			l.append(float(t)) 
		except ValueError: 
			pass
	return l 

# calculating LCM 
def lcm(a,b): 
	L=a if a>b else b 
	while L<=a*b: 
		if L%a==0 and L%b==0: 
			return L 
		L+=1

# calculating HCF 
def hcf(a,b): 
	H=a if a<b else b 
	while H>=1: 
		if a%H==0 and b%H==0: 
			return H 
		H-=1

# Addition 
def add(a,b): 
	return a+b 

# Subtraction 
def sub(a,b): 
	return a-b 

# Multiplication 
def mul(a,b): 
	return a*b 

# Division 
def div(a,b): 
	return a/b 

# Remainder 
def mod(a,b): 
	return a%b 

# Response to command 
# printing - "I am glad that I was able to help you" on exit 
def end(): 
	print(response[2]) 
	input('press enter key to exit. ') 
	exit() 

def myname(): 
	print(response[1]) 
def sorry(): 
	print(response[3]) 

# Operations - performed on the basis of text tokens 
operations={'ADD':add,
            'PLUS':add,
            'SUM':add,
            'ADDITION':add, 
			'SUB':sub,
            'SUBTRACT':sub, 
            'MINUS':sub, 
			'DIFFERENCE':sub,
            'LCM':lcm,
            'HCF':hcf, 
			'PRODUCT':mul, 
            'MULTIPLY':mul,
            'MULTIPLICATION':mul, 
			'DIVISION':div,
			'DIVIDE':div,
            'MOD':mod,
            'REMANDER':mod,
            'MODULAS':mod} 
##operations1={'add':['ADD','PLUS','SUM','ADDITION'],

# commands 
commands={'NAME':myname,'EXIT':end,'END':end,'CLOSE':end} 
		
print('--------------'+response[0]+'------------') 
print('--------------'+response[1]+'--------------------') 


while True: 
	print() 
	text=input('enter your queries: ') 
	for word in text.split(' '): 
		if word.upper() in operations.keys(): 
			try: 
				l = operations_from_text(text) 
				q = str(operations[word.upper()].__name__)
				if q == 'add':
					r=0
					for i in range(len(l)):
						r = operations[word.upper()] (r,l[i]) 
					print(r) 
				elif q == 'sub':
					r=float(l[0])
					for i in range(1,len(l)):
						r = operations[word.upper()] (r,l[i])
					print(r)
				elif q == 'mul':
					r=1
					for i in range(len(l)):
						r = operations[word.upper()] (r,l[i]) 
					print(r)
				elif q == 'div':
					r=float(l[0])
					for i in range(1,len(l)):
						r = operations[word.upper()] (r,l[i])
					print(r)
				
			except: 
				print('something went wrong going back please enter again !!') 
			finally: 
					break
		elif word.upper() in commands.keys(): 
					commands[word.upper()]() 
					break
	else:		 
		sorry() 
