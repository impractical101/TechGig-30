''' Read input from STDIN. Print your output to STDOUT '''
#Use input() to read input from STDIN and use print to write your output to STDOUT
# submitted by thr3sh0ld 
def main():
    import numpy as np 
    row, col = map(int,input().split())
    def m_input():
        arr=[]
        for i in range(row):
            arr.append(list(map(int, input().split())))
        return arr

    mat = m_input()
    rez = np.transpose(mat)
    #rez = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))] 
    for i in range(row):
        for j in range(col):
            print(rez[i][j],end = ' ')
        if i < row-1:
            print()
        else:break 
 # Write code here 

main()

