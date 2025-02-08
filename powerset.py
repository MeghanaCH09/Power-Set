def powerset(set, setsize):
    power_set_size=2**setsize
    outer=0
    inner=0
    for outer in range(0, power_set_size):
        for inner in range(0, setsize):
            if(outer & (1<<(inner))>0):
                print(set[inner], end="")
        print()

size=int(input("Enter the array size:"))
set=[]
for i in range(0, size):
    n=int(input("Enter data: "))
    set.append(n)
print(powerset(set,len(set)))