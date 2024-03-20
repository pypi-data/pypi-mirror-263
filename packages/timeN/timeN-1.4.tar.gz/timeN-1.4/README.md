# Package Description

timeN is a simple package that contains a customizable `@timen` decorator which times how long it takes (in milliseconds) for the decorated function to run n times. The decorator supports printing, forwards return values to the calling function, and can even work on recursive functions (see [A Note about Recursion](#a-note-about-recursion)).

# Usage

The timen decorator is quite simple to use. it can be imported by simply importing it from the timeN package with 
```python
from timeN import timeN
```
From there, the timeN decorator can be used like any other decorator, with the exception that you must end the decorator in parentheses since it takes optional parameters
```python
@timeN()
def foo():
    print("Hello World")
```
Output:
```
Hello World
...
Hello World
foo took 2.0 milliseconds to run 10 times
```
The 2 optional parameters are: n (number of times to run the function) and round_to (number decimal places to round the final result to).
```python
@timeN(100, 5)
def foo():
    print("Hello World")
```
Output:
```
Hello World
...
Hello World
foo took 11.99365 milliseconds to run 100 times
```

# A Note about Recursion

Due to limitations within python decorators themselves, if you would like to time a recursive function like the following...
```python
@timeN(1, 10)
def virfib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return virfib(n-2) + virfib(n-1)

virfib(4)
```
...then that will not work. The reason why is because every time virfib is recursively called, the decorator function is also called. This leads to recursive calling of the timing function, meaning that a function that is recursively called 4 times will be timed 5 times (once for the original function call and once more for EACH recursive call).

To fix this issue, simplay call your recursive function from another function, and time the second function instead:
```python
def virfib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return virfib(n-2) + virfib(n-1)

@timeN(1, 10)
def virfib_caller():
    print(virfib(4))

virfibcaller()
```
In this way only the call to `virfib_caller()` is timed, and since all that that function does is call `virfib`, it will give the desired result.

A higher order recursive function will work flawlessly with timeN:
```python
@timeN(1, 10)
def virfib(n):
    def fib_helper(i, curr, next):
        return curr if i >= n else fib_helper(i+1, next, curr+next)
    return fib_helper(0, 0, 1)

virfib(100)
```
Output:
```
-------------- Captured return value from function virfib --------------
354224848179261915075
virfib took 0.0 milliseconds to run 1 times
```