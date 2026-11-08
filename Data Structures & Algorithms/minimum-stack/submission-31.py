from copy import deepcopy

class MinStack:
    def __init__(self):
        self.min_value = None
        self.stack = []
        self.internal_data = {
            0 : {
                "min_value" : None,
                "stack" : []
            }
        }

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_value == None:
            self.min_value = val
        else:
            self.min_value = min(self.min_value, val)

        self.min_value = min(self.min_value, val)
        stack_copy = self.stack.copy()

        self.internal_data[len(stack_copy)] = {"stack": stack_copy, "min_value": self.min_value}

    def pop(self) -> None:
        idx = len(self.stack)
        del self.internal_data[idx]
        prev_data = self.internal_data[idx - 1]
        self.stack = prev_data["stack"].copy()
        self.min_value = prev_data["min_value"]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value