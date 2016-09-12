from math import sin, cos, pi,sqrt 
import matplotlib.pyplot as plt 
import matplotlib 

def triangleframe(p, n): 
    x_vertex1 = 0 
    y_vertex1 = 0 
     
    x_vertex2 = p * cos(pi / 3) 
    y_vertex2 = p * sin(pi / 3) 
     
    x_vertex3 = p * cos(0) 
    y_vertex3 = p * sin(0) 
     
 
    Sierpinskitriangledraw(x_vertex1,y_vertex1,x_vertex2,y_vertex2,x_vertex3,y_vertex3, n) 
    Sierpinskitriangledraw(x_vertex1,y_vertex1,x_vertex2,y_vertex2,x_vertex3,y_vertex3, n-1) 
     
 
    return 
 
 
def Sierpinskitriangledraw(xi, yi, xm, ym, xf, yf, n): 
    
    if n == 0: 
 
        plt.plot([xi, xm, xf, xi], [yi, ym, yf, yi], color = 'black') 
 
    elif n > 0: 
 
        pmedio1x = (xi + xm)/2 
        pmedio1y = (yi + ym)/2 
    
        pmedio2x = (xm + xf)/2 
        pmedio2y = (ym + yf)/2 
    
        pmedio3x = (xf + xi)/2 
        pmedio3y = (yf + yi)/2 
 
 
        Sierpinskitriangledraw(xi, yi, pmedio1x, pmedio1y, pmedio3x, pmedio3y, n-1)       
        Sierpinskitriangledraw(xm, ym, pmedio2x, pmedio2y, pmedio1x, pmedio1y, n-1) 
        Sierpinskitriangledraw(xf, yf, pmedio3x, pmedio3y, pmedio2x, pmedio2y, n-1) 
 
 
    return 
 
# Main program 
print 'This program draw the Sierpinski triangle fractal' 
print 'The user will be provide two parameters:' 
print ' (a) The length of line segment called p' 
print ' (b) The recursion level called n, this value will be a positive integer value' 
print 
r1 = float(raw_input('write the length of line segment: ')) 
print 
n1 = abs(int(raw_input('write the recursion level: '))) 
print 
print 
plt.figure('Sierpinski Triangle') # Create a window where draw the graphic of dragon curve 
plt.suptitle('Sierpinski Triangle Fractal') # Write the title of graphic inside of window 
triangleframe(r1, n1)  
plt.show() 