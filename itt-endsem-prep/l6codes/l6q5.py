import re

s = "heya whats going on"

c = re.sub("whats", "nothing", s)

print(c)
