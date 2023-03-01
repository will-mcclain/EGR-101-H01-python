## Will McClain
## Question 1

t = []
s = []
x = []
x_prime = []

# loops through any list, makes reading easier
def print_list(list_name):
    for i in range(len(list_name)):
        print(list_name[i])

def check_string_is_int_or_float_TF(data):
    #.replace() turns "3.05" into "305", which is checked with .isdigit()
    if data.replace('.', '', 1).isdigit():
        return True
    return False

# if user input isn't a float or an int or is less than 10m, ask for input again
def input_handler(prompt):
    while True:
        output = input(prompt)
        if not check_string_is_int_or_float_TF(output):
            print("That's not an acceptable value. Try again...")
            continue
        #rope has to be at least 10m in length to be pulled for 6 sec
        if float(output) < 10:
            print("That's not an acceptable value. Try again...")
            continue
        break;
    return output

# need a special function for this because the main loop spans i=0-60, when x_prime only is calculated from i=1-60
def append_x_prime_value(i):
    if i == 0:
        x_prime.append(0)
    else:
        # change in distance per change in time, should be negative
        x_prime.append((x[i]-x[i-1]) / (t[i]-t[i-1]))

def main():
    # take value for rope length, treated as a constant
    STARTING_ROPE_LENGTH = float(input_handler("How long is the rope? (>4m) "))
    # loop spans i=0-60, which represents the 60 100ms time blocks in 6 seconds
    for i in range(61):
        # advance time 100ms
        t.append(i/10)
        
        # update s, x, and x_prime with new entries
        # rope length decreases by 0.1m per 100ms
        s.append(STARTING_ROPE_LENGTH - 1*t[i])
        # done by pythagorean theorem
        x.append((s[i]**2 - 4**2)**(1/2))
        append_x_prime_value(i)

    print("Rope length(m):")
    print_list(s)
    print("\nDistance from dock(m):")
    print_list(x)
    print("\nBoat velocity(m):")
    print_list(x_prime)
    print("\nMax boat speed, min velocity(m/s)")
    print(min(x_prime))
    input()

main()


##For STARTING_ROPE_LENGTH = 12:
##    s[-3, -1] (m) =  [6.2, 6.1, 6.0]
##    x[-3, -1] (m) = [4.7370877129308315, 4.60543157586781, 4.472135954999608]
##    x_prime (m/s)[-3, -1] = [-1.301496965243776, -1.316561370630211, -1.3329562086820215]
##    min(x_prime) (m/s) = -1.3329562086820215
