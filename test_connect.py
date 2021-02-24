from database.coconut import COCONUT
from data import source_np
from pprint import pprint

repo = COCONUT()
# print(repo.count())

i = 0
for np in repo.get_unique_stream():
    print(np)

    i = i + 1

    if i > 5:
        break

# print(repo.get_count_source(source="gnps"))
# print(repo.get_unique_source_statistics())

print(repo.get_source_organism_set())