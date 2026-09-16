import base64
import os
import tempfile
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components
import yt_dlp


def baixar_video_para_tempo(url):
    pasta_temp = tempfile.gettempdir()

    config = {
        'format': 'bv*+ba/b',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(pasta_temp, '%(title)s.%(ext)s'),
        'noplaylist': True,
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
    if url:
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
                st.error(f"Erro ao baixar: {erro}")
    else:
        st.warning("Digite uma URL antes de baixar.")