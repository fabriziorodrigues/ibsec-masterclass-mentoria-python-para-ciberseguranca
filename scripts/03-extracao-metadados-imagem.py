from PIL import Image
from PIL.ExifTags import TAGS
import exifread

def extrair_metadados_imagem(caminho_arquivo):
    # Abrir a imagem e extrair os metadados
    imagem = Image.open(caminho_arquivo)
    metadados = imagem._getexif()

    # Dicionário para armazenar os metadados extraídos
    metadados_extraiidos = {}

    # Iterar sobre os metadados e adicionar ao dicionário
    if metadados:
        for tag_id, valor in metadados.items():
            tag = TAGS.get(tag_id, tag_id)
            metadados_extraiidos[tag] = valor

    return metadados_extraiidos

# Caminho do arquivo de imagem
caminho_imagem = 'caminho_para_sua_imagem.jpg'

# Chamando a função e exibindo os metadados
metadados = extrair_metadados_imagem(caminho_imagem)
for tag, valor in metadados.items():
    print(f"{tag}: {valor}")
