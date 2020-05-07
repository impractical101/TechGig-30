''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    num = int(input())
    cpy = num
    arr=[]
    sum = 0
    while int(num) > 0:
        arr.append(int(num % 10))
        num/=10
    for i in range(len(arr)):
        sum += pow(arr[i],3)
    if sum == cpy:
        print('True')
    else:
        print('False')

main()


