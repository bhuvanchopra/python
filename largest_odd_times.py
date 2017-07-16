def largest_odd_times(L):
    """
    Assumes L is a non-empty list of ints
    Returns the largest element of L that occurs an odd number
    of times in L. If no such element exists, returns None
    """
    count=0
    L2=[]
    L3=[]
    for l in L:
        if l not in L2:
            L2.append(l)
    for l1 in L2:
        count1=0
        for l2 in L:
            if l1==l2:
                count1+=1
        L3.append(count1)
    for l4 in sorted(L2,reverse=True):
        if L3[L2.index(l4)]%2!=0:
            return (l4)

print("Enter the number of integers you want in your list.")
r=input()
L1=[]
for i in range(int(r)):
    print("Enter integer no.",i+1)
    r1=input()
    L1.append(int(r1))
largest_odd_times(L1)
