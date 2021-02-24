from database.coconut import COCONUT
from data.unique_np import Unique_NP
from pprint import pprint
from rdkit import Chem
from rdkit.Chem import inchi

repo = COCONUT()
# print(repo.count())
i = 0
converted, not_converted = 0, 0

converted_list_file = open(
    "out/inchi_valid_check/converted.txt", mode="w", encoding="utf-8"
)
converted_not_match_file = open(
    "out/inchi_valid_check/converted_not_match.txt", mode="w", encoding="utf-8"
)
np: Unique_NP
for np in repo.get_unique_stream():
    try:
        mol = Chem.MolFromInchi(inchi=np.inchi, treatWarningAsError=True)
    except:
        not_converted += 1

    if mol:
        mol_inchikey = inchi.MolToInchiKey(mol)

        if np.inchikey == mol_inchikey:
            converted_list_file.write(np.inchi + "\n")
            converted += 1
        else:
            converted_not_match_file.write(np.inchi + "\n")
            not_converted += 1
    i += 1

    if i % 10000 == 0:
        print("{}th checked".format(i))

print("converted:", converted, "not converted:", not_converted)
converted_list_file.close()
converted_not_match_file.close()
