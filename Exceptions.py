def sanitize(n):
    while type(n) != int():
        try:
            n = int(n)
            n = 18 // n
            return str(n)
        except ValueError:
            n = input("Not a number, try again ")
        except ZeroDivisionError:
            n = input("Don't try zero ")

i = input("Enter a number ")
print("Value after arithmetic " + sanitize(i))
