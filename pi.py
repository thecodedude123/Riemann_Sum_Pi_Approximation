import math
while True: # we loop so that the user can continue expirimenting with the amount of iterations
    pi = 0 # we initialize the value pi
    n = int(input("put a number here:"))# we allow input to choose the amount of iterations the progam will go through to get a more accurate number for pi
    for i in range (1,n):#                                                                            n
        pi += 4*math.sqrt(1-(i/n)**2)/n #This is code for a Riemann sum. Formally it would look like 4Σ (√(1-(i/n)^2))/n where √(1-(i/n)^2)) is the value of a function of a halfcircle at index i, and you multiply by 4 because this sum starts at a positive number, meaning only the right quadrant of the circle's approximated area is calculated and we divide it by n because that is the same as multiplying it by Δx
    print(pi)#  we print the value of the pi that we approximated with the Riemann sum here          i=1
    print(math.pi) # we print the actual value of pi here
    print("Difference:"+str(math.pi-pi))# we find out how much these values differe here
    

