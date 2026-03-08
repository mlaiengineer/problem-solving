from parenthesis_checker import Solution

def run_tests():
    sol = Solution()

    # --- Given Examples (from problem statement) ---
    assert sol.isBalanced("[{()}]")  == True,  "Test 1 Failed: simple nested valid"
    assert sol.isBalanced("[()()]{}") == True,  "Test 2 Failed: multiple valid groups"
    assert sol.isBalanced("([{")     == False, "Test 3 Failed: missing closing brackets"
    assert sol.isBalanced("([{]})")  == False, "Test 4 Failed: wrong closing order"

    # --- Edge Cases ---
    # Single unmatched opener — stack never empties
    assert sol.isBalanced("(")       == False, "Test 5 Failed: single opener"

    # Single unmatched closer — stack is empty on first check
    assert sol.isBalanced(")")       == False, "Test 6 Failed: single closer"

    # Correct order matters; same brackets but reversed closing
    assert sol.isBalanced("([)]")    == False, "Test 7 Failed: interleaved wrong order"

    # All three types valid side by side
    assert sol.isBalanced("(){}[]")  == True,  "Test 8 Failed: all types sequential"

    # Deeply nested — every level must close in reverse order
    assert sol.isBalanced("({[({[]})]})") == True,  "Test 9 Failed: deep nesting"

    # Closer with no opener at all
    assert sol.isBalanced("]")       == False, "Test 10 Failed: lone closer"

    # Large balanced input — stress tests performance at scale
    assert sol.isBalanced("()[]{}" * 1000) == True, "Test 11 Failed: large valid input"

    # Looks balanced but has extra opener at the end
    assert sol.isBalanced("()((")   == False, "Test 12 Failed: trailing unmatched openers"

    print("✅ Passed all 12 test cases!")

if __name__ == "__main__":
    run_tests()