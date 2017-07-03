def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    i=1
    diff=k
    done=False
    while not done:
        diff=diff-i
        if diff==0:
            done=True
            return True
        elif diff<0:
            done=True
            return False
        else:
            i+=1
print("Enter an integer to test.")
r=input()
print(is_triangular(int(r)))
