<<<<<<< HEAD
#!/usr/bin/python3

from models.engine.file_storage import FileStorage

storage = FileStorage()
=======
storage = __import__('FileStorage').FileStorage
>>>>>>> 240ed285581b939eccaded472388ed8c7d347a5e

storage.reload()
