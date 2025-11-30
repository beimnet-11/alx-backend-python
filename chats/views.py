from django.http import JsonResponse

def index(request):
    return JsonResponse({"message": "Chats API working"})

def home(request):
    return JsonResponse({"message": "Welcome to Messaging API"})

# Create your views here.
