''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
#submitted by thr3sh0ld
def main():
    x =int(input())
    res, res1= 0,0
    arr = map(int,input().split())
    for i in arr: 
        if i%2:
            res+=i
        else:
            res1+=i
    print(res*res1,end='')

 # Write code here 

main()

