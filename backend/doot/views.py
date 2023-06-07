from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from doot.serializers import DocumentSerializer

from haystack.query import SearchQuerySet

@api_view(['GET', 'POST'])
def test_func(request):
    if request.method == 'GET':
        query = request.query_params.get("q")
        results = SearchQuerySet().filter(content=query)

        documents = [item.object for item in results]

        serializer = DocumentSerializer(documents, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DocumentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response("parameters are not valid!")
