import check50
import check50.c

with open('test.txt') as f:
    lines = f.read().split()

@check50.check()
def exists():
    """hello.c exists"""
    check50.exists("hello.c")

@check50.check(exists)
def txtexists():
    """test.txt exists"""
    check50.exists("test.txt")
    check50.log(lines)

@check50.check(txtexists)
def compiles():
    """hello.c compiles"""
    check50.c.compile("hello.c", lcs50=True)

@check50.check(compiles)
def emma():
    """responds to name Emma"""
    check50.run("./hello").stdin("Emma").stdout("Emma").exit()

@check50.check(compiles)
def blah():
    """responds to word Blah"""
    check50.run("./hello").stdin("Blah").stdout("Blah").exit()
    
@check50.check(txtexists)
def content():
    with open('test.txt') as f2:
        linesRez = f2.read().split()
        if(len(linesRez) < 1):
            raise check50.Failure("Faile test.txt nepakanka duomenų")
        else:
            if (str("testas") != linesRez[0]):
                raise check50.Failure("Blogi duomenys")   
