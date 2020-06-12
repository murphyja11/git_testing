def default():
    print('Hello World')

def main():
    if argv[1] == 'cat':
	cat()
    elif argv[1] == 'dog':
	dog()
    else:
	default()

def cat():
    print('Meow')

def dog():
    print('Woof!')

if __name__ == '__main__':
	main()
