# -*- coding: utf-8 -*-
'''

Operators Precedence

Operator					Description
**							Exponentiation (raise to the power)
~ + -						Complement, unary plus and minus (method names for the last two are +@ and -@)
* / % //					Multiply, divide, modulo and floor division
+ -							Addition and subtraction
>> <<						Right and left bitwise shift
&							Bitwise 'AND'
^ |							Bitwise exclusive `OR' and regular `OR'
<= < > >=					Comparison operators
<> == !=					Equality operators
= %= /= //= -= += *= **=	Assignment operators
is is not					Identity operators
in not in					Membership operators
not or and					Logical operators

'''
def main():
	# Values
	a = 20
	b = 20

	if ( a is b ):
	   print "a and b have same identity"
	else:
	   print "a and b do not have same identity"

	if ( id(a) == id(b) ):
	   print "a and b have same identity"
	else:
	   print "a and b do not have same identity"

	b = 30
	if ( a is b ):
	   print "a and b have same identity"
	else:
	   print "a and b do not have same identity"

	if ( a is not b ):
	   print "a and b do not have same identity"
	else:
	   print "a and b have same identity"
		
# Practice excercise
def excercise():
	print 'Write a program to hmmmmm!!';

if __name__ == '__main__':
    main();