from rest_framework import generics
from .serializers import FavoriteSerializer, CustomUserSerializer
from user.models import CustomUser, Favorite
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.db import IntegrityError

def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            newuser = CustomUser(username=request.POST['username'], password=request.POST['password1'])
            newuser.save()
            token = Token.objects.create(user=newuser)
            return JsonResponse({'token': str(token)}, status=201)

        except IntegrityError:
            return JsonResponse({'error': 'this username has already been taken'}, status=400)

def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        theuser = CustomUser.objects.get(username=request.POST['username'], password=request.POST['password'])
        
        if theuser is None:
            return JsonResponse({'error': 'not exist!'}, status=400)

        else:
            try:
                token = Token.objects.get(user=theuser)
            except:
                token = Token.objects.create(user=theuser)

            return JsonResponse({'token': str(token)}, status=200)

class FavoritesList(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer
    
    def get_queryset(self):
        return CustomUser.objects.all()
