from django.urls import path
from .views import home, create,detail,delete_blog,update_blog,category,blog_list,user_signup,user_login,user_logout
urlpatterns = [
    path('index/', home, name="index"),
    path('create/', create, name="create"),
    path('blog_list/<int:id>/', blog_list, name='blog_list'),
    path('category/', category, name='category'),
    path("blog/<int:id>/", detail,  name="detail"),
    path("delete_blog/<int:id>/", delete_blog,  name="delete"),
    path("update_blog/<int:id>/", update_blog, name="update"),
    # path('dashboard/', dashboard, name='dashboard'),
    path('', user_signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout')
]