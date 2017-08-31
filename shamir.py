#Carson Harmon
#Purdue University
#Harmon35@purdue.edu
import random

def generateA(t, Zp, s):
    #Generate random coeficents
    a = []
    for i in range(t-1):
        a.append(random.choice(Zp))
    a.append(s)
    #print "Coefficents", a
    return a
def px(a, x, p):
    val = 0
    degree = len(a) - 1
    for i in range(len(a)):
        val += (a[i]*(x ** degree)) % p
        #print a[i], x, "**", degree
        degree -= 1
    val = val % p
    #print x, val
    return val

def reconstruct(x, p):
    #given the points, we need to construct a line and plugin 0 for X.
    #Lagrange interpolation of t coordinates
    secret = 0
    value = 0
    print x
    for i in range(len(x)):
        numerator = x[i][1]
        denominator = 1
        for j in range(len(x)):
            if i != j:
                numerator *= (0-x[j][0])
                denominator *= (x[i][0] - x[j][0])
        value = numerator/denominator
        secret += value
    print "Reconsturcted Secret", secret % p

def main():
    #Create ZP
    Zp = [0, 1, 2, 3, 4, 5, 6] #p = 5, Zp = {0...p-1} where p is prime
    p = 7


    s = random.choice(Zp) #S is the secret chosen at random from Zp
    print "Secret:", s

    t = 3 #2 people can construct the key, 2-1=1 so simple line

    #Generate random coefficents for the polynomial
    a = generateA(t, Zp, s)

    #get secrets
    x1 = 1
    y1 = px(a, x1, p)
    secret1 = (x1, y1)
    x2 = 2
    y2 = px(a, x2, p)
    secret2 = (x2, y2)
    x3 = 3
    y3 = px(a, x3, p)
    secret3 = (x3, y3)
    points = [secret1, secret2, secret3]

    #Reconstruct secret from points
    reconstruct(points, p)


main()

