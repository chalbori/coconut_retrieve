from database.coconut import COCONUT
from data.source_np import Source_NP
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

source_np = repo.get_source_np(object_id="5f945fc5ae0c19564521a3a1")
print(type(source_np.organism_text))
