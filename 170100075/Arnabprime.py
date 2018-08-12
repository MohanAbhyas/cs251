import argparse
import math
#take space arguments
delim=" "

def prime(number):
    if number==1:
        return "No"
    i=2
    while (i <= number**(0.5)) :
        if (number%i==0):
            return "No"
        i=i+1
    return "Yes"

def prime2(lower,upper):
    i=lower
    c=0
    while i <= upper:
        if prime(i)=="Yes":
            c=c+1
        i=i+1
    return str(c)

parser=argparse.ArgumentParser()
parser.add_argument("--check_prime",help="takes integer as value and prints “Yes” or “No” depending on whether the value is prime or not respectively",required=False)
parser.add_argument("--range",help="takes two more integer values named “​lower_bound​” and “​upper_bound​” and prints total number of primes between lower_bound ​and​ upper_bound ​(both inclusive)",nargs=2,required=False)
args=parser.parse_args()
flag1=0
flag2=0

try:
    if args.check_prime:
        number=int(args.check_prime)
        if 1<=number<=1000:
            flag1=flag1+1
            f=prime(number)
        else:
            raise ValueError("Error : Please enter a value between 1 and 1000 only")


    if args.range:
        bounds=args.range
        bound1=int(bounds[0])
        bound2=int(bounds[1])
        if 1 <=bound1  <= 1000 and 1 <=bound2 <= 1000:
            s=prime2(bound1,bound2)
            flag2=flag2+1
        else:
            raise ValueError("Error : Please enter a value between 1 and 1000 only")

    
    if flag1==1 and flag2==0:
        print (f)
    if flag1==0 and flag2==1:
        print (s)
    if flag1==1 and flag2==1:
        print (f+' '+s)

    if not (args.check_prime or args.range):
        raise ValueError("Error : At least one of the following arguments are required: --check_prime, --range")

except ValueError as ve:
    print(ve)

