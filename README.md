# MIDIA DOWNLOAD - yt_dlp

Projeto simples em Python para baixar mídia diretamente pela URL usando a biblioteca `yt_dlp`
e criando interface usando a biblioteca do `streamlit`.

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

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/abaixador.git
cd abaixador
```

2. Instale as dependências:

```bash
pip install yt-dlp
```

3. Execute o script:

```bash
python link.py
```

## Como usar

Ao rodar o programa, você será solicitado a inserir a URL da mídia:

```bash
URL do video: https://www.instagram.com/reel/xxxxx/
```

O arquivo será baixado no mesmo diretório em que o script está sendo executado.

## Exemplo

```python
import yt_dlp


def baixar_video(url):
    config = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(config) as ydl:
        info = ydl.extract_info(url, download=False)
        filename = ydl.prepare_filename(info)
        print(f"Baixando: {filename}")
        ydl.download([url])
        return filename

link = input("URL do video:")
arquivo_baixado = baixar_video(link)
```

## Observações

- Nem todas as plataformas permitem download de conteúdo por política da própria plataforma.
- Algumas URLs podem exigir cookies ou outras configurações extras dependendo do site.
- Use este projeto apenas para fins legais e conforme os termos de uso dos serviços envolvidos.

## Licença

Este projeto está disponível para uso pessoal e educacional.
