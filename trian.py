from itertools import chain 
 
def next_Sierpiński(triangle): 
    base = (len(triangle[0]) << 1) | 1 
    return chain((row.center(base) for row in triangle), 
                 map(' '.join, zip(triangle, triangle))) 
 
def Sierpiński(height): 
    triangle = generate_triangle(height) 
    while True: 
        yield triangle 
        triangle = list(next_Sierpiński(triangle)) 
 
def generate_triangle(height): 
    base = height << 1 
    return [('*' * i).center(base - 1) for i in range(1, base + 1, 2)] 
 
 
from itertools import islice 
 
triangles = list(islice(Sierpiński(3), 4)) 
print(*triangles[-1], sep = '\n') 