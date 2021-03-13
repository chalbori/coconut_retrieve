from pprint import pprint
from data.source_np import Source_NP
from pymongo import MongoClient
from database.auth import Database
from data.unique_np import Unique_NP
from bson.objectid import ObjectId


class COCONUT:
    def __init__(self):
        self.client = MongoClient(Database.connection_info)
        self.database_list = self.client.list_database_names()
        # self.db = self.client["COCONUT"]
        self.db = self.client[Database.database]
        self.quarantined_collec = self.db["quarantined"]
        self.source_np_collection = self.db["sourceNaturalProduct"]
        self.unique_np_collection = self.db["uniqueNaturalProduct"]

    def __del__(self):
        self.client.close()

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
    
    def get_unique_stream(self):
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

    def get_unique_np(self, object_id):
        doc = self.unique_np_collection.find_one({"_id": ObjectId(object_id)})
        return Unique_NP(
            object_id=doc["_id"],
            coconut_id=doc["coconut_id"],
            inchi=doc["inchi"],
            inchikey=doc["inchikey"],
        )

    def get_source_np(self, object_id):
        doc = self.source_np_collection.find_one({"_id": ObjectId(object_id)})
        result = Source_NP(
            object_id=doc["_id"],
            source=doc["source"],
            name=doc["name"],
            continent=doc["continent"],
            organism_text=doc["organismText"],
        )
        return result

    def get_unique_source_list(self) -> list:
        return self.source_np_collection.distinct("source")

    def get_count_source(self, source) -> int:
        return self.source_np_collection.count_documents({"source": source})

    def get_count_organism(self, organism_text) -> int:
        return self.source_np_collection.count_documents({"organismText": organism_text})

    def get_unique_source_statistics(self) -> dict:
        result = dict()
        source_list = self.get_unique_source_list()
        for source in source_list:
            result[source] = self.get_count_source(source=source)
        return result

    def get_organism_list(self) -> list:
        return self.source_np_collection.distinct("organismText")

    def get_organism_statistics_stream(self, organism_set):
        for organism_text in organism_set:
            yield organism_text, self.get_count_organism(organism_text=organism_text)


# print(db)
# print(db.list_collection_names())

# # pprint.pprint(db.quarantined.find_one({'coconut_id':'CNP0074823'}))
# # pprint.pprint(collection.find_one({'coconut_id':'CNP0074823'}))

# # for doc in collection.find():
# #     pprint.pprint(doc)

# print("quarantined:",collection.count_documents({}))
# print("sourceNaturalProduct:", db.sourceNaturalProduct.count_documents({}))
# print("uniqueNaturalProduct:",db.uniqueNaturalProduct.count_documents({}))
