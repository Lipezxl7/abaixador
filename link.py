import base64
import os
import tempfile
from pathlib import Path
from urllib.parse import urlparse

import streamlit as st
import streamlit.components.v1 as components
import yt_dlp


def identificar_plataforma(url):
    host = urlparse(url).netloc.lower()

    if 'youtube.com' in host or 'youtu.be' in host or 'youtube-nocookie.com' in host:
        return 'YouTube'
    if 'instagram.com' in host:
        return 'Instagram'
    if 'tiktok.com' in host:
        return 'TikTok'
    if 'pinterest.com' in host:
        return 'Pinterest'
    if 'twitch.tv' in host:
        return 'Twitch'
    if 'twitter.com' in host or 'x.com' in host:
        return 'Twitter/X'
    return 'Outra plataforma'


def obter_titulo(url):
    opts = {
        'quiet': True,
        'no_warnings': True,
        'skip_download': True,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info.get('title', 'Título não encontrado')


def baixar_video_para_tempo(url):
    pasta_temp = tempfile.gettempdir()

    config = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(pasta_temp, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'no_warnings': True,
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(config) as ydl:
        info = ydl.extract_info(url, download=False)
        nome_arquivo = ydl.prepare_filename(info)
        ydl.download([url])
        return Path(nome_arquivo)


def gerar_html_download(nome_arquivo, dados_arquivo):
    base64_data = base64.b64encode(dados_arquivo).decode('utf-8')
    return f'''
        <a id="download-link" href="data:application/octet-stream;base64,{base64_data}" download="{nome_arquivo}" style="display:none"></a>
        <script>
            document.getElementById('download-link').click();
        </script>
    '''


st.title("Midia Downloader")
st.write("Cole a URL para baixar.")

url = st.text_input("URL")

if st.button("Baixar"):
    if not url:
        st.warning("Digite uma URL antes de baixar.")
        st.stop()

    try:
        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            st.error("URL inválida. Verifique se a URL foi colada corretamente.")
            st.stop()

        plataforma = identificar_plataforma(url)

        with st.spinner("Identificando a mídia..."):
            titulo = obter_titulo(url)

        st.info(f"Plataforma: {plataforma} | Título: {titulo}")

        if plataforma == 'YouTube':
            st.error(
                "Não é possível baixar vídeos do YouTube neste deploy. "
                "O YouTube bloqueia esse tipo de uso no ambiente de hospedagem e o download não funciona aqui. "
                "Use outras plataformas como Instagram, TikTok, Pinterest ou Twitch."
            )
            st.stop()

        with st.spinner("Baixando..."):
            try:
                arquivo = baixar_video_para_tempo(url)

                if arquivo.exists():
                    with open(arquivo, 'rb') as file:
                        dados = file.read()

                    components.html(
                        gerar_html_download(arquivo.name, dados),
                        height=0,
                    )

                    st.success("Download iniciado no navegador.")
            except Exception as erro:
                st.error("Não foi possível baixar esse link no momento. Verifique a URL ou a plataforma.")
                st.caption(str(erro))

    except Exception as erro:
        st.error("Não foi possível processar essa URL.")
        st.caption(str(erro))