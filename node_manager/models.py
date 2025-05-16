from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Defines access modes to the node
class AccessModes(models.Model):
    name = models.CharField(max_length=40) # TODO: define modes logically

# Defines nodes as atomic objects of parent-child "fantasy setting" relation
# "parent" foreign key to itself will allow to "walk" through nodes 
class Nodes(models.Model):
    name = models.CharField(max_length=200)
    access_mode = models.ForeignKey(AccessModes, null=False, blank=False, on_delete=models.DO_NOTHING)
    creator = models.ForeignKey(User, null=False, blank=False, editable=False, on_delete=models.DO_NOTHING, related_name='node_creator') # TODO: make "if creator deleted" logic
    owner = models.ForeignKey(User, null=False, blank=False, on_delete=models.DO_NOTHING, related_name='node_owner') # TODO: make "if owner changes" logic
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

# Contains pieces of information about certain node in text 
class NodePieces(models.Model):
    node = models.ForeignKey(Nodes, null=False, blank=False, on_delete=models.CASCADE)
    is_secret = models.BooleanField(null=False, blank=False, default=True) # defines if owner wants to show this piece to ANYONE except himself
    body = models.CharField()

# Contains users (as well as the owner and the creator) who can look at your "nodes tree"
# In case when "AccessMode" of the node is not "public" defines allowed users
class NodesAllowedUsers(models.Model):
    node = models.ForeignKey(Nodes, null=False, blank=False, on_delete=models.CASCADE)
    allowed_user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
