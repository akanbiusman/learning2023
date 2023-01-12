import re

result = re.search(r"Py.*n", "Pygmalion").span()
print(result)

