import os

from tkinter.filedialog import askdirectory

caminho = askdirectory(title='Selecione a pasta pasta')

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "audios": [".mp3", ".wav", ".aac"],
    "videos": [".mp4", ".avi", ".mkv"],
    "programas": [".exe", ".msi", ".dmg"],
    "zips": [".zip", ".rar", ".tar", ".gz"],
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.makedirs(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")