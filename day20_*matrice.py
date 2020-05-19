''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
#Submitted by thr3sh0ld
#For printing matrices error follow the below method
def main():
    for i in range(5):
        for j in range(5):
            if i!=j and j==4:
                print('*')
            elif i==4 and j==4:
                print('*',end='')
            else:
                print('*',end=' ')

main()

