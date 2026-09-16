import yt_dlp

def baixar_video(url):
    config = {
        'format': 'best', # Pega o melhor vídeo + áudio juntos
        'outtmpl': '%(title)s.%(ext)s', # Salva com o nome do vídeo
    }
    
    with yt_dlp.YoutubeDL(config) as ydl:
        # Primeiro, extrai as informações para obter o nome do arquivo
        info = ydl.extract_info(url, download=False)
        filename = ydl.prepare_filename(info)
        print(f"Baixando: {filename}")
        
        # Agora baixa
        ydl.download([url])
        
        return filename

# Uso:
link = input("URL do video:")
arquivo_baixado = baixar_video(link)