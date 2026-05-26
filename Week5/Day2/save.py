def save_ints(data):
    for item in data:
        try:
            yield int(item)
        except ValueError:
            continue

data = ["10", "abc", "20", "30"]

for x in save_ints(data):
    print(x)