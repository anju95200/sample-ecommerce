from django.urls import path
from shop import views
from .views import signup
from .views import user_logout


urlpatterns=[
    path('',views.home,name='home'),
    path('products',views.pro,name='pro'),
    path('add_product', views.add, name='add_product'),
    path('delete/<int:pro_id>',views.delete_product,name='delete'),
    path('edit/<int:pro_id>',views.edit,name='edit'),
    path('search',views.search,name='search'),
    path('signup',views.signup,name='sign'),
    path('signin',views.signin,name='signin'),
    path('logout/', views.user_logout, name='logout'),
    
]
