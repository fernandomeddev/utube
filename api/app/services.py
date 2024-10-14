from pytube import YouTube
from app.models import UrlModel, db

def is_valid_youtube_url(url):
    """Verifica se uma determinada URL  uma URL do YouTube vlida.

    Args:
        url (str): URL a ser verificada.

    Returns:
        pytube.YouTube: Inst ncia da classe YouTube contendo informa es sobre o v deo,
            caso a URL seja vlida; False, caso contr rio.
    """

    try:
        videoInformationbyURL = YouTube(url)
        print(videoInformationbyURL)
        return videoInformationbyURL
    except:
        return False

def add_url_info(urlInfo):
    """Adiciona um novo url.

    Recebe um objeto contendo as informa es do novo url e o adiciona na lista de urls.
    Caso a URL do YouTube seja fornecida, verifica se ela  vlida.

    Args:
        urlInfo (pytube.YouTube): Inst ncia da classe YouTube contendo informa es sobre o v deo.

    Returns:
        dict: Dicion rio contendo as informa es do novo url, ou uma mensagem de erro se a URL do YouTube for inv lida.
        int: C digo de status HTTP.
    """
    try:
        newUrlInfo = UrlModel(**{
            'title': urlInfo.title,
            'description': urlInfo.description,
            'views': urlInfo.views,
            'publish_date': urlInfo.publish_date,
            'author': urlInfo.author,
            'length': urlInfo.length,
            'watch_url': urlInfo.watch_url
        })

        db.session.add(newUrlInfo)
        db.session.commit()

        data = {
            "success": True,
            "data": {
                "id": newUrlInfo.id,
                **{key: value for key, value in newUrlInfo.__dict__.items() if not key.startswith('_')}
            }
        }
        return data
    except Exception as e:
        data = {
            "success": False,
            "data": str(e),
            "message": "Failed to add url"
        }
        return data

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
