''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    string = input()
    lower,upper = 0,0
    
    for i in range(len(string)):
        if string[i].isupper() :
            upper += 1
        elif string[i].islower() :
            lower += 1
    print(upper,end='\n')
    print(lower,end='')
main()
