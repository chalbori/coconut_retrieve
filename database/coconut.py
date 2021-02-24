from pymongo import MongoClient
from database.auth import Database
from data.unique_np import Unique_NP


class COCONUT:
    def __init__(self):
        self.client = MongoClient(Database.connection_info)
        self.database_list = self.client.list_database_names()
        self.db = self.client["COCONUT"]
        self.quarantined_collec = self.db["quarantined"]
        self.source_np_collection = self.db["sourceNaturalProduct"]
        self.unique_np_collection = self.db["uniqueNaturalProduct"]

    # db = client.get_default_database()
    # assert db.name == "COCONUT"

    def get_database_list(self):
        return self.client.list_database_names()

    def count(self):
        result = dict()
        result["quarantined"] = self.quarantined_collec.count_documents({})
        result["sourceNaturalProduct"] = self.source_np_collection.count_documents({})
        result["uniqueNaturalProduct"] = self.unique_np_collection.count_documents({})
        return result

    def get_unique_stream(self)->Unique_NP:
        stream = self.unique_np_collection.find(
            {}, {"_id": 1, "coconut_id": 1, "inchi": 1, "inchikey": 1}
        )
        # stream = self.unique_np_collection.find({})
        for doc in stream:
            result = Unique_NP()
            result.id = doc["_id"]
            result.coconut_id = doc["coconut_id"]
            result.inchi = doc["inchi"]
            result.inchikey = doc["inchikey"]
            yield result

    def get_unique_source_set(self) -> list:
        return self.source_np_collection.distinct("source")
    
    def get_count_source(self, source) -> int:
        return self.source_np_collection.count_documents({"source":source})

    def get_unique_source_statistics(self) -> dict:
        result = dict()
        source_set = self.get_unique_source_set()
        for source in source_set:
            result[source]=self.get_count_source(source=source)
        return result
       
    def get_source_organism_set(self) -> list:
        return self.source_np_collection.distinct("organismText")
        
    def get_source_organism_statistics(self) -> dict:
        pass
# print(db)
# print(db.list_collection_names())

# # pprint.pprint(db.quarantined.find_one({'coconut_id':'CNP0074823'}))
# # pprint.pprint(collection.find_one({'coconut_id':'CNP0074823'}))

# # for doc in collection.find():
# #     pprint.pprint(doc)

# print("quarantined:",collection.count_documents({}))
# print("sourceNaturalProduct:", db.sourceNaturalProduct.count_documents({}))
# print("uniqueNaturalProduct:",db.uniqueNaturalProduct.count_documents({}))
