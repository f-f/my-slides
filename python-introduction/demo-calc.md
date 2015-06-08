# Demo calcolatrice

>>> 2 + 3
>>> 3 * 5

Examples of floating point numbers (or floats for short) are 3.23 and 52.3E-4. 
The E notation indicates powers of 10. In this case, 52.3E-4 means 52.3 * 10^-4^.

Quick overview:

+ (plus)
    Adds two objects
    3 + 5 gives 8. 'a' + 'b' gives 'ab'.

- (minus)
    Gives the subtraction of one number from the other; if the first operand is absent it is assumed to be zero.
    -5.2 gives a negative number and 50 - 24 gives 26.

* (multiply)
    Gives the multiplication of the two numbers or returns the string repeated that many times.
    2 * 3 gives 6. 'la' * 3 gives 'lalala'.

## Commenti

** (power)
    Returns x to the power of y
    3 ** 4 gives 81 (i.e. 3 * 3 * 3 * 3)

/ (divide)
    Divide x by y
    13 / 3 gives 4. 13.0 / 3 gives 4.333333333333333

## Exceptions

% (modulo)
    Returns the remainder of the division
    13 % 3 gives 1. -25.5 % 2.25 gives 1.5.

< (less than)
    Returns whether x is less than y. All comparison operators return True or False. Note the capitalization of these names.
    5 < 3 gives False and 3 < 5 gives True.
    Comparisons can be chained arbitrarily: 3 < 5 < 7 gives True.

## Variables

> (greater than)
    Returns whether x is greater than y
    5 > 3 returns True. If both operands are numbers, they are first converted to a common type. Otherwise, it always returns False.

== (equal to)
    Compares if the objects are equal
    x = 2; y = 2; x == y returns True.
    x = 'str'; y = 'stR'; x == y returns False.
    x = 'str'; y = 'str'; x == y returns True.

## Intro booleani

<= (less than or equal to)
    Returns whether x is less than or equal to y
    x = 3; y = 6; x ⇐ y returns True.

>= (greater than or equal to)
    Returns whether x is greater than or equal to y
    x = 4; y = 3; x >= 3 returns True.

!= (not equal to)
    Compares if the objects are not equal
    x = 2; y = 3; x != y returns True.

## Algebra booleana

not (boolean NOT)
    If x is True, it returns False. If x is False, it returns True.
    x = True; not x returns False.

and (boolean AND)
    x and y returns False if x is False, else it returns evaluation of y
    x = False; y = True; x and y returns False since x is False. In this case, Python will not evaluate y since it knows that the left hand side of the 'and' expression is False which implies that the whole expression will be False irrespective of the other values. This is called short-circuit evaluation.

or (boolean OR)

    If x is True, it returns True, else it returns evaluation of y
    x = True; y = False; x or y returns True. Short-circuit evaluation applies here as well.

Shortcuts for math operation and assignment:

It is common to run a math operation on a variable and then assign the result of the operation back to the variable, hence there is a shortcut for such expressions:

a = 2
a = a * 3

can be written as:

a = 2
a *= 3

