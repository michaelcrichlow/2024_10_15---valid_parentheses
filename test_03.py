def valid_parentheses(s: str) -> bool:
    stack = []

    for val in s:
        if val == "(" or val == "[" or val == "{":
            stack.append(val)
        if val == ")" or val == "]" or val == "}":
            if len(stack) == 0:
                return False
        if stack and (val == ")" or val == "]" or val == "}"):
            if val == ")" and stack.pop() != "(":
                return False
            elif val == "]" and stack.pop() != "[":
                return False
            elif val == "}" and stack.pop() != "{":
                return False

    if len(stack) != 0:
        return False

    return True


def main() -> None:
    print(valid_parentheses("()[]{}"))
    print(valid_parentheses("((()))"))
    print(valid_parentheses("([{)}]"))
    print(valid_parentheses("((()"))
    print(valid_parentheses("(()[]{})"))


if __name__ == '__main__':
    main()
