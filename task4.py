# Дана строка X, состоящая только из символов “{“, “}”, “[“, “]”, “(“, “)”.
# Программа должна вывести True, в том случае если все открытые скобки закрыты.
# Например: “[()]{}”, все открытые скобки закрыты закрывающимися скобками,
# потому вывод будет True. В случае же, если строка будет похожа на: “{{{}”,
# то вывод будет False, т.к. не все открытые скобки закрыты.
#
# Пример 1:
# Ввод: x = “[{}({})]”
# Вывод: True
#
# Пример 2:
# Ввод: x = “{]”
# Вывод: False
#
# Пример 3:
# Ввод: x = “{“
# Вывод: False
# Гарантируется, что введенная строка X будет содержать только скобки и не будет пустой.

def is_balanced(text, brackets="〈〉()[]{}"):
    opening, closing = brackets[::2], brackets[1::2]
    stack = [] # keep track of opening brackets types
    for character in text:
        if character in opening: # bracket
            stack.append(opening.index(character))
        elif character in closing: # bracket
            if stack and stack[-1] == closing.index(character):
                stack.pop()  # remove the matched pair
            else:
                return False # unbalanced (no corresponding opening bracket) or
                             # unmatched (different type) closing bracket
    return (not stack) # no unbalanced brackets

print(is_balanced(input()))
