# some exercises from python the hard way & some of my own
# pmcampbell
# 2022-01

'''  
before you run this code, try to decide what the outcome will be 
then   run the code to check your expectations
if they do not match think abou why that is 

hint: you will have to fix some  syntax to make them run properly
hint: remember operator precedence, check the slides

'''
print ("I will now count my chickens:)

print "Hens", 25 + 30 / 6)
print "Roosters", 100 - 25 * 3 % 4)

print (Now I will count the eggs)

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print ("What is 5 - 7?"), 5 - 7

print 'Oh, that's why it's False."

print "How"  about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2


print (f" 2/3 {2//3}")
print (f" 6/2.5 {6//2.5}")

print (f' 10 is an even number {10%3}")

print (f" 9 is an odd number {9%3}'')

num = 1/3
print ("type(num)")
print( 2*num)

print(1//3)
print(1%3)

# extra for those who were asking about using superscript
# to print non standard characters you can use the unicode value 

# numbers superscript ex  as follows
print("x\u00b2")  # x to the power of 2
print("y\u2079")  # y to the power of 9
# the \ escapes & the u is unicode followed by the character code
print("unicode spiral \u058D")  

# challenge look up some characters and display them also
# https://www.rapidtables.com/code/text/unicode-characters.html 