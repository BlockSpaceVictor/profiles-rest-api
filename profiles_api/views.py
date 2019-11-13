from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test api view"""

    def get(self, request, format=None):
        """returns a list of api views features"""

        an_apiview = [
            "User HTTP methods as function (get, pots, patch, put, delete)",
            "Is similar to a traditional Django View",
            "gives you the most control over your application logic",
            "is mapped manually to URLs",
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    
