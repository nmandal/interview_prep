# O(N) time | O(N) space
def balanced_brackets(string):
    openings = '([{'
    closings = ')]}'
    matching = {')': '(', ']': '[', '}': '{'}
    stack = []
    for char in string:
        if char in openings:
            stack.append(char)
        elif char in closings:
            if len(stack) == 0:
                return False
            if stack[-1] == matching[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0
