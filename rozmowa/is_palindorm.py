#def is_palindrome(s): return len(s) <=1 or list(s[:len(s)/2])==list(reversed(s[-(len(s)/2):]))

#print(is_palindrome('dawid'))

def is_palindrome(a):
    return a == a[::-1]

print(is_palindrome('dupaapud'))