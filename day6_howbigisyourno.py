''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    count =0 
    input1 = int(input())
    while(input1 != 0):
        input1 = round(input1 /10)
        count += 1
    print(count, end = '')
    
    

main()


