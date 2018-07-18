# def eightqueen八皇后

def eightqueen(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8):
    for a in [(x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5),(x6,y6),(x7,y7),(x8,y8)]:
        for b in [(x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5),(x6,y6),(x7,y7),(x8,y8)]:
            if a!=b:
                if a[0]!=b[0]:
                    if abs((b[1]-a[1])/(b[0]-a[0]))!=1:
                        return "true" 
print(eightqueen(0,0,1,4,2,7,3,5,4,2,5,6,6,1,7,3))