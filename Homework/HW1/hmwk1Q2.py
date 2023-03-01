## Will McClain
## Question 2

NUM_OF_TAYLOR_TERMS = 100
PI = 3.14

t = []
y = []
s = []
theta = []

# loops through any list, makes reading easier
def print_list(list_name):
    for i in range(len(list_name)):
        print(list_name[i])

# approximates arctan to NUM_OF_TAYLOR_TERMS terms
def arctan(x):
    total = 0
    for i in range(NUM_OF_TAYLOR_TERMS):
        total += (-1)**i * (x**(2*i+1)) / (2*i+1)
    return total

# easy radian to degree conversion
def convert_rads_to_degrees(angle):
    return angle * 180 / PI

def main():
    # loop spans i=0-100, which represents the 100 100ms time blocks in 10 seconds
    for i in range(101):
        # advance time 100ms
        t.append(i/10)
        # update y, s, and theta with new entries
        y.append(5*t[i])
        # done by pythagorean theorem
        s.append((y[i]**2 + 100**2)**(1/2))
        # append new angle to theta list
        angle_measure = convert_rads_to_degrees(arctan(y[i]/100))
        theta.append(angle_measure)
    
    print("Height(m):")
    print_list(y)
    print("\nLine-of-sight distance(m):")
    print_list(s)
    print("\nMax line-of-sight angle(degrees):\n" + str(max(theta)))
    input()

main()


## y[-3, -1] (m) = [49.0, 49.5, 50.0]
## s[-3, -1] (m) =  [111.35977729862789, 111.58068829327054, 111.80339887498948]
