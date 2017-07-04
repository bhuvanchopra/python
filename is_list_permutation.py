def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    L3=[]
    L4=[]
    L5=[]
    L6=[]
    for l1 in L1:
        if l1 not in L3:
            L3.append(l1)
    for l2 in L2:
        if l2 not in L4:
            L4.append(l2)
    for l3 in L3:
        count=0
        for l1 in L1:
            if l1==l3:
                count+=1
        L5.append(count)
    for l4 in L4:
        count=0
        for l2 in L2:
            if l2==l4:
                count+=1
        L6.append(count)
    if L1==[] and L2==[]:
        return (None,None,None)
    elif len(L1)==len(L2) and sorted(L5)==sorted(L6) and len(L3)==len(L4) and L3[L5.index(max(L5))]==L4[L6.index(max(L6))]:
        return (L3[L5.index(max(L5))],L5[L5.index(max(L5))],type(L3[L5.index(max(L5))]))
    else:
        return False

L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']
print(is_list_permutation(L1,L2))
