from data_parser import parse

if __name__=="__main__":
    x=parse("/media/asdazey/PSCSTA/Judge/icecreamcatch.in",True)
    #x=parse("/home/asdazey/Desktop/PSCSTA/logan/icc/icecreamcatch.in",True)
    #print(x)

    n=int(x[0][0])
    x=x[1:]

    for i in range(n): #all
        #print(x)
        s=int(x[0][0])
        x=x[1:]

        max=int(x[0][0])
        min=int(x[0][0])
        for j in range(s): #for all tests
            #print(x[j])

            if int(x[j][0])<min:
                min=int(x[j][0])
            
            if int(x[j][1])>max:
                max=int(x[j][1])
            
        print(min, max, (max-min+1))

        x=x[s:]