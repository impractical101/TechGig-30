''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    inp = int(input())
    temp = inp
    lst = []
    sum1 = 0
    while int(inp) > 0:
        lst.append(int(inp % 10))
        inp/=10
    n = len(lst)
    
    for i in range(n):
        sum1 += lst[i]**n
        
    if sum1 == temp:
        print('True',end='')
    else :
        print('False',end='')

main()
