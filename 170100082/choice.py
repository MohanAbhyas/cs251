#! /usr/bin/python3
import random
import pickle
import sys

def fill_choice():
    a='ABCD'
    f=open('new_int.p','w+')
    f.close()

    with open('new_int.p','ab') as f:
        arbit=[]
        for i in range(1,5000):
            arbit.append(i)
        random.shuffle(arbit)
        arbit=arbit[:100]
        for i in range(0,100):
            if a[3]=='Z':
                a=a[:2]+chr(ord(a[2])+1)+'@'
            a=a[:3]+chr(ord(a[3])+1)
            rand=arbit[i]
            st=str(rand)+' '+a
            pickle.dump(st,f)

def throws():
    raise ValueError()
def ask_choice():
    file=sys.argv[1]
    try:
        open(file)
    except:
        print("file not found")
        exit(1)
    inp=int(input('Enter Number: '))
    while inp<5000 or inp>7000:
        try:
            throws()
            return 0
        except Exception:
            sys.stderr.write('ERROR: Input range is 5000-7000\n')
            inp=int(input('Enter Number: '))
    num=[]
    name=[]
    l=100
    with open(file,'rb') as f:
        for i in range(0,l):
            new = pickle.load(f)
            alist=[]
            for word in new.split(' '):
                alist.append(word)
            num.append(int(alist[0]))
            name.append(alist[1])

    flag_backup=0
    flag_real=0
    for i in range(0,l):
        for j in range(i+1,l):
            if flag_backup==0:
                if num[i]+num[j]<inp:
                    temp=name[j]+' '+str(num[j])+' '+name[i]+' '+str(num[i])
                    flag_backup=1

            if num[i]+num[j]==inp:
                print(name[j]+' '+str(num[j])+' '+name[i]+' '+str(num[i]))
                flag_real=1

            if flag_real == 1:
                break
        if flag_real == 1:
            break

    if flag_real==0:
        if flag_backup==1:
            print(temp)
        else:
            print("Not possible")
            
def main():
   # print(sys.argv)
    if len(sys.argv)==2:
        ask_choice()
    else:
        fill_choice()

if __name__ == "__main__":
    main()
