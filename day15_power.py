''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
#submitted by thr3sh0ld 
def main():
    x,y = map(int, input().split())
    def powe(x,y):
        res = 0
        if y ==1:
            return x
        else:
            return x**y
        return res  
    res = powe(x,y)
    print(res,end='')

main()


