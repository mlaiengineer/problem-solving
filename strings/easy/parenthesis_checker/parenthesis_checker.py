class Solution:
    def isBalanced(self, s: str) -> bool:

        # Maps closing → opening; avoids multiple if-checks per bracket type
        matching_bracket = {')': '(', '}': '{', ']': '['}

        # Stack tracks unmatched opening brackets in order
        stack = []

        for bracket in s:
            if bracket in '({[':
                # Push opening brackets to wait for their matching close
                stack.append(bracket)

            elif bracket in matching_bracket:
                # Top must match expected opener; order & type enforced here
                if not stack or stack[-1] != matching_bracket[bracket]:
                    return False
                stack.pop()

        # Unmatched openers remaining means expression is incomplete
        return len(stack) == 0