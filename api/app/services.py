from pytube import YouTube  
from app.models import UrlModel, db

def is_valid_youtube_url(url, proxies=None):
    """Verifica se uma determinada URL é uma URL do YouTube válida."""
    try:
        video = YouTube(url, proxies=proxies)
        video.check_availability()
        return video
    except Exception as e:
        print(f"Erro ao validar a URL: {e}")
        return False

def add_url_info(urlInfo):
    print(urlInfo)
    """Adiciona um novo URL, se for válido."""
    try:
        if not urlInfo:
            return {"success": False, "message": "URL do YouTube inválida", "status": 400}
        
        newUrlInfo = UrlModel(
            watch_url=urlInfo
        )

        db.session.add(newUrlInfo)
        db.session.commit()

        return {
            "success": True,
            "data": {"id": newUrlInfo.id, **{key: value for key, value in newUrlInfo.__dict__.items() if not key.startswith('_')}},
            "status": 200
        }
    except Exception as e:
        print(f"Erro ao adicionar o URL ao banco: {e}")
        return {"success": False, "message": "Failed to add url", "error": str(e), "status": 500}


def list_urls():
    """Lista todos os urls cadastrados.

    Returns:
        dict: Dicion rio contendo a lista de urls, ou uma mensagem de erro se n o for poss vel listar os urls.
        int: C digo de status HTTP.
    """
    try:
        urls = UrlModel.query.all()
        if not urls:
            return {"success": True, "data": []}

        return {"success": True, "data": [{"id": url.id, **{key: value for key, value in url.__dict__.items() if not key.startswith('_')}} for url in urls]}
    except Exception as e:
        print(e)
        return {
            "success": False,
            "data": str(e),
            "message": "Failed to list urls"
        }

def get_url_by_id_service(url_id):
    """Obt m um url pelo seu ID.

    Args:
        url_id (int): ID do url a ser obtido.

    Returns:
        dict: Dicion rio contendo as informa es do url, ou uma mensagem de erro se o url n o for encontrado.
        int: C digo de status HTTP.
    """
    try:
        url = UrlModel.query.get(url_id)
        if url is None:
            return {"success": False, "data": "url not found"}
        
        return {"success": True, "data": {"id": url.id, **{key: value for key, value in url.__dict__.items() if not key.startswith('_')}}}
    except Exception as e:
        print(e)
        return {
            "success": False,
            "data": str(e),
            "message": "Failed to get url"
        }
    
def delete_url_service(url_id):
    """Deleta um url pelo seu ID.

    Args:
        url_id (int): ID do url a ser deletado.

    Returns:
        dict: Dicion rio contendo uma mensagem de confirma o, ou uma mensagem de erro se o url n o for encontrado.
        int: C digo de status HTTP.
    """
    try:
        url = UrlModel.query.get(url_id)
        if url is None:
            return {"success": False, "data": "url not found"}
        
        db.session.delete(url)
        db.session.commit()
        return {"success": True, "data": "url deleted"}
    except Exception as e:
        print(e)
        return {"success": False, "data": str(e), "message": "Failed to delete url"}
