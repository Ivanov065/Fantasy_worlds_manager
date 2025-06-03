from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path('show_tree/<int:pk>', views.show_node_tree, name='show_node_tree'),
    path('show_node/<int:pk>', views.show_node, name='show_node'),
    path('create_root/', views.create_root, name='create_root'),
    path('create_tree_branch/<int:parent>', views.create_node_tree_branch, name='create_node_tree_branch'),
    path('update_branch/<int:pk>', views.update_node, name='update_node'),
    path('delete_branch/<int:pk>', views.delete_node, name='delete_node'),
    path('create_node_piece/<int:pk>', views.create_node_tree_piece, name="create_node_tree_piece"),
    path('not_found/', views.not_found, name='not_found')
]