"""
Stacks
Pop - O(1)
Push - O(1)
Peek - O(1)
"""


"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true

"""

def isValid(self, s: str) -> bool:
    
    #create a stack to keep track of balance
    stack = []

    for char in s:
        #if opening parenthesis, add to the stack
        if char == '[' or char == '{' or char == '(':
            stack.append(char)
        #if close parenthesis, and top of the stack is matching open, pop from the stack
        elif (char == ']' and stack and stack[-1] == '[') or (char == '}' and stack and stack[-1] == '{') or (char == ')' and stack and stack[-1] == '('):
                stack.pop()
        #return false if stack is not empty
        else:
            return False

    return stack == []


"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.

Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

"""

def eval_polish_notation(tokens):
    
    stack = []

    for char in tokens:
        #if current char is not an operator
        if char not in ["+","-","/","*"]:
            stack.append(int(char))
        else:
            #pop last element from the stack
            y = stack.pop()
            x = stack.pop()
            if char == "+":
                stack.append(x+y)
            elif char == "-":
                stack.append(x-y)
            elif char == "*":
                stack.append(x*y)
            elif char == "/":
                stack.append(int(x/y))

    return stack[-1]


"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
Example 4:

Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right. Asteroids moving the same direction never meet, so no asteroids will meet each other.


"""

def collisions(asteroids):
    
    stack = []
    
    for asteroid in asteroids:
        #if asteroid is positive, add it to the stack
        if asteroid > 0:
            stack.append(asteroid)
            
        #if negative
        else:
            #simulate collisions
            #while stack is not empty
            #the last element on the stack is postivive
            #the current element is greater than last element
            while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                stack.pop()
            #if stack is empty or the last element is negative
            #add elements on to the stack
            if not stack or stack[-1] < 0 :
                stack.append(asteroid)
            elif stack[-1] == abs(asteroid):
                stack.pop()
                
    return stack


"""
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"


Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

"""

def minimum_parentheses(s):
    
    
    
    """
    First Case:
    lee(t(c)o)de)
                i
    op = 0
    first = lee(t(c)o)de
    
    Second Case:
    
    ))((
       i
    op = 2
    first = ((
    
    
    
    
    
    """
    
    first = ""
    op = 0
    for i in range(len(s)):
        if s[i] == "(":
            op += 1
        elif s[i] == ")":
            if op == 0:
                continue
            op -= 1
        first += s[i]
            
    res = ""
    for i in range(len(first)-1,-1,-1):
        if first[i] == "(":
            op -= 1
            if op >= 0:
                continue
            
        res += first[i]
        
    return res[::-1]