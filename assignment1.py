def addition(a,b):
	return a+b

def subtraction(a,b):
	return a-b;

def multiplication(a,b):
	return a*b;
        
def division(a,b):
        try:
                return a/b
        except ZeroDivisionError:
                return "Can't divide by zero";

if __name__ == "__main__":
	a = 3
	b = 5
	print(addition(a,b))
	print(subtraction(a,b))
	print(multiplication(a,b))
	print(division(a,b))

'''
clone from github
Create new branches for Multiplication and Division
merge with master
push to github 
'''
