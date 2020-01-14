from termcolor import colored
import time

def print_layer(n,color):
    layer = '*'*n
    text = colored(layer, color)
    print(text.center(50))

def print_tree(n):
    for i in range(1,n*2,2):
        print_layer(i,'green')
    for j in range(3):
        print_layer(3,'magenta')

def main():
    while True:
        print_tree(10)
        for i in range(3):
            print_layer(40, 'white')
        time.sleep(1)


if __name__ == "__main__":
    main()