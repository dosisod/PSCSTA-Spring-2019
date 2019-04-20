from data_parser import parse

def find(n):
    n=int(n)
    last=0
    current=1
    for i in range(1000000):
        last=current
        current+=i
        if current>n:
            return [(i-1-(n-last)), (n-last)]

if __name__=="__main__":
    #x=parse("/home/asdazey/Desktop/PSCSTA/logan/it/infinite.in")
    x=parse("/media/asdazey/PSCSTA/Judge/infinite.in")
    #print(x)

    for i in range(int(x[0])+1):
        cord=find(x[i+1])
        #print(x[i+1])
        #print(cord)

        if cord[0]==0 and cord[1]==0:
            print(2)
        elif cord[0]==0 or cord[1]==0:
            print(3)
        else:
            print(4)