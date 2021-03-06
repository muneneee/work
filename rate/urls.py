from django.urls import path
from .views import PostView,DetailView,CreateView,UpdatePostView,DeletePostView
from . import views


urlpatterns=[
    path('', PostView.as_view(), name='index'),
    path('profile/',views.profile, name='profile'),
    path('post/<int:project_id>/', views.detail, name='detail'),
    path('post/new/', CreateView.as_view(), name='create'),
    path('post/<int:pk>/update/', UpdatePostView.as_view(), name='update'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete'),
    path('search/', views.search_results, name = 'search_results'),
    path('api/project/', views.ProjectList.as_view()),
    path('api/profile/', views.ProfileList.as_view()),

]