



import re

text = """asdasdsadasdasd
"""

start_pattern = "start"
end_pattern = "end"

start_index = re.search(start_pattern, text).end()
end_index = re.search(end_pattern, text).start()

result = text[start_index:end_index].strip()
print(result)



