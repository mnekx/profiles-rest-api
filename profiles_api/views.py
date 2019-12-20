from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Test APIView"""

    def get(self, request, format=None):
        """Returns Response object"""
        an_apiview = [
            'item1',
            'item2',
            'item3'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})