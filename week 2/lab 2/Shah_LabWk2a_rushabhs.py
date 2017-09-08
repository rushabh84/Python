import random

def write_numbers():
    # Get a random number.
    rangeN = int(input('What should the length of file be?: '))
    fileName = input('What should the name of the file be?')
    fileName = open(fileName+'.txt', 'w+')
    for i in range(rangeN):
        number = str(random.randint(1, 500))
        #print(number)
        fileName.write(number + "\n")
    fileName.close()


def read_numbers():
    try:
        fileName = input('What should the name of the file be?')
        num_sum = 0
        f = open(fileName+'.txt', 'r')
        for line in f:
            num_sum += int(line)
            print(int(line))
        print(num_sum)
    except:
        print('File not found')

def recasterisk(n):
    if n>1:
        recasterisk(n-1)
    print('*'*n)
    

def main():
    print('Now writes')
    write_numbers()
    print('Now reads')
    read_numbers()
    recasterisk(3)

main()
