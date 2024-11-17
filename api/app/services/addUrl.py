from ..models.UrlModel import UrlModel, db
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