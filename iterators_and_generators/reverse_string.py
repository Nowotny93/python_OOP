def reverse_text(text):

    idx = len(text) - 1
    limit = 0
    while idx >= limit:
        yield text[idx]
        idx -= 1

for char in reverse_text("step"):
    print(char, end="")