from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloAPIView(APIView):
    """Test APIView"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns Response object"""
        an_apiview = [
            'item1',
            'item2',
            'item3'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request, format=None):
        """Test when POST request is sent"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Test PUT request method"""
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        """Test PATCH request method"""
        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        """Test the DELETE method"""
        return Response({'message': 'DELETE'})