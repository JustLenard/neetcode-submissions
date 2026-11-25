class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        def get_nums() -> tuple[int, int]:
            return (stack.pop(), stack.pop())

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                if token == "+":
                    first_num, second_num = get_nums()
                    stack.append(second_num + first_num)

                if token == "-":
                    first_num, second_num = get_nums()
                    stack.append(second_num - first_num)
                if token == "*":
                    first_num, second_num = get_nums()
                    stack.append(second_num * first_num)
                if token == "/":
                    first_num, second_num = get_nums()
                    stack.append(int(second_num / first_num))

        return stack[0]