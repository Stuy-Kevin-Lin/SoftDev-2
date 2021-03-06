import random

def makeMemo(f):
    results = {}
    def inner(*argv): #Allows for makeMemo to be used on functions with more than one argument
        if argv not in results: #Stores output if it doesn't exist
            results[argv] = f(*argv)
        return results[argv] #Return output
    return inner

@makeMemo
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def make_HTML_heading(f):
	txt = f()
	def inner():
		return '<h1>' + txt + '</h1>'
	return inner

@make_HTML_heading
def greet():
	greetings = ['Hello', 'Welcome', 'AYO!', 'Hola', 'Bonjour', 'Word up']
	return random.choice(greetings)

print(greet())
print(fib(32))
