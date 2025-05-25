from django.shortcuts import render, redirect
from .models import Nodes, AccessModes
from .forms import NodeTreeForm

# Base view
def home(request):
    nodes = Nodes.objects.all()
    return render(request, "home.html", {"nodes": nodes})


# TODO: show user node tree
def show_node_tree(request, pk):
    pass


# TODO: create node tree (that means create root node)
def create_root(request):
    if request.method == "POST":
        form = NodeTreeForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.creator = request.user
            form.save()
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

# TODO: create node tree (that means create root node)
def show_node_tree(request):
    pass

# TODO: create node tree (that means create root node)
def create_node_tree(request):
    pass

# TODO: create node tree (that means create root node)
def create_node_tree(request):
    pass

# TODO: create node tree (that means create root node)
def create_node_tree(request):
    pass
