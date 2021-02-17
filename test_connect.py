from database.coconut import COCONUT

repo = COCONUT()
# print(repo.count())

i = 0
for np in repo.get_unique_stream():
    print(np)
    i = i + 1

    if i > 5:
        break
