''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
#Submitted by thr3sh0ld
def main():
    x = int(input())
    even,odd = 0,0
    while x > 0 :
        rem = x%10
        if rem%2 == 0:
            even += rem
        else:
            odd += rem
        x = int(x/10)
    print(int(abs(even-odd)),end='')
 # Write code here 

main()

