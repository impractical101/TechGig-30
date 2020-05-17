''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
#submtted by thr3sh0ld
def main():
    x = int(input())
    stcount, lcount= 0, x-1
    inp = list(map(int,input().split()))
    idcase = sorted(inp)
    while inp[stcount] == idcase[stcount]:
        stcount += 1
    while inp[lcount] == idcase[lcount]:
        lcount -= 1
    for i in range(stcount,lcount+1):
        if i==lcount:
            print(inp[i],end='')
        else:
            print(inp[i], end= " ")

 # Write code here 

main()

