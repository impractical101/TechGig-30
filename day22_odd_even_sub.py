''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
#Submitted by thr3sh0ld
def main():
    x= int(input())
    res, res1 = 0, 0
    arr = [int(i) for i in input().split()]
    for j in range(len(arr)):
        if j%2 ==0:
            res+=arr[j]
        else: res1+=arr[j]
    if(res1>res):
        print(res1-res,end='')
    else:
        print(res-res1,end='')
 # Write code here 

main()

