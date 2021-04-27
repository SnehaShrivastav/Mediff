
def checkPalindrome(val):
    val = val[::-1]
    return val

val = input("Enter your value: ")
rev_val = checkPalindrome(val)

if val == rev_val:
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")