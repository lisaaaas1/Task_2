#проверка скобок
def check(text):
    brackets = []
    for i in text:
        if i == "[" or i == "]" or i == "(" or i == ")" or i == "{" or i == "}" or i == "<" or i == ">":
            brackets.append(i)

    if brackets.count("[") == brackets.count("]") and brackets.count("(") == brackets.count(")") and brackets.count(
            "{") == brackets.count("}"):

        try:
            j = 0
            while j != range(len(brackets)):
                if brackets[j] == "(" and brackets[j + 1] == ")":
                    brackets.pop(j)
                    brackets.pop(j)
                    j = 0
                elif brackets[j] == "{" and brackets[j + 1] == "}":
                    brackets.pop(j)
                    brackets.pop(j)
                    j = 0
                elif brackets[j] == "[" and brackets[j + 1] == "]":
                    brackets.pop(j)
                    brackets.pop(j)
                    j = 0
                else:
                    j += 1
        except:
            if (len(brackets)) == 0:
                return True
            else:
                return False
    else:
        return False

v = input('Выражение ')
print(check(v))
