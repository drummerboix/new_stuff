import sys

def cat():
	print('MEOW!')

def default():
	print('Hello world')

def dog():
	print('WOOF!')

def main():
	if sys.argv[1] == 'cat':
		cat()
	elif sys.argv[1] == 'dog':
		dog()
	else:
		default()

if __name__ == '__main__':
	main()
