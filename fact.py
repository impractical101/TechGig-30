''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    int1 = int(input())
    def fact(n):
        if n == 1:
            return n
        elif n < 1:
            return ("NA")
        else:
            return n*fact(n-1)
    print (fact(int(int1)), end ='')

main()
