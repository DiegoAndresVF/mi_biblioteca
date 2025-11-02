biblioteca = []

biblioteca.append({"titulo": "Cuentos de amor de locura y de muerte", "autor": "Horacio Quiroga", "anio": 1917})
biblioteca.append({"titulo": "Carrie","autor": "Stephen King","anio": 1974})
biblioteca.append({"titulo": "1984","autor": "George Orwell","anio": 1949})

print("=== Mis libros ===")
for i, libro in enumerate(biblioteca, start=1):
    print(f"{i}. {libro['titulo']} - {libro['autor']} - {libro['anio']} ")

categoria = ("Ficción", "Historia", "Ciencia","Novela","Biográfica")
print("\nCategoría: ", categoria)

opcion = input("\n ¿Quieres agregar un nuevo libro? (s/n)").lower()

if opcion == "s":
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = input("Año: ")

    nuevo_libro= {
            "titulo": titulo,
            "autor": autor,
            "anio": anio
        }
    biblioteca.append(nuevo_libro)
    print("\n Libro agrego con éxito!")


print("=== Mis libros ===")
for i, libro in enumerate(biblioteca, start=1):
    print(f"{i}. {libro['titulo']} - {libro['autor']} - {libro['anio']} ")