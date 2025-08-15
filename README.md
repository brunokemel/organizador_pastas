📂 Organizador Automático de Arquivos

Este projeto é um script em Python que organiza automaticamente arquivos em uma pasta, separando-os por categorias como imagens, documentos, áudios, vídeos, programas e arquivos compactados.

🚀 Funcionalidades

Detecta automaticamente o diretório escolhido pelo usuário.

Identifica arquivos com base na extensão.

Cria pastas automaticamente para cada categoria, caso não existam.

Move os arquivos para suas respectivas pastas.

📋 Categorias Suportadas(pode alterar ou criar pastas para mais tipos de arquivos, apenas se atente manter o padrão do código e evitar erros)

Imagens: .png, .jpg, .jpeg, .gif

Documentos: .pdf, .docx, .txt, .xlsx

Áudios: .mp3, .wav, .aac

Vídeos: .mp4, .avi, .mkv

Programas: .exe, .msi, .dmg

Compactados: .zip, .rar, .tar, .gz

📦 Instalação e Uso

Certifique-se de ter o Python 3 instalado.

Salve o script como organizador.py.

Execute no terminal ou prompt de comando:

python organizador.py


Escolha a pasta que deseja organizar na janela que será aberta.

🛠 Tecnologias Utilizadas

Python 3

Tkinter (para selecionar pastas)

Módulo os (para manipulação de arquivos e diretórios)

⚠️ Observações

Certifique-se de ter permissão para modificar a pasta escolhida.

Arquivos com extensões não listadas não serão movidos.

Caso dois arquivos tenham o mesmo nome na pasta de destino, poderá ocorrer substituição.
