#!/usr/bin/python3


"""
This module contains methods that enables the storage in
a file of objects, also reloads the objects store so they
can be used when opening the file again
"""


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
        to_save_dict = {}

        for key, value in FileStorage.__objects.items():
            to_save_dict[key] = value.to_dict()

        with open(f'{FileStorage.__file_path}', "w") as f:
            json.dump(to_save_dict, f)

    def reload(self):
        '''
        reads json file and deserialize it into dictionary of objects
        '''

        from models.base_model import BaseModel
        from models import user
        try:
            with open(self.__file_path, "r") as f:
                dict_of_dicts = json.load(f)
                for key, value in dict_of_dicts.items():
                    class_list = key.split('.')
                    class_name = class_list[0]
                    new_object = eval(class_name)(**value)
                    FileStorage.__objects[key] = new_object
        except Exception as e:
            pass
