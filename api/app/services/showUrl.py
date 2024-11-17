from ..models.UrlModel import UrlModel

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