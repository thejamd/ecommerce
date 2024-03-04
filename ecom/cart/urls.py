from . import views
from django.urls import path
from .views import CartSummaryView
app_name="cart"
urlpatterns = [
    path('add/',views.cart_add,name='cart_add'),
    path('delete/',views.cart_delete,name='cart_delete'),
    path('update/',views.cart_update,name='cart_update'),
    path('cart_summary/', CartSummaryView.as_view(), name='cart_summary'),    
    
    ]