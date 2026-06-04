from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import blog, Book
from .serializers import blogserializer, BookSerializer
from rest_framework.decorators import api_view
from rest_framework import status

def index(request):
    return HttpResponse("hello ajay")


class blogAPI(APIView):
    def get(self, request):
        blogs = blog.objects.all()
        serializer = blogserializer(blogs, many=True)
        return Response(serializer.data)   # ✅ removed text after this line

    def post(self, request):
        serializer = blogserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class blogdetailAPI(APIView):

    def put(self, request, pk):
        blogdata = blog.objects.get(id=pk)
        serializer = blogserializer(blogdata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        blogdata = blog.objects.get(id=pk)
        blogdata.delete()
        return Response({"message": "deleted successfully"})  # ✅ self.response → Response


@api_view(['GET'])
def get_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book = Book.objects.filter(id=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return Response({'message': 'Book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)