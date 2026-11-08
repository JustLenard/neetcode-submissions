class Solution:
    def isValid(self, s: str) -> bool:
        # Rules:
        # 1. Must not start with a close paranth
        # 2. Close paranth is allowed only if: 
        # prev paranth is opening and of the same kind

        # Create stack
        # if is first paranth is cloning -> early return
        # add paranth to stack if opening 
        # remove from stack if corect paranth
        # return stack empty

        paranths_pairs ={
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        if s[0] not in paranths_pairs:
            return False

        stack = []

        for paranth in s:
            # If paranth is opening
            if paranth in paranths_pairs:
                stack.append(paranth)
            else:
                # If last parant in stack matches with this one
                if len(stack) > 0 and paranths_pairs[stack[-1]] == paranth:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0