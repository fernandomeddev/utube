from ..models.UrlModel import UrlModel, db
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
