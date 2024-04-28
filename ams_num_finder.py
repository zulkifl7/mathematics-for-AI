'''
Task
-----
Develop a computational program to identify all Armstrong numbers 
within the range of 0 to 100,000. Formulate a systematic algorithm 
to derive the solution. Please submit your response as a gist on GitHub 
and provide the link to your gist containing the algorithm you have developed.


There are two different defenitions for armstrong number!

1. Armstrong number is a number that is equal to the sum of cubes of its digits.
 For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers. 
    REF : https://pages.mtu.edu/~shene/COURSES/cs201/NOTES/chap04/arms.html


2. Armstrong numbers are those numbers which are equal to the sum of the digits 
 of the number each raised to the power of the number of digits in the number itself.
    REF : https://u-next.com/blogs/data-science/what-is-armstrong-number/
          https://www.shiksha.com/online-courses/articles/armstrong-number-in-c/
          https://takeuforward.org/maths/check-if-a-number-is-armstrong-number-or-not/

We have given the solution to find the amstrong number respective to for both the defenitions.
'''


# Using defenition - 1

def ams_no_finder_1():
    for i in range(0, 100001):
        tot = 0
        for m in str(i):
            tot += (int(m)**3)
        if tot == i:
            print(i)
        
# Using defenition - 2

def ams_no_finder_2():
    for i in range(0, 100001):
        sum = 0 
        for digit in str(i):
            sum += int(digit) ** len(str(i))
        if i == sum:
            print(i)


print("Using defenition 1\n----------------")
ams_no_finder_1()
print("Using defenition 2\n----------------")
ams_no_finder_2()