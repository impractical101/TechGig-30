def main():
    str=input()
    if str.isalpha():
        print("This input is of type string.",end='')
    elif str.isnumeric():
        print("This input is of type Integer.",end='')
    elif str.rfind('.')!=-1: # -1 if substring not present
    #'. full stop ya float handling'
        try:
            str=float(str)
            print('This input is of type Float.',end='')
        except:
            print("This input is of type string.",end='')
    elif str[0]=='-':
        print("This input is of type Integer.",end='')
    else:
        print('This is something else.',end='')
main()
