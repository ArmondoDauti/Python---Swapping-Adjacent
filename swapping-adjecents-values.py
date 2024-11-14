inp = input () 
l = inp.split () 

N = len(l) - 1
for i in range (0, N, 2):
    (l[i], l[i+1]) = (l[i+1], l[i])

result = "".join(l)
print (result) 
