
class Solution:
    def dailyTemperatures(self, temps: list[int]) -> list[int]:
        response = [0] * len(temps)
        temp_stack = []

        for i, current_temp in enumerate(temps):
            # Edgecases
            if i == 0:
                temp_stack.append((i, current_temp))
            if i == len(temps) - 1:
                pass

            # Handle scenarios
            while temp_stack and current_temp > temp_stack[-1][1]:
                last_temp_index_in_stack = temp_stack[-1][0]

                response[last_temp_index_in_stack] = i - last_temp_index_in_stack
                temp_stack.pop()

            temp_stack.append((i, current_temp))

        return response
