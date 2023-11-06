class FileStorage():
    """
    __file_path: stores the jason file
    __objects: empty dict to store a BaseModel object. 
    keys with following format: <class name>.id ex:BaseModel.12121212
    where 12121212 is the id and BaseModel is the class
    """
    __file_path = "file.json"
    __objects = dict()

    def __init__(self):
        pass

    def all(self):
        return (self.__objects)

    def new(self, obj):
        print(self.__objects)
        key = "{0}.{1}".format(obj.__class__.__name__, obj.id)
        print(key)
        print(obj)
        self.__objects[key] = obj
        print(self.__objects)
  
    def save(self):
        pass

    def reload(self):
        pass

file = FileStorage()
file.new()