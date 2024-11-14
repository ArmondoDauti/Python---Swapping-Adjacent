# Python - Swapping-Adjacents

The problem statement for this project is:
Given a sequence of numbers, swap adjacent items in pairs, i.e., the first number with the second number, the third number with the forth number, etc. Print the resulting sequence. If the sequence has an odd number of elements, leave the last element in place.

An example of how the output would look like:
Example
Input:
1 3 2 6 7
Output:
3 1 6 2 7

Step 1 Swap adjacent

As we decided to use a list as our main data structure, we need to convert our input to a list
str object in Python has a method split()
return type of this method is a list of strings

here is an example
s = "abc xyz 123 "
l = s.split()  #l is a list
print(l)


the split() method is more powerful; read more in Python documentation
So the following code can be used at the first step of our solution

Step 2

Now let us think how to swap adjacent elements in a list
for starters, let us assume the list has a fixed size, say 2

the traditional universal method to swap values of two variables in programming is by using a new variable
l = [10, 20]
new_var = l[0]
l[0] = l[1]
l[1] = new_var
print(l)


However, in Python swapping can be done more conveniently by using tuples
l = [10, 20]
(l[0], l[1]) = (l[1], l[0])
print(l)

Let us now consider a bigger list l of fixed size, say 5
we need to swap l[0] with l[1] as above
then we need to swap l[2] with l[3]

Step 3

l (variable) now contains all the data that is necessary for the output. It remains to produce the output string and print it
if we are given a list of strings, a traditional method to join them together is by using a loop

l = ["xx", "yy", "zz"]
s = ""
for i in range(0, len(l)-1):
  s+=l[i] + " "

s+= l[len(l)-1]
print(s)


however, Python provides a more convenient join() method of str (see Python documentation)
l = ["xx", "yy", "zz"]
s = " ".join(l)
print(s)
