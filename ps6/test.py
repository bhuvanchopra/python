import string
def build_d(shiftt):
    dic={}
    for i in range(26):
        if (i+shiftt)>=26:
            dic[string.ascii_lowercase[i]]=string.ascii_lowercase[(i+shiftt)-26]
        else:
            dic[string.ascii_lowercase[i]]=string.ascii_lowercase[(i+shiftt)]
    for j in range(26):
        if (j+shiftt)>=26:
            dic[string.ascii_uppercase[j]]=string.ascii_uppercase[(j+shiftt)-26]
    return dic
print(build_d(4))
