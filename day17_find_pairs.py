''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
def main():
    n = int(input())
    lis = list(map(int,input().split()))
    out  = int(input())
    flag=0
    for i in range(n-1):
        if out == lis[i]+lis[i+1]:
            flag = 1
    if flag == 1:
        print('True',end='')
    else:
        print('False',end='')
        
main()