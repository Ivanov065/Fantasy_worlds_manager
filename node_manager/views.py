from django.shortcuts import render, redirect
from .models import Nodes, NodesAllowedUsers, NodesPch
from .forms import NodeTreeForm

# Base view
def home(request):
    nodes = Nodes.objects.all()
    return render(request, "home.html", {"nodes": nodes})


# TODO: show user node tree
def show_node_tree(request, pk):
    nodes = Nodes.objects.filter(parent=pk)


# TODO: create node tree (that means create root node)
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
            created_root.save(update_fields=["parent"])
            NodesAllowedUsers.objects.create(node=created_root, allowed_user=request.user)
            
            return redirect("node_manager:home")
    else:
        form = NodeTreeForm()
    return render(request, "create_node_tree.html", {'form': form})
    


# TODO: create node tree branch (that means create node that has parent in a node tree)
def create_node_tree_branch(request):
    pass


# TODO: update node tree (now update node no matter what it is)
def update_node(request):
    pass


# TODO: delete node tree (deletes any node AND IT'S CHILDREN)
def delete_node(request):
    pass

# TODO: create node tree piece 
def create_node_tree_piece(request, pk):
    if request.method == "POST":
        form = NodeTreeForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.creator = request.user
            form.save()
            NodesAllowedUsers.objects.create(node=Nodes.objects.get(creator=request.user, name=request.POST["name"]), allowed_user=request.user)
            return redirect("node_manager:home")
    else:
        form = NodeTreeForm()
    return render(request, "create_node_tree_piece.html", {'form': form})

# TODO: update node tree piece
def update_node_tree_piece(request):
    pass

# TODO: delete node tree piece
def delete_node_tree_piece(request):
    pass
