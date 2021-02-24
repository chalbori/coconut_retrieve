class Source_NP:
    def __init__(self):
        self.__object_id = None
        # self.__original_smiles = None
        # self.__simple_smiles = None
        # self.__original_inchi = None
        # self.__original_inchikey = None
        # self.__simple_inchi = None
        # self.__simple_inchikey = None
        self.__source = None
        self.__name = None
        self.__continent = None
        self.__organism_text = None

    def __repr__(self):
        return "<Chemical(object_id={object_id}, source={source}, name={name}, continent={continent}, organism_text={organism_text}>".format(
            object_id=self.__object_id,
            source=self.__source,
            name=self.__name,
            continent=self.__continent,
            organism_text=self.__organism_text,
        )
