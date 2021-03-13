class Unique_NP:
    def __init__(self, object_id=None, coconut_id=None, inchi=None, inchikey=None):
        self.__object_id = object_id
        self.__coconut_id = coconut_id
        self.__inchi = inchi
        self.__inchikey = inchikey

    def __repr__(self):
        return "<Chemical(object_id={object_id}, coconut_id={coconut_id}, inchi={inchi}, inchikey={inchikey})>".format(
            object_id=self.__object_id,
            coconut_id=self.__coconut_id,
            inchi=self.__inchi,
            inchikey=self.__inchikey,
        )

    def __iter__(self):
        return self

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def coconut_id(self):
        return self.__coconut_id

    @coconut_id.setter
    def coconut_id(self, coconut_id):
        self.__coconut_id = coconut_id

    @property
    def inchi(self):
        return self.__inchi

    @inchi.setter
    def inchi(self, inchi):
        self.__inchi = inchi

    @property
    def inchikey(self):
        return self.__inchikey

    @inchikey.setter
    def inchikey(self, inchikey):
        self.__inchikey = inchikey
