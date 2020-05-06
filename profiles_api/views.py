from rest_framework.views import APIView
from rest_framework.response import Response


from rest_framework import status
from profiles_api import serializers

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
