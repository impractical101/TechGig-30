''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    n = int(input())
    ar = list(map(int,input().split()))
    arr= sorted(ar)
    start = arr[0]
    for i in range(n):
        if start+i != arr[i]:
            print('False',end='')
            return 0
    print('True',end='')
        



 # Write code here 

main()