''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    arr =[]
    maxi = 0
    row, column = map(int,input().split())
    for i in range(row):
        arr = list(map(int,input().split()))
        if sum(arr)>maxi:
            maxi = sum(arr)
            row = i+1
    print("Row",row, end='')
    
 # Write code here 

main()

