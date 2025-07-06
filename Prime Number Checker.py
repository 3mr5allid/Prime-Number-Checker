def is_prime(n):
    if n == 2 :
        return ('Is Prime')
    elif n<=1 or n % 2 == 0:
        return ("Not Prime")
    else:
        return ("Is Prime")
    
print(is_prime(n=int(input("Enter The Number: "))))