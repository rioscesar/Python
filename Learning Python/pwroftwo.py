def pwroftwo( number ):
    while number >= 1:
        if number == 1:
            return True
        if number % 2 == 0:
            number = number // 2
        else:
            return False
    return False

def fastpwroftwo( number ):
    if number == 0:
        return False    
    return 0 == (number&(number-1))

for i in range( 32768 ):
    if pwroftwo( i ):
        print( i )

print()

for i in range( 32768 ):
    if fastpwroftwo( i ):
        print( i )

    
