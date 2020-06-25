h1=int(input("Input h1:"))
h2=int(input("Input h2:"))
h3=int(input("Input h3:"))
t=int(input("Input t:"))
mine, minevar=t,0
for i in range (t//h3, -1, -1):
    for j in range((t-h3*i)//h2,-1,-1):
        k=(t-h3*i-h2*j)//h1+1
        e=h1*k+h2*j+h3*i-t
        print("h3 *",i,"h2 *",j,"h1 *",k,"excess",t,"by",e)
        if e<mine:
            mine, minevar=e, minevar+1
print("minimal excess is",mine,"(row #",minevar,")")
