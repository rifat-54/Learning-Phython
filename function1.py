
def avgnum(*num):
    print(type(num))
    sum=0
    for i in num:
        sum=sum+i
    print(sum)

avgnum(2,5,6,10)