# Valid Brackets
In this problem, we consider expressions containing opening brackets and closing brackets that are either properly or improperly nested. 
```
( a + $ ( b = ) ( a ) )    # this is properly nested

( a + $ ) b = ) ( a ( )    # this is not
```

There will be several pairs of brackets, so we have to impose a second condition on the expression: the matching brackets should be of the same kind. Consequently `(())` is OK, but `([))` is not. The pairs of brackets are:
```
( )
[ ]
{ }
< >
```

## Objective
Fill in the `is_valid(expr)` function to check whether the brackets contained in the given expression are properly nested. If the expression is **not** properly nested your program should determine the position of the offending bracket &mdash; that is, the first position at which the expression can be determined as improperly nested.

## Output
Your `is_valid(expr)` function should return one of the following to be printed by the `main()` function:
- `YES` if the expression is properly nested
- `NO` if the expression is not properly nested, followed by a space and the position of the offending character.

## Considerations
- For expressions that are **not** properly nested, be sure to count *all* characters when determining the offending position, not just those that are brackets. That includes whitespace characters!
- If the expression ends with all brackets in the proper order, but leaves one or more open brackets unclosed, the offending position is considered to be the end of the expression (the number of characters, plus 1). [see the [**Unclosed bracket**](#unclosed-bracket) example below]
- Be sure to use quotes around your expression when running the program from the command line as the examples below show. Otherwise, your shell may interpret certain characters for itself instead of passing them through to your program. If that happens, press Ctrl-c to return to your terminal prompt.

## Examples

#### All open brackets properly closed
```
% python brackets.py "(a{+})"
YES
```

#### Contains no brackets
```
% python brackets.py "*a*"
YES
```

#### Missing a closing bracket
```
% python brackets.py "  (a"
NO 5
```

#### Mismatched closing bracket
```
% python brackets.py "([))"
NO 3
```

## Hints
In earlier readings, you were introduced to the concept of <a title="Using Lists as Stacks" href="https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks" target="_blank">Using Lists as Stacks</a>. This problem would lend itself nicely to such a strategy. Also, carefully consider whether a `while` loop or a `for` loop is more beneficial for accomplishing this task.

## Submitting your work
To submit your solution for grading, you will need to create a github [Pull Request (PR)](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests). Refer to the `PR Workflow` article in your course content for details.
