from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("ResumenRD.pdf")  # Convierte el PDF a Markdown, tenes que escribir el nombre del archivo PDF que queres convertir, guardalo en la misma carpeta que este archivo main.py


with open("ResumenRD.md", "w", encoding="utf-8") as archivo: # Guarda el archivo, aqui volves a escribir el nombre del archivo que queres guardar, en este caso es ResumenRD.md
    archivo.write(result.text_content)

print("¡Ya se guardo el archivo maquina!")