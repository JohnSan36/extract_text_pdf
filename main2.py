import json
#import re
from pypdf import PdfReader

def pdf_to_json(pdf_path):
  
    reader = PdfReader(pdf_path)

    paginas_capitulos = {
        8: "APRESENTAÇÃO",
        17: "É possível obter educação de qualidade padrão MIT sem ter frequentado o MIT?",
        42: "Por que o ultra-aprendizado é importante?",
        57: "Como se tornar um ultra-aprendiz",
        68: "Meta-aprendizagem",
        86: "Foco",
        105: "Prática direta",
        124: "Repetição",
        138: "Recuperação",
        153: "Retorno",
        171: "Retenção",
        195: "Intuição",
        216: "Experimentação",
        234: "Seu primeiro projeto de ultra-aprendizado",
        250: "Uma educação não convencional",
        275: "AGRADECIMENTOS"
    }

    textos_paginas = {}
    for i, page in enumerate(reader.pages):
        textos_paginas[i+1] = page.extract_text()

    # Dividir o texto em capítulos
    chapters = split_into_chapters(reader, textos_paginas, paginas_capitulos)

    # Criar um arquivo JSON para cada capítulo
    for i, chapter in enumerate(chapters):
        data = {
            "titulo": chapter['titulo'],
            "conteudo": chapter['conteudo']
        }
        with open(f"capitulo_{i+1}.json", "w") as f:
            json.dump(data, f, indent=4)

def split_into_chapters(reader, textos_paginas, paginas_capitulos):

    capitulos = list(paginas_capitulos.values())
    chapters = []

    # Páginas do sumário
    paginas = list(paginas_capitulos.keys())

    for i in range(len(capitulos) - 1):
        # Extrair o texto entre as páginas de início e fim do capítulo
        pagina_inicio = paginas[i]
        pagina_fim = paginas[i + 1]
        
        texto_capitulo = ""
        for j in range(pagina_inicio, pagina_fim):
            texto_capitulo += textos_paginas.get(j, "")
        
        chapters.append({
            'titulo': capitulos[i],
            'conteudo': texto_capitulo
        })

  
    ultimo_capitulo = capitulos[-1]
    pagina_ultimo_capitulo = paginas[-1]
    
    texto_ultimo_capitulo = ""
    for j in range(pagina_ultimo_capitulo, 277):
        texto_ultimo_capitulo += textos_paginas.get(j - 1, "")

    chapters.append({
        'titulo': ultimo_capitulo,
        'conteudo': texto_ultimo_capitulo
    })

    return chapters


pdf_to_json("ultra-aprendizado-ultralearning-scott-young.pdf")