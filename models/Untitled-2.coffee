{
key : value
receta 1 : hamburguesa
receta 2 : pasta
}

{
    diccionario 1 : {
                       receta 1 : hamburguesa
                       receta 2 : pasta
                    } 
    
    diccionario 2 : {
                        receta 1 : pizza
                        receta 2 : ravioli

                    }
}


{
    objeto 1 : models.base_model.BaseModel object at memdir
    objeto 2 : models.base_model.BaseModel object at memdir2
}

cuando lo tengo en el archivo json - cuando lo serializamos. 



dicti = {
    'BaseModel.44c666c0-79b1-47fd-95d6-e40f9f7e3d2e' : {'id': '44c666c0-79b1-47fd-95d6-e40f9f7e3d2e', 'created_at': '2023-11-11T13:18:14.919540', 'updated_at': '2023-11-11T13:18:14.919606', 'name': 'My_First_Model', 'my_number': 89, '__class__': 'BaseModel'}

    'BaseModel.555554c666c0-79b1-47fd-95d6-e40f9f7e3d2e' : {'id': '555554c666c0-79b1-47fd-95d6-e40f9f7e3d2e', 'created_at': '2023-11-11T13:18:14.919540', 'updated_at': '2023-11-11T13:18:14.919606', 'name': 'My_First_Model', 'my_number': 89, '__class__': 'BaseModel'}
        }    

new_dict = {}
for key, value in dicti.items():
            new_dict[key] = value



cuando lo deserializamos?
{
    'BaseModel.8e26c0ee-b9d3-4f4f-a279-3790335503a9' : <models.base_model.BaseModel object at 0x7f8601e41c60>
    #llave sirve para 
}



class BaseModel

new_oject = BaseModel()

new_oject.name = "sam"
new_oject.last_name = Calderon
new_oject.age = 24
print(new_oject.__dict__())
dicti = {}
dicti[f'{new_object.__class__.__name__}.{new_object.id}']
{name : 'sam', last_name : "calderon", age : 24}

dicti[[f'{new_object.__class__.__name__}.{new_object.id}']] = new_object.__dict__()
