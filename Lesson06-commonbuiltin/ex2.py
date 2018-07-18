#凱薩加密法
def key():
    a=input("請輸入明文：")
    b=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]*len(a)
    c=[]
    
    for i in a:
        for j in b:
            if j==i:
                d=int(b.index(j))+3
                c.append(b[d])
                break
    str=''
    print(str.join(c))

key()