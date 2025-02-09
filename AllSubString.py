import math

def powrset(set,setsize):
    powersetsize=(int) (math.pow(2,setsize))
    count=0
    j=0
    
    for count in range(1, powersetsize):
        for j in range(1,setsize):
            if(count &(1<<j)):
                print(set[j], end="")
        print("")

power=input("Enter string: ")
print(powrset(power,len(power)))