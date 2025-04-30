import random
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import viewsets
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import SignupSerializer

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "I Escaped Tutorial Hell!"})

@api_view(['GET'])
def random_joke(request):
    jokes = [
        "Why don't scientist trust atoms? Because they make up everything!",
        "What do you call fake spaghetti? An impasta"    
    ]
    return Response({"joke": random.choice(jokes)})

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, sserializer):
        serializer.save(author=self.request.user)


class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({"token": token.key}, status=201)
        return Response(serializer.errors, status=400)