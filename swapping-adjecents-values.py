inp = input () 
l = inp.split () 

N = len(l) - 1
for i in range (0, N, 2):
    (l[i], l[i+1]) = (l[i+1], l[i])

result = "".join(l)
print (result) 

# inp (input) = user enters ' 1 4 5 6 7 8'
# output is displayed as ' 4 1 6 5 8 7 ' 
