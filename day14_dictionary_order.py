#submitted by thr3sh0ld
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    l = []
    end = int(input())
    for i in range(end):
        inp = str(input())
        l.append(inp)
    b_list = sorted(l, key=str.lower)
    
    for i in range(len(b_list)):
        if b_list[i]==b_list[-1]:
            print(b_list[i],end='')
        else:
            print(b_list[i])
    
        
main()
