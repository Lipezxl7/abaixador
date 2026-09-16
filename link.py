import os
import streamlit as st
import yt_dlp

def baixar_video(url):
    pasta = os.getcwd()

    config = {
        'format': 'best',
        'outtmpl': os.path.join(pasta, '%(title)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(config) as ydl:
        info = ydl.extract_info(url, download=False)
        filename = ydl.prepare_filename(info)
        ydl.download([url])
        return filename

# Usando streamlit para criar a interface do usuário

st.title("Midia Downloader")
st.write("Cole a URL do vídeo ou da midia que deseja baixar.")

url = st.text_input("URL")

if st.button("Baixar"):
    if url:
        with st.spinner("Baixando..."):
            try:
                arquivo = baixar_video(url)
                st.success(f"Download concluído (salvo na pasta do script): {arquivo}")
            except Exception as erro:
                st.error(f"Erro ao baixar: {erro}")
    else:
        st.warning("Digite uma URL antes de baixar.")