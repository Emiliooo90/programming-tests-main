class SQL:
    seq = 0
    
    #Se crea esta variable para almacenar los libros
    database = {}

    def create(self, table_name="books", *args, **kwargs):
        print("Creando registro nuevo")
        print(table_name)
        print(args)
        print(kwargs)
        SQL.seq += 1
        record_id = SQL.seq
        SQL.database.setdefault(table_name, {})[record_id] = kwargs
        return record_id

    def update(self, record_id, table_name="books", *args, **kwargs):
        print(f"Actualizando {table_name} con id: {record_id}")
        print(f"Valores: {args}")
        print(kwargs)
        SQL.database.setdefault(table_name, {})[record_id].update(kwargs)

    def list(self, table_name="books"):
        print(f"Lista de {table_name}")
        return SQL.database.get(table_name, {})

    def retrieve(self, record_id, table_name="books"):
        print(f"Se obtiene {record_id} desde {table_name}")
        return SQL.database.get(table_name, {}).get(record_id, None)

    def delete(self, record_id, table_name="books"):
        print(f"Se eliminó {record_id} desde {table_name}")
        if table_name in SQL.database and record_id in SQL.database[table_name]:
            del SQL.database[table_name][record_id]


class Book:
    def __init__(self, nombre: str, autor: str = None, num_paginas: int = None):
        self.id = None
        self.nombre = nombre
        self.autor = autor
        self.num_paginas = num_paginas
    
    #Función para guardar los libros
    def save(self):
        if self.id is None:
            self.id = SQL().create(nombre=self.nombre, autor=self.autor, num_paginas=self.num_paginas)
        else:
            SQL().update(record_id=self.id, nombre=self.nombre, autor=self.autor, num_paginas=self.num_paginas)
    
    #Función para listar todos los libros
    @staticmethod
    def list_books():
        return SQL().list(table_name="books")
    
    #Función para obtener un libro por su id
    @staticmethod
    def get_book(record_id: int):
        return SQL().retrieve(record_id)
    
    #Función para eliminar un libro por su id
    def delete(self):
        if self.id is not None:
            SQL().delete(record_id=self.id)
            self.id = None


# Ejemplo de uso
libro = Book(nombre="Harry Potter y la piedra filosofal", autor="J.K. Rowling", num_paginas=300)
libro2 = Book(nombre="El programador prágmatico (Edición especial)", autor="Andy Hunt y Dave Thomas", num_paginas=100)
libro3 = Book(nombre="La teoría del todo", autor="Stephen Hawking", num_paginas=500)
libro4 = Book(nombre="Padre rico, Padre pobre", autor="Robert T. Kiyosaki", num_paginas=230)
libro5 = Book(nombre="De animales a dioses", autor="Yuval Noah Harari", num_paginas=300)

#Se guardan los libros
libro.save()
libro2.save()
libro3.save()
libro4.save()
libro5.save()

#Se actualiza el libro 1
libro.nombre = "Los juegos del hambre"
libro.autor = "Suzanne Collins"
libro.num_paginas = 500
libro.save()

#Se elimina el libro 1
libro.delete()

#Se listan todos los libros
print(Book.list_books())

#Se obtiene un libro por su id
print(Book.get_book(record_id=3))

