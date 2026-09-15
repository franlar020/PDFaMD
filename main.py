from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("ResumenRD.pdf")


with open("ResumenRD.md", "w", encoding="utf-8") as archivo:
    archivo.write(result.text_content)

print("¡Archivo guardado con éxito!")