# IntroCS-Track-A

# Class 1 - 31/08/2026 

What is a computer?

v.g: Cellphones, E-Cars, Tablet, Bio-Computer

A computer has an Input, a central unit to process the input, and it generates an Output

- Hardware
- Software



More specifically it follows the von Neumann architecture

Input Device -> Central Processing Unit {Control UJnit, Arithmetic/Logic Unit} <-> Memory Unit -> Output


# Class 2 - 07/09/2026 

## Converting

How to transform a decimal number into any other base?

Here is the step-by-step process:

Divide the decimal number by the new base B.

1 - Write down the remainder. (This remainder will be a digit in the new base).

2 - Replace the decimal number with the quotient (the result of the division).

3 - Repeat steps 1–3 until the quotient becomes 0.

4 - Read the remainders backwards (from the last remainder to the first). This is your final answer.

Important: Digits in Bases larger than 10
If your new base is larger than 10 (like base-16 hexadecimal), you need letters to represent digits above 9:

10 = A

11 = B

12 = C

13 = D

14 = E

15 = F
(And so on for higher bases)

example:

35 in the base of 3

35 ÷ 3 = 11 R 2

11 ÷ 3 = 3 R 2

3 ÷ 3 = 1 R 0

1 ÷ 3 = 0 R 1

Read backwards: 1022

## Arithmetric Operations

### Addition and Subtraction

In base B:

You are allowed digits from 0 to B-1.

You carry when a column's sum reaches B (not 10, not 2, but B).

![alt text](image.png)

You borrow an amount of B from the left column (not 10, not 2, but B).


When you "borrow", you add B amount.


For multiplication in a generic base B, the logic stays exactly the same as decimal and binary, but now you have to deal with larger times tables.

Here is the golden rule for multiplying in base B:

### Multiplication and Division

When you multiply two digits and get a product P, you write down P mod B (the remainder) and carry P ÷ B (the quotient) to the next column.

Just like in base 10, if you multiply 7 x 8 = 56, you write down 6 (56 mod 10) and carry 5 (56 ÷ 10). In base B, you do the exact same thing, just with a different number.


## Bit, byte, words 

Bit (The Smallest Unit), 

Byte (The Standard Building Block), 8 bits stuck together (e.g., 10110011) ( A single letter in a book)

Word (The Natural Size), A group of multiple Bytes (usually 2, 4, or 8 bytes), (default chunk of data that a computer's processor (CPU) prefers to handle at one time.) 

 - A 32-bit computer has a Word = 4 bytes (32 bits).

 - A 64-bit computer has a Word = 8 bytes (64 bits).

 ## How 1s and 0s are made in computers

  TRANSISTORS

![alt text](image-1.png)

   A transistor is essentially just a tiny electronic switch

Source: Electricity enters here.

Drain: Electricity exits here.

Gate: The "key" that controls the flow.

When you apply a small voltage (electrical pressure) to the Gate, it acts like you squeezing the hose—it opens a bridge inside the transistor, allowing electricity to flow freely from the Source to the Drain.

When you remove the voltage from the Gate, the bridge closes, and electricity stops flowing.