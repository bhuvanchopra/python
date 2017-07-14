def general_poly (L):
    """
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0
    """
    def f(x):
        """
        f is a function that returns a value that is formed by multiplying with
        the numbers obtained from general_poly function with a base value x.
        """
        result=0
        q=len(L)
        for l in L:
            result+=l*x**(q-1)
            q-=1
        return print(result)
    return f
general_poly([1, 2, 3, 4])(10)
