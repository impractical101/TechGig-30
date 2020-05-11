#submitted by thr3sh0ld 
#although this code giving not a 100 score so i tried using C which is commented below 
def m_input():
    row, col = map(int,input().split())
    arr=[]
    for i in range(row):
        arr.append(list(map(int, input().split())))
    return arr

def main():
    m1 = m_input()
    m2 = m_input()
    m3 =[]
    for i in range(len(m1)):
        l =[] 
        for j in range(len(m1[0])):
            l.append(m1[i][j] + m2[i][j])
        m3.append(l)
    for i in range(len(m3)):
        for j in range(len(m3)):
            if i==j==len(m3)-1:
                print(m3[i][j],end='')
                break
            if j!=len(m3)-1:
                print(m3[i][j],end=' ')
            elif j==len(m3)-1:
                print(m3[i][j])     
        
main()


"""
#include<stdio.h>
int main()
{
  int m1[10][10], m2[10][10], mc[10][10], a, b;
  scanf("%d%d", & a, & b);
  for (int i = 0; i < a; i++)

  {

    for (int j = 0; j < b; j++)

    {

      scanf("%d", & m1[i][j]);

    }

  }

  scanf("%d%d", & a, & b);

  for (int i = 0; i < a; i++)

  {

    for (int j = 0; j < b; j++)

    {

      scanf("%d", & m2[i][j]);

    }

  }

  for (int i = 0; i < a; i++)

  {

    for (int j = 0; j < b; j++)

    {

      mc[i][j] = m1[i][j] + m2[i][j];

    }

  }

  for (int i = 0; i < a; i++)

  {

    for (int j = 0; j < b; j++)

    {

      printf("%d", mc[i][j]);

      if (j != (b - 1)) 

        printf(" "); 

    }

    if (i != (a - 1)) 

      printf("\n"); 

  }

}
"""
