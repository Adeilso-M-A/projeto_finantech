from django.http import JsonResponse

def api_root(request):
    """
    View simples para a raiz da API.
    Ajuda o professor a entender que o sistema está online.
    """
    return JsonResponse({
        "projeto": "Sistema de Gestão Financeira",
        "status": "Online",
        "versao": "1.0.0",
        "documentacao": "/api/v1/" # Ou o caminho que você definiu nas URLs
    })