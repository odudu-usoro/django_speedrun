import random
from rest_framework.decorators import api_view
from rest_framework.response import Response

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