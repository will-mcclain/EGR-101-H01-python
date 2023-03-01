## Will McClain
## Question 3


G = 9.8

t = []
y = []
y_prime = []
y_double_prime = []

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
    # loop spans i=0-51, which represents the 51 100ms time blocks in 5.1 seconds
    for i in range(52):
        # advance time 100ms
        t.append(i/10)
        
        # update y, y_prime, and y_double_prime with new entries
        y.append(25*t[i] - G/2 * t[i]**2)
        append_custom_derivative(i, y_prime, y, 1)
        append_custom_derivative(i, y_double_prime, y_prime, 2)

    print("y (m):")    
    print_list(y)
    print("\ny' (m/s):")
    print_list(y_prime)

    input()

main()


## y[-3, -1] (m) = [4.850999999999985, 2.499999999999986, 0.05099999999998772]
## y_prime[-3, -1] (m/s) = [-22.530000000000022, -23.510000000000076, -24.490000000000066]
