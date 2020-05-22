''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
#Submitted by thr3sh0ld
def main():
    import math
    x = int(input())
    res, count, res1, count1 = 0,0,0,0
    arr = [int(i) for i in input().split()]
    for i in range(len(arr)):
        if arr[i]%2 == 0:
            res += arr[i]
            count+=1
        else:
            res1 += arr[i]
            count1+=1
    if res>0:
        avg_eve = math.ceil(res/count)
    else:
        avg_eve=0
    if res1>0:
        avg_odd = math.ceil(res1/count1 )
    else:
        avg_odd = 0
    print(avg_odd+avg_eve,end='')
main()
