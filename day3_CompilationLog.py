''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    x = float(input())
    y = int(input())
    z = int(input())
    res = (x*y*z)//100
    res = int(res)
    print(res, end = '')
main()

