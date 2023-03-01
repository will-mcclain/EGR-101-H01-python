## Will McClain
## Question 1


# Universal constants
G = 6.674 * 10**(-11) #Nm^2kg^-2
K = 9.0 * 10**9 #Nm^2C^-2

# Set masses and charges
m1 = 9.1 * 10**(-31) #kg
m2 = 9.1 * 10**(-31) #kg
q1 = 1.6 * 10**(-19) #C
q2 = 1.6 * 10**(-19) #C

d = list(range(1,101)) #pm
Fg = [] #N
Fe = [] #N

# loops through any list, makes reading easier
def print_list(list_name):
    for i in list_name:
        print(i)

def main():
    # loop through distance values and calculate Fg & Fe
    for i in d:
        Fg.append(G * m1 * m2 / (i * 10**(-12))**2)
        Fe.append(K * q1 * q2 / (i * 10**(-12))**2)
    print("Distance (pm)")
    print_list(d)
    print("\nGravitational Force (N)")
    print_list(Fg)
    print("\nElectrostatic Force (N)")
    print_list(Fe)
    input()

main()


## d[-3, -1] (pm) = [98, 99, 100]
## Fg[-3, -1] (N) = [5.754622448979591e-51, 5.638954596469749e-51, 5.526739399999999e-51]
## Fe[-3, -1] (N) = [2.3990004164931284e-08, 2.3507805325987156e-08, 2.3040000000000003e-08]
