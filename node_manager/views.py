from django.shortcuts import render, redirect
from .models import Nodes, NodesAllowedUsers
from .forms import NodeTreeForm, NodePieceForm
from django.contrib.auth.decorators import login_required

# Base view
def home(request):
    nodes = Nodes.objects.all()
    return render(request, "home.html", {"nodes": nodes})


# TODO: show user node tree
def show_node_tree(request, pk):
    nodes = Nodes.objects.filter(root_parent=pk)
    max_level = 0
    for node in nodes:
        if node.level > max_level:
            max_level = node.level
    return render(request, "show_node_tree.html", {"nodes": nodes, "max_level": max_level})


# TODO: create node tree (that means create root node)
@login_required(login_url='users:login')
def create_root(request):
    if request.method == "POST":
        form = NodeTreeForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.creator = request.user
            form.save()
            # print(request.POST["name"])
            created_root = Nodes.objects.get(creator=request.user, name=request.POST["name"])
            created_root.parent = created_root
            created_root.root_parent = created_root
            created_root.save(update_fields=["parent", "root_parent"])
            NodesAllowedUsers.objects.create(node=created_root, allowed_user=request.user)
            #NodesPch.objects.create(child=created_root, parent=created_root)
            
            return redirect("node_manager:home")
    else:
        form = NodeTreeForm()
    return render(request, "create_node_tree.html", {'form': form})
    


# TODO: create node tree branch (that means create node that has parent in a node tree)
@login_required(login_url='users:login')
def create_node_tree_branch(request):
    pass


# TODO: update node tree (now update node no matter what it is)
@login_required(login_url='users:login')
def update_node(request):
    pass


# TODO: delete node tree (deletes any node AND IT'S CHILDREN)
@login_required(login_url='users:login')
def delete_node(request, pk):
    node = Nodes.objects.get(pk=pk)

    if node.owner != request.user and not request.user.is_superuser:
        return redirect("node_manager:forbidden")

    if request.method == "POST":
        node.delete()
        return redirect("node_manager:home")

    return render(request, "node_delete.html", {"node": node})

# TODO: create node tree piece 
@login_required(login_url='users:login')
def create_node_tree_piece(request, pk):

    node = Nodes.objects.get(pk=pk)
    if node is None:
        return redirect("node_manager:not_found")

    if request.method == "POST":
        form = NodePieceForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.node = node
            form.save()
            return redirect("node_manager:create_node_tree_branch", pk=pk)
    else:
        form = NodePieceForm()
    return render(request, "create_node_tree_piece.html", {'form': form, "node": node})

# TODO: update node tree piece
@login_required(login_url='users:login')
def update_node_tree_piece(request):
    pass

# TODO: delete node tree piece
@login_required(login_url='users:login')
def delete_node_tree_piece(request):
    pass

def not_found(request):
    return render(request, "404.html")