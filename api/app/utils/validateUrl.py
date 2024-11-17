from pytube import YouTube  
from ..models.UrlModel import UrlModel, db

def is_valid_youtube_url(url):
    """Verifica se uma determinada URL é uma URL do YouTube válida."""
    try:
        video = YouTube(url)
        video.check_availability()
        return video
    except Exception as e:
        print(f"Erro ao validar a URL: {e}")
        return False