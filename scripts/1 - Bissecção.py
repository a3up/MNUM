from math import log, sqrt, floor

def bisection(function, a, b):
    iterations = 23 + log(b - a)/log(2)
    for i in range(floor(iterations)):
        average = (a + b)/2
        if function(average) == 0:
            return average
        if function(a) * function(average) < 0:
            b = average
        else:
            a = average
    return (a + b)/2

functions = [(lambda x: -2.75*pow(x,3)+18*x*x-21*x-12, 
                          (( -2,  0),
                           (  1,  3),
                           (  4,  7))),
    
             (lambda x: x-2*log(x)-5,
                          ((0.1,  1),
                           (  9, 10))),
              
             (lambda x: pow(2,sqrt(x)) - 10*x + 1,
                          ((  0,  1),
                           ( 98,100)))]

for i in range(len(functions)):
    print("\nf"+str(i))
    for interval in functions[i][1]:
        print(bisection(functions[i][0],interval[0],interval[1]))
