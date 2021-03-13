class Source_NP:
    def __init__(
        self, object_id=None, source=None, name=None, continent=None, organism_text=None
    ):
        # self.__object_id = None
        # self.__source = None
        # self.__name = None
        # self.__continent = None
        # self.__organism_text = None

        self.__object_id = object_id
        self.__source = source
        self.__name = name
        self.__continent = continent
        self.__organism_text = organism_text

    def __repr__(self):
        return "<Chemical(object_id={object_id}, source={source}, name={name}, continent={continent}, organism_text={organism_text}>".format(
            object_id=self.__object_id,
            source=self.__source,
            name=self.__name,
            continent=self.__continent,
            organism_text=self.__organism_text,
        )

    @property
    def object_id(self):
        return self.__object_id

    @object_id.setter
    def object_id(self, object_id):
        self.__object_id = object_id

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source):
        self.__source = source

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def continent(self):
        return self.__continent

    @continent.setter
    def continent(self, continent):
        self.__continent = continent

    @property
    def organism_text(self):
        return self.__organism_text

    @organism_text.setter
    def organism_text(self, organism_text):
        self.__organism_text = organism_text
