from database.coconut import COCONUT

repo = COCONUT()

source_organism_set = repo.get_organism_list()
# source_organism_dict = repo.get_organism_statistics()
print("len: {}".format(len(source_organism_set)))
print("type: {}".format(type(source_organism_set)))

with open("out/source_organism_set.txt", mode="w", encoding="utf-8") as fs:
    for line in source_organism_set:
        fs.write(line + "\n")

print("organism set written")

i = 0
with open("out/source_organism_dict.txt", mode="w", encoding="utf-8") as fd:
    for organism_text, count in repo.get_organism_statistics_stream(
        source_organism_set
    ):
        print(organism_text,str(count))
        fd.write(organism_text + "\t" + str(count) + "\n")

print("organism set statistics written")

# for organism, count in repo.get_organism_statistics_stream(source_organism_set):
#     print(organism, count)