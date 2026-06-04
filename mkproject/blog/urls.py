from django.urls import path
from .import views
from blog.views import blogAPI,blogdetailAPI

urlpatterns = [
    path('',views.index,name = 'index' ),
    path('blog/',blogAPI.as_view()),
    path('blog/<int:pk>/',blogdetailAPI.as_view()),
    path('books/',views.get_books,name = 'get_books'),
    path('books/<int:pk>/',views.get_book,name='get_book'),
    path('books/create/',views.create_book),
    path('books/<int:pk>/update/',views.update_book, name='update_book'),
    path('books/<int:pk>/delete/',views.delete_book, name='delete_book'),
]

