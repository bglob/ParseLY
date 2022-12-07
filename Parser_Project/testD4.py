def myfunction():
    test1+=1

def test2(fname):
    name=fname

def test3(fname,lname):
    name=fname+lname

def test4(size, n):
    for x in n:
        result=x-size
    return result

myfunction()
test2("Melissa")
fname="Raju"
lname="Nichols"
test3(fname, lname)

result=test4(4, n)