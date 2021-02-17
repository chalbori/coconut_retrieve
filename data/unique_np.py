class Unique_NP:
    def __init__(self):
        self.__id = None
        self.__coconut_id = None
        self.__inchi = None
        self.__inchikey = None

    def __repr__(self):
        return "<Chemical(id={id}, coconut_id={coconut_id}, inchi={inchi}, inchikey={inchikey})>".format(
            id=self.__id,
            coconut_id=self.__coconut_id,
            inchi=self.__inchi,
            inchikey=self.__inchikey,
        )

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
