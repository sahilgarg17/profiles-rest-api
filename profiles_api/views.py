from rest_framework.views import APIView
from rest_framework.response import Response


from rest_framework import status
from profiles_api import serializers

from rest_framework import viewsets

from profiles_api import models

from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions

class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """returns a list of APIView features"""
        serializer_class  = serializers.HelloSerializer
        an_apiview = [
        'uses http methods as function (get,post,patch,put,delete)',
        'is similar to traditional django view',
        'Gives you the most control over you application logic',
        'is mapped manually to URLs',
        ]
        return Response({'message':'helllo!','an_apiview':an_apiview})

    def post(self,request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})
    def patch(self, request, pk=None):
        """Handle partial updating an object """
        return Response({'method':'PATCH'})
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """test api ViewSet"""
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        """return a hello message"""
        a_viewset = [
        'Uses actions (create,list,retrieve,update,partial_update)',
        'Automatically maps to urls using routers',
        'provides more functionality wid less code',
        ]
        return Response({'message':'hello!','a_viewset':a_viewset})
    def create(self,request):
        """creates a new heelloo msg"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self,request,pk=None):
        """gets an object by id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Hndels  upadate an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """handels partial updating of object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """handels removing of object"""
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """handels creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes  = (TokenAuthentication,)
    permission_class = (permissions.UpdateOwnProfile,)
