from django.db import models
from django.contrib.auth.models import User

# Defines access modes to the node
class AccessModes(models.Model):
    name = models.CharField(max_length=40) # TODO: define modes logically

    def __str__(self):
        return f"{self.name}"

# Defines nodes as atomic objects of parent-child "fantasy setting" relation
# "parent" foreign key to itself will allow to "walk" through nodes 
class Nodes(models.Model):
    name = models.CharField(max_length=200)
    access_mode = models.ForeignKey(AccessModes, null=False, blank=False, on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(User, null=False, blank=False, on_delete=models.DO_NOTHING, related_name='node_owner') # TODO: make "if owner changes" logic
    creator = models.ForeignKey(User, null=False, blank=False, on_delete=models.DO_NOTHING, related_name='node_creator') # TODO: make "if creator deleted" logic
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    level = models.IntegerField(default=0, null=False, blank=False)
    root_parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING, related_name='root')

    class Meta:
        unique_together= (('name', 'creator'))

# Helps to work with node tree
class NodesPch(models.Model):
    child = models.ForeignKey(Nodes, on_delete=models.CASCADE, related_name="nodes_pch_child")
    parent = models.ForeignKey(Nodes, on_delete=models.CASCADE, related_name="nodes_pch_parent")

# Contains users (as well as the owner and the creator) who can look at your "nodes tree"
# In case when "AccessMode" of the node is not "public" defines allowed users
class NodesAllowedUsers(models.Model):
    node = models.ForeignKey(Nodes, null=False, blank=False, on_delete=models.CASCADE)
    allowed_user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

# Contains pieces of information about certain node in text 
class NodePiece(models.Model):
    piece_name =  models.CharField(max_length=200)
    node = models.ForeignKey(Nodes, null=False, blank=False, on_delete=models.CASCADE)
    is_secret = models.BooleanField(null=False, blank=False, default=True) # defines if owner wants to show this piece to ANYONE except himself
    body = models.CharField()