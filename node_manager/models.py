from django.db import models
from django.contrib.auth.models import User

# Defines access modes to the node
class AccessModes(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name}"

# Defines nodes as atomic objects of parent-child relation
class Nodes(models.Model):
    name = models.CharField(max_length=200)
    access_mode = models.ForeignKey(AccessModes, null=False, blank=False, on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(User, null=False, blank=False, on_delete=models.DO_NOTHING, related_name='node_owner') 
    creator = models.ForeignKey(User, null=False, blank=False, on_delete=models.DO_NOTHING, related_name='node_creator') 
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    level = models.IntegerField(default=0, null=False, blank=False)
    root_parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING, related_name='root')

    class Meta:
        unique_together= (('name', 'creator'))

# Contains pieces of information about certain node in text 
class NodePiece(models.Model):
    piece_name =  models.CharField(max_length=200)
    node = models.ForeignKey(Nodes, null=False, blank=False, on_delete=models.CASCADE)
    is_secret = models.BooleanField(null=False, blank=False, default=True) 
    body = models.CharField()