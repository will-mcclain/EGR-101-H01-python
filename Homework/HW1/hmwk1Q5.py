## Will McClain
## Question 5


t = []
a = []
v = []

# loops through any list, makes reading easier
def print_list(list_name):
    for i in range(len(list_name)):
        print(list_name[i])

# for any list of values, function will run through the list and approximate the list's integral, takes how long each interval lasts as a param
def return_integral(integrand_list, time_increment_seconds):
    total = 0
    for i in integrand_list:
        total += i * time_increment_seconds
    return total

def main():
    # loop spans i=0-150, which represents the 150 100ms time blocks in 15 seconds
    for i in range(151):
        
        # advance time 100ms
        t.append(i/10)
        
        # populate a and v with new entries
        # acceleration can be found by a(t) = (1/2)t for 0<=t<=10 and a(t) = 5 for t>10
        if i < 100:
            a.append((1/2)*t[i])
        else:
            a.append(5)
        # append the integral of a when a = [x0], then a = [x0, x1], then a = [x0, x1, x2], etc.
        v.append(return_integral(a, 0.1))

    print("v (m/s):")    
    print_list(v)
    input()

main()


## v[-3, -1] (m) = [49.25, 49.75, 50.25]
