def default():
    print('Hello World')

def dog():
    print('Woof!')

def main():
    if argv[1] == dog:
	dog()
    else: 
	default()

if __name__ == '__main__':
	main()
