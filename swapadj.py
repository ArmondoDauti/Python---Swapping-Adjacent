l = ["aa", "bb", "cc"]
s = ""

for i in range (0, len(l)-1):
    s += l[i] + ""

s += l[len(l)-1]
print (s)

# output = ' aabbcc ' 
