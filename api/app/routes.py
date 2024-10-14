from flask import Blueprint, jsonify, request # type: ignore
from app.services import add_url_info, delete_url_service, get_url_by_id_service, is_valid_youtube_url, list_urls

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def home():
    try:
        return jsonify({"message": "service is running"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "service is not running"}), 500

# Rota para listar todos os videos
@main_routes.route('/api/urls', methods=['GET'])
def get_url_info():
    response_service =  list_urls()
    if not response_service['success']:
        return jsonify(response_service), 404
    
    return jsonify(response_service), 200

# Rota para obter um URL pelo ID
@main_routes.route('/api/url/<int:url_id>', methods=['GET'])
def get_url_by_id(url_id):
    """Obtém um url pelo seu ID.
    Args:
        url_id (int): ID do url a ser obtido.
    Returns:
        dict: Dicionário contendo as informações do url.
        int: Código de status HTTP.
    """
    
    response_service = get_url_by_id_service(url_id)
    if not response_service['success']:
        return jsonify(response_service), 404
    
    return jsonify(response_service), 200

# Rota para adicionar um novo Url
@main_routes.route('/api/url', methods=['POST'])
def add_url():
    try:
        """Adiciona um novo url.

        Recebe um JSON contendo as informações do novo url e o adiciona na lista de urls.
        Caso a URL do YouTube seja fornecida, verifica se ela é válida.

        Args:
            request (Request): Requisição que contém o corpo com as informações do novo url.

        Returns:
            Response: Resposta com o novo url adicionado, ou uma mensagem de erro se a URL do YouTube for inválida.
            int: Código de status HTTP.
        """
        body = request.get_json()
        print(request.get_json())
        # Verificar se a URL do YouTube está presente no corpo da requisição
        youtube_url = body.get("url", None)
        if youtube_url is None:
            return jsonify({"error": "YouTube URL is required"}), 400

        # Verificar se a URL do YouTube é válida
        validUrl =  is_valid_youtube_url(youtube_url)
        if not validUrl:
            return jsonify({"error": "Invalid YouTube URL"}), 400
        
        response_service = add_url_info(validUrl)
        if not response_service['success']:
            return jsonify(response_service), 400
        
        return jsonify(response_service), 200
    except Exception as e:
        print(e)
        return str(e), 500

# Rota para deletar um url pelo ID
@main_routes.route('/api/url/<int:url_id>', methods=['DELETE'])
def delete_url(url_id):
    """Deleta um url pelo seu ID.

    Args:
        url_id (int): ID do url a ser deletado.

    Returns:
        dict: Dicionário contendo uma mensagem de confirmação.
        int: Código de status HTTP.
    """
    try:
        response_service = delete_url_service(url_id)
        if not response_service['success']:
            return jsonify(response_service), 404
        return jsonify(response_service), 200
    except Exception as e:
        print(e)
        return str(e), 500
