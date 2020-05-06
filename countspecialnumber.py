''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    def prime(num):
        if num > 1:
            for i in range(2,num):
                if((num % i) == 0):
                    return 0
                    break
            else:
                return 1
    count = 0
    x = int(input())
    y = int(input())
    for i in range(x,y):
        if(prime(i)):
            count +=1
    print(count, end ='')


main()


