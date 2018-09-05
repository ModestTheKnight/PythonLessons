import series
import trig
import math

print('HELLO')
n=int(input('Enter something:'))
print "Your number is ", n
if n==10:
    print ('You win')
else:
    print('You lose')
print "%i! = %i" % (n, series.factor(n))
f1,f2 = series.fibo(n)
print "F(%i) = %i" %(n-1, f1)
print "F(%i) = %i" %(n, f2)
f=open('test')
while f:
    try:
        nf=int(f.readline())
        print "%i! = %i" % (nf, series.factor(nf))
    except:
        print ('Empty string mean end of file')
        break
x=float(input('Enter something for sin&cos:'))
if x<= 10*math.pi:
    print "sin is ", trig.sin(x)
    print "cos is ", trig.cos(x)
    print "sin^2 + cos^2 = ", (trig.sin(x)**2 + trig.cos(x)**2)
else:
    print "Oh, too much"
    print math.pi
    print math.cos(x)
    print math.sin(x)
