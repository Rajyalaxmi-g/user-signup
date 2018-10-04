import re

s = 'abcghyuiokjuihj@klyte.com'

#p = re.search('^[_A-Za-z0-9]@\.{3,20}\S+$',s)
p = re.search('^(?=.{3,20}$)[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$',s)
#regex_str = "^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"
if p:
    print("email found")
else:
    print("not found")