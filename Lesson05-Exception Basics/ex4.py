relation = {'Jason':'Mary', 'Mary':'Jason', 'Jennifer':'Ken', 'Ken':'Jennifer', 'Tina':'Kim', 'Kim':'Tina'}

class raiseexception(Exception):
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
        if (self.p1 != relation[pa]) or (self.p2 != relation[pb]):
            raise Zerorelation("查無此人")
def check(pa, pb):
        if relation[pa] != pb:
            raise raiseexception("他們没关系","")
        
try:
    p1 = input("Please enter the first person: ")
    p2 = input("Please enter the second person: ")
    check(p1, p2)
    print("{} and {} are in love with each other!".format(p1, p2))
    
except raiseexception as e:
    print(e)

except Zerorelation as e:
    print(e)

check('Jason','Mary')


'''
def eightqueen(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8):
    if (x1!=x2) and (x3!=x2) and (x3!=x4) and (x5!=x4) and (x5!=x6) and (x6!=x7) and (x7!=x8):
        if (y1!=y2) and (y3!=y2) and (y3!=y4) and (y5!=y4) and (y5!=y6) and (y6!=y7) and (y7!=y8):
            if (x1!=y1) and (x2!=y2) and (x3!=y3) and (x4!=y4) and (x5!=y5) and (x6!=y6) and (x7!=y7) and (x8!=y8):
                print("true")

eightqueen(0, 0, 1, 4, 2, 7, 3, 5, 4, 2, 5, 6, 6, 1, 7, 3)'''








