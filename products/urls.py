from django.urls import path
from .views import new_product, productDetail, updateProduct, deleteProduct, newComment, deleteComment

app_name = 'products'

urlpatterns = [
    path('new/', new_product, name='new'),
    path('detail/<int:id>/', productDetail, name='detail'),
    path('update/<int:id>/', updateProduct, name='update'),
    path('delete/<int:id>/', deleteProduct, name='delete'),
    path('new-cooment/<int:id>/', newComment, name='new_comment'),
    path('delete/<int:product_id>/comment/<int:comment_id>/', deleteComment, name='delete_comment'),
]