import random
inp = input("ENTER YOUR CHOISE ROCK(r) PAPER(p) SISCOR(s)\n")
cmp_inp = random.choice('rps')
print("computer choose:"+cmp_inp)
if(inp==cmp_inp):
	print("Tie")
elif(inp=='r'and cmp_inp=='p' or inp=='p' and cmp_inp=='s' or inp=='s' and cmp_inp=='r'):
	print("COMPUTER WINS")
else:
	print("USER WINS")
	
