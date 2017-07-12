def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    L1=[]
    L2=[]
    L3=[]
    L4=[]
    for key in d.keys():
        L1.append(d[key])
    for l1 in L1:
        if l1 not in L2:
            L2.append(l1)
    for l2 in L2:
        for key in d.keys():
            if d[key]==l2:
                L3.append(key)

        L4.append(sorted(L3))
        L3=[]
    dictionary=dict(zip(L2,L4))
    return dictionary

e = {1:10, 2:20, 3:30, 4:30}
print(dict_invert(e))
