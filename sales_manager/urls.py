from django.urls import path
from sales_manager import views

urlpatterns = [
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book_rate/<int:book_id>/<int:rate>/<str:redirect_url>/', views.book_like, name='book-rate'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add-ajax-like/', views.add_like_ajax),
    path('add_comment/<int:book_id>/', views.add_comment, name='add-comment'),
    path('comment_like/<int:comment_id>/', views.comment_like, name='comment-like'),
    path('', views.main_page, name='main-page')
]
