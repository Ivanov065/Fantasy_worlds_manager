from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path('show_tree/<int:pk>', views.show_node_tree, name='show_node_tree'),
    path('create_tree/', views.create_node_tree, name='create_node_tree'),
    path('create_tree_branch/', views.create_node_tree_branch, name='create_node_tree_branch'),
    path('update_branch/<int:pk>', views.update_node, name='update_node'),
    path('delete_branch/<int:pk>', views.delete_node, name='delete_node')
]