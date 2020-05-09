''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    l =[]
    x =int(input())
    arr = list(map(int, input().split()))
    num = arr.index(max(arr))
    print(arr[num-1],end='')

 # Write code here 

main()


