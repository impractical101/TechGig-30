''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
#Submitted by thr3sh0ld
def main():
    x = int(input())
    arr = [int(i) for i in input().split()]
    print(max(arr)*min(arr),end= '')

 # Write code here 

main()

