''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    import math
    x ,y = map(int, input().split())
    print(math.gcd(x,y),end ='')

 # Write code here 

main()


