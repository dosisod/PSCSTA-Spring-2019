from data_parser import parse
from string import ascii_letters as ascii

def getone(s):
    try:
        n=s.index("#")
        after=s[n+1:]
    except:
        return ""

    ret=""
    for i in after:
        if i in ascii:
            ret+=i
        else:
            return ret
    return ret

if __name__=="__main__":
    x=parse("/media/asdazey/PSCSTA/Judge/hashtags.in")
    #x=parse("/home/asdazey/Desktop/PSCSTA/logan/ht/hashtags.in")
    #print(x)

    n=int(x[0])
    x=x[1:]

    for i in range(n):
        m = []
        for j in x[i].split(" "):
            k = getone(j)
            if k!= "":
                m.append(k)
        print(" ".join(m))