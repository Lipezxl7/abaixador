# MIDIA DOWNLOAD - yt_dlp

Projeto simples em Python para baixar mídia diretamente pela URL usando a biblioteca `yt_dlp`.

Ele foi pensado para facilitar o download de conteúdos de plataformas como:

- Instagram Reels e posts
- Vídeos do TikTok
- Imagens do Pinterest
- Lives e vídeos da Twitch
- Outros sites suportados pelo `yt_dlp`

## Funcionalidades

- Download de mídia apenas com a URL
- Extração automática do nome do arquivo
- Salva o conteúdo no diretório atual do projeto
- Interface simples via terminal

## Requisitos

- Python 3.8+
- Biblioteca `yt_dlp`

## Instalação

1. Instale as dependências:

```bash
pip install yt-dlp
```

2. Execute o script:

```bash
python link.py
```

## Como usar

Ao rodar o programa, você será solicitado a inserir a URL da mídia:

```bash
URL do video: https://www.instagram.com/reel/xxxxx/
```

O arquivo será baixado no mesmo diretório em que o script está sendo executado.
