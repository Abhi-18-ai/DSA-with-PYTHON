# by recursion

def palindrome(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False

    return palindrome(s,left+1,right-1)

s = "anbcddcbna"
n = len(s)
answer = palindrome(s,0,n-1)
print(answer)