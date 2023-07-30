# Riemann_Sum_Pi_Approximation
This is Python code that approximates the area of a circle with an area of pi using a Riemann sum so that I can prove to myself that 3.14159... is the actually value of pi. 
It does this by using the fact that the A = π*r^2
If we use r = 1, then the equation is A = π
Then we can use the equation for a circle with radius 1 which is x^2 + y^2 = 1
Then we solve for y by moving x^2 over and making it y^2 = 1-x^2
and then we change it to y = sqrt(1-x^2)
Technically it should be ±sqrt(1-x^2), but it is fine because we are just looking for the area of a section so that we can multiply it later.
Now we use the Riemann sum to get the area of the right quadrant
And now we get A = pi ≈ 4 Σ sqrt(1-(i/n)^2)/n where i is the lower bound of the sum and n is the upper bound

