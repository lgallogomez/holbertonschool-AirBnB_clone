#!/usr/bin/python3

import json

class FileStorage():
    '''
    class stores objects into a json file and puts 
    json file info into objects
    '''
    __file_path = "File.json"
    __objects = dict()


    def all(self):
        '''
        returns dictionary __objects
        '''
        return self.__objects
    
    def new(self, obj):
        '''
        sets in __ojects dict of objects key and value
        '''
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj
    
    def save(self):
        '''
        serializes objects in __objects into a json
        '''
        with open("self.__file_path", "w") as f:
             j_string = json.dumps(self.__objects)
             f.write(j_string)
    
    def reload(self):
        '''
        reads json file and deserialize it into dictionary of objects
        '''
        try:
            with open("self.__file_path", "r") as f:
                read_str = f.read()
                self.__objects = json.loads(read_str)
        except Exception as e:
            pass
