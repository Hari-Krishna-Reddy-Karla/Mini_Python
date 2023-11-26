'''
Traditional way to start to learn to program 
is to write a hello world program
'''


# print("Hello, World!")

def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()

