from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import models
from profiles_api import permissions


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


class HelloViewSet(viewsets.ViewSet):
    """Test the viewset feature"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'more appropirate for database intarractions',
            'can perform logic to requests'
        ]

        return Response({'message': 'hellp viewset', 'viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
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

    def update(self, request, pk=None):
        """Updating an object by its ID"""
        return Response({'http_method': 'PUT'})

    def retrieve(self, request, pk=None):
        """Geting an object by its ID"""
        return Response({'http_method': 'GET'})

    def partial_update(self, request, pk=None):
        """Paritally update an object by its ID"""
        return Response({'http_method': 'PATCH'})

class UserProfileViewset(viewsets.ModelViewSet):
    """Handle creating and updating user profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
