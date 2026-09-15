from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("ResumenRD.pdf")  # Convierte el PDF a Markdown, tenes que escribir el nombre del archivo PDF que queres convertir


with open("ResumenRD.md", "w", encoding="utf-8") as archivo: # Guarda el archivo, aqui volves a escribir el nombre del archivo que queres guardar, en este caso es ResumenRD.md
    archivo.write(result.text_content)

print("¡Archivo guardado con éxito!")