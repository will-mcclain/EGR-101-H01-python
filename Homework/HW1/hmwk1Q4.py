## Will McClain
## Question 4


G = 9.8

t = []
y = []
y_prime = []
x = []
x_prime = []

# loops through any list, makes reading easier
def print_list(list_name):
    for i in range(len(list_name)):
        print(list_name[i])

# makes a new list by approximating the derivative of each term from another list
def append_custom_derivative(i, custom_list, previous_list, num_of_skipped_steps):
    # if i points to a value we want to skip, just append 0
    if i in list(range(num_of_skipped_steps)):
        custom_list.append(0)
    else:
        # change in previous_list per change in time
        custom_list.append((previous_list[i]-previous_list[i-1]) / (t[i]-t[i-1]))

def main():
    # loop spans i=0-32, which represents the 32 100ms time blocks in 3.2 seconds
    for i in range(33):
        # advance time 100ms
        t.append(i/10)
        
        # update y, y_prime, x, and x_prime with new entries
        y.append(50 - G/2 * t[i]**2)
        append_custom_derivative(i, y_prime, y, 1)
        x.append(10 * t[i])
        append_custom_derivative(i, x_prime, x, 1)

    print("y (m):")    
    print_list(y)
    print("\ny' (m/s):")
    print_list(y_prime)
    print("\nx (m):")    
    print_list(x)
    print("\nx' (m/s):")
    print_list(x_prime)
    input()

main()


## x[-3, -1] (m) = [30.0, 31.0, 32.0]
## x_prime[-3, -1] (m/s) = [9.999999999999991, 9.999999999999991, 9.999999999999991]
## y[-3, -1] (m) = [5.899999999999999, 2.910999999999987, -0.17600000000001614]
## y_prime[-3, -1] (m/s) = [-28.909999999999958, -29.89000000000009, -30.870000000000005]
