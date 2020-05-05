from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """returns a list of APIView features"""
        an_apiview = [
        'uses http methods as function (get,post,patch,put,delete)',
        'is similar to traditional django view',
        'Gives you the most control over you application logic',
        'is mapped manually to URLs',
        ]

        return Response({'message':'helllo!','an_apiview':an_apiview})
