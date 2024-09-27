import pdfplumber

with pdfplumber.open('Jeruel.pdf') as archive:
    for pagina in archive.pages:
        print(pagina.extract_text())

