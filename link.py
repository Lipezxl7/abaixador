import yt_dlp
from enviando import enviar_na_raca

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
link = input("Cole o link (YT, TikTok ou Insta): ")
arquivo_baixado = baixar_video(link)

# Agora envia pro WhatsApp
numero_destino = input("Digite o número do WhatsApp (com código do país, ex: 5511999999999): ")
enviar_na_raca(arquivo_baixado, numero_destino)