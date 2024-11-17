from ..models.UrlModel import UrlModel, db

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