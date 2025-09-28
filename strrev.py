
#simple code for string reversal


def reverse(s):
  a=''.join(reversed(s))
  return a  

str=str(input("enter a string"))
print(reverse(str))
