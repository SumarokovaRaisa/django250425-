from django.urls import path, include

urlpatterns = [
    path('books/', include('library.urls.books')),
    path('users/', include('library.urls.users')),
]
