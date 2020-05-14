from speak import male



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
	male('I am glad that I was able to help you')
	print(response[2])
	input('press enter key to exit.')
	male('press enter key to exit.')

	exit() 

def myname(): 
	
	print(response[1])
	male('My name is Cavill')
def sorry(): 
	
	print(response[3])
	male('Sorry ,this is beyond my ability')

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
			'DIVIDE':div,
			'DIVISION':div,
            'MOD':mod,
            'REMANDER':mod,
            'MODULAS':mod} 


# commands 
commands={'NAME':myname,'EXIT':end,'END':end,'CLOSE':end,'QUIT':end} 
		
print('--------------'+response[0]+'------------') 
male('Welcome to smart calculator')
print('--------------'+response[1]+'--------------------') 
male('My name is Cavill')


while True: 
	print('enter your queries: ')
	male('enter your queries:') 
	text=input()
	

	r=0
	for word in text.split(' '): 
		if word.upper() in operations.keys(): 
			try: 
				l = operations_from_text(text)
				q = str(operations[word.upper()].__name__)
				if q == 'mul':
					r=1
					for i in range(len(l)):
						r = operations[word.upper()] (r,l[i]) 
				elif q == 'add':
					for i in range(len(l)):
						r = operations[word.upper()] (r,l[i]) 
				elif q == 'div' or 'lcm' or 'hcf' or 'sub':	
					r=float(l[0])
					for i in range(1,len(l)):
						r = operations[word.upper()] (r,l[i])
				elif q == 'mod':
					r = operations[word.upper()] (l[0],l[1])
				print(r)
				
				male(r)						
				 
				r=0
			except: 
				print('something went wrong going please enter again !!') 
				male('something went wrong going please enter again !!')
			finally: 
					break
		elif word.upper() in commands.keys(): 
					commands[word.upper()]() 
					break
	else:		 
		sorry() 
