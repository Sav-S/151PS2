########################################
# Name: Savanna Starks
# Collaborators:
# Estimated time spent (hr):2
########################################

def digital_root(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
        if len(str(total)) > len(str(1)):
            p = total
            total = 0
            total += p %10
            p = p // 10
            return total
        if len(str(total)) == len(str(1)):
            return total
        

        
 #while len(str(n)) > len(str(1)):
if __name__ == '__main__':
    # You can alter the below value to test your function with a variety
    # of numeric inputs!
   n = 1729
print("The digital root of ", n, " is ", digital_root(n))
