import argparse
import math
#take space arguments
delim=","

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
parser.add_argument("--checkprime",help="takes integer as value and prints “Yes” or “No” depending on whether the value is prime or not respectively",required=False)
parser.add_argument("--range",help="takes two more integer values named “​lower_bound​” and “​upper_bound​” and prints total number of primes between lower_bound ​and​ upper_bound ​(both inclusive)",required=False)
print(parser)
args=parser.parse_args()
print(args)
try:
    if args.checkprime:
        number=int(args.checkprime)
        if 1<=number<=1000:
            if args.range:
                print(prime(number),end=" ")
            else:
                print(prime(number))
        else:
            raise ValueError("Error : Please enter a value between 1 and 1000 only")


    if args.range:
        bounds=args.range.split(delim)
        bound1=int(bounds[0])
        bound2=int(bounds[1])
        if 1 <=bound1  <= 1000 and 1 <=bound2 <= 1000:
            print(prime2(bound1,bound2))
        else:
            raise ValueError("Error : Please enter a value between 1 and 1000 only")


    if not (args.checkprime or args.range):
        raise ValueError("Error : At least one of the following arguments are required: --check_prime, --range")

except ValueError as ve:
    print(ve)





