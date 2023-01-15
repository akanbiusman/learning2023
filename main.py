import re

def re_items(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result is None:
        return name
    print(result)
    return f"{result[2]}, {result[1]}"


print(re_items("Lovelace, Ada"))
print(re_items("Akanbi, Usman O."))
