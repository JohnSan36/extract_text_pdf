from PyPDF2 import PdfReader

def pdf_to_txt(pdf_path, txt_path):

    reader = PdfReader(pdf_path)

    text = ""
    for page in reader.pages:
        text += page.extract_text()

    with open(txt_path, "w") as f:
        f.write(text)

# Exemplo de uso
pdf_to_txt("Elon Musk - Como o CEO bilionário - Ashlee Vance.pdf", "conteudo.txt")