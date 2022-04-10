from django.urls import path, include
from . import views

urlpatterns = [path('bets/', views.BetList.as_view(), name='bet_list'), path('bets/<int:pk>',views.BetDetail.as_view(), name='bet_detail'),]
