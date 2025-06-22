from django.shortcuts import render, redirect
from .models import Nodes, NodesAllowedUsers, NodePiece
from .forms import NodeTreeForm, NodePieceForm
from django.contrib.auth.decorators import login_required

def home(request):
    nodes = Nodes.objects.all()
    return render(request, "home.html", {"nodes": nodes})


def show_node_tree(request, pk):
    try:
        root = Nodes.objects.get(pk=pk)
    except Nodes.DoesNotExist:
        return redirect("node_manager:not_found")

    if request.user != root.owner and root.access_mode.name == "private":
        return redirect("node_manager:forbidden")

    nodes = Nodes.objects.filter(root_parent=pk)

    if nodes.count() == 0:
        return redirect("node_manager:not_found")

    max_level = 0
    for node in nodes:
        if node.level > max_level:
            max_level = node.level
    return render(request, "show_node_tree.html", {"nodes": nodes, "max_level": max_level})


def show_user_trees(request):
    user = request.user
    roots = Nodes.objects.filter(owner=user, level = 0)

    if roots.count() == 0:
        return redirect("node_manager:not_found")

    return render(request, 'show_user_trees.html', {'roots' : roots})


@login_required(login_url='users:login')
def create_root(request):
    if request.method == "POST":
        form = NodeTreeForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.creator = request.user
            form.save()

            created_root = Nodes.objects.get(creator=request.user, name=request.POST["name"])
            created_root.parent = created_root
            created_root.root_parent = created_root
            created_root.save(update_fields=["parent", "root_parent"])
            NodesAllowedUsers.objects.create(node=created_root, allowed_user=request.user)
            
            return redirect("node_manager:home")
    else:
        form = NodeTreeForm()
    return render(request, "create_node_tree.html", {'form': form})
    

@login_required(login_url='users:login')
def create_node_tree_branch(request, parent):

    try:
        parent_node = Nodes.objects.get(pk=parent)
    except Nodes.DoesNotExist:
        return redirect("node_manager:not_found")

    if request.user != parent_node.owner:
                return redirect("node_manager:forbidden")
    
    if request.method == "POST":
        form = NodeTreeForm(request.POST)

        if form.is_valid():

            instance = form.save(commit=False)
            instance.owner = request.user
            instance.creator = request.user
            form.save()

            created_node = Nodes.objects.get(creator=request.user, name=request.POST["name"])
            created_node.parent = parent_node
            created_node.level = parent_node.level + 1
            created_node.root_parent = parent_node.root_parent
            created_node.save(update_fields=["parent", "root_parent", 'level'])

            NodesAllowedUsers.objects.create(node=created_node, allowed_user=request.user)
            
            return redirect("node_manager:home")
            
    else:
        form = NodeTreeForm()

    return render(request, "create_node_tree_branch.html", {'form': form, "parent_node": parent_node})


def show_node(request, pk):

    try:
        node = Nodes.objects.get(pk=pk)
    except Nodes.DoesNotExist:
        return redirect("node_manager:not_found")

    if request.method == "POST":

        if request.user != node.owner:
            return redirect("node_manager:forbidden")

        form = NodePieceForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.node = node
            instance.save()
            return redirect("node_manager:show_node", pk=pk)

    if request.user != node.owner:

        if node.access_mode.name == "private":
            return redirect("node_manager:forbidden")

        pieces = NodePiece.objects.filter(node=node, is_secret=False)
        form = None
    else:
        form = NodePieceForm()
        pieces = NodePiece.objects.filter(node=node)

    return render(request, "show_node.html", {'form': form, 'pieces': pieces, "node": node})
    

@login_required(login_url='users:login')
def update_node(request, pk):

    try:
        node = Nodes.objects.get(pk=pk)
    except Nodes.DoesNotExist:
        return redirect("node_manager:not_found")
    
    parent_node = node.parent
    

    if request.user != parent_node.owner:
                return redirect("node_manager:forbidden")
    
    if request.method == "POST":
        form = NodeTreeForm(request.POST, instance=node)

        if form.is_valid():

            form.save()
            return redirect("node_manager:home")
    else:
        form = NodeTreeForm(instance=node)
        form.access_mode = node.access_mode.name

    return render(request, "update_node_tree_branch.html", {'form': form, "parent_node": parent_node, "node":node})


@login_required(login_url='users:login')
def delete_node(request, pk):

    try:
        node = Nodes.objects.get(pk=pk)
    except Nodes.DoesNotExist:
        return redirect("node_manager:not_found")

    if node.owner != request.user and not request.user.is_superuser:
        return redirect("node_manager:forbidden")

    if request.method == "POST":
        if node.id == node.root_parent.id:
            node.delete()
            return redirect("node_manager:show_user_trees")
        else:
            root = Nodes.objects.get(pk=node.root_parent.id)
            node.delete()
            return redirect("node_manager:show_node_tree", pk = root.id)

    return render(request, "node_delete.html", {"node": node})


@login_required(login_url='users:login')
def create_node_tree_piece(request, pk):
    try:
        node = Nodes.objects.get(pk=pk)
    except Nodes.DoesNotExist:
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


@login_required(login_url='users:login')
def update_node_tree_piece(request, pk):

    try:
        node_piece = NodePiece.objects.get(pk=pk)
    except Nodes.DoesNotExist:
        return redirect("node_manager:not_found")
    
    node = node_piece.node

    if node.owner != request.user and not request.user.is_superuser:
        return redirect("node_manager:forbidden")

    if request.method == "POST":
        form = NodePieceForm(request.POST, instance=node_piece)

        if form.is_valid():
            node_piece.body = request.POST['body']
            node_piece.piece_name = request.POST['piece_name']

            if 'is_secret' in request.POST:
                node_piece.is_secret = True
            else:
                node_piece.is_secret = False

            node_piece.save(update_fields=["body", "piece_name", 'is_secret'])

            return redirect("node_manager:show_node", pk = node.pk)

    return redirect("node_manager:show_node", pk = node.pk)


@login_required(login_url='users:login')
def delete_node_tree_piece(request, pk):
    try:
        node_piece = NodePiece.objects.get(pk=pk)
    except Nodes.DoesNotExist:
        return redirect("node_manager:not_found")
    
    node = node_piece.node

    if node.owner != request.user and not request.user.is_superuser:
        return redirect("node_manager:forbidden")

    if request.method == "POST":
        node_piece.delete()
        return redirect("node_manager:show_node", pk = node.pk)

    return redirect("node_manager:show_node", pk = node.pk)


def not_found(request):
    return render(request, "404.html")


def forbidden(request):
    return render(request, "forbidden.html")