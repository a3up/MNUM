from math import log, sqrt

def regula_falsi(function, a, b, error = pow(10,-5)):
    while abs(a - b) > error:
        average = (a * function(b) - b * function(a)) / (function(b) - function(a))
        if function(a) == 0:
            return a
        elif function(a)*function(average) < 0:
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
        print(regula_falsi(functions[i][0],interval[0],interval[1]))
