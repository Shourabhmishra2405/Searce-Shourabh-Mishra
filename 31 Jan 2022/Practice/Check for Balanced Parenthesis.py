# defining a function to check if both the parameters (a and b) provided to the function are same or not.
def isMatching(a,b):
    # checking for match in both the parameters
    if (a =='('and b==")") or (a =='{'and b=="}") or (a =='['and b=="]"):
        return True
    else:
        return False

def isBalanced(expr):
    # initialising and empty stack
    stack = []
    # iterating through each element in the string
    for x in expr:
        # Checkin if the element is an opening parenthesis if yes appending it to the stack else
        if x in ('(','{','['):
            stack.append(x)
        else:
            # if the parenthesis is not an opening parenthesis
            # if stack is empty return False
            if not stack:
                return False
            # if parenthesis is not matching to the peek element of stack return False
            elif isMatching(stack[-1],x) == False:
                return False
            # if the parenthesis is matching the peek element of stack pop the peek element of the stack
            else:
                stack.pop()
    # After iterating through each element in the parenthesis string if the stack has any element left return False otherwise return True
    if stack:
        return False
    else:
        return True

print(isBalanced('(([()]))'))