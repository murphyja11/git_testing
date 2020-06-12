def default():
    print('Hello World')

def cat():
    print('Meow!')

def main():
    if argv[1] == cat:
	cat()
    else:
	default()

if __name__ == '__main__':
	main()
