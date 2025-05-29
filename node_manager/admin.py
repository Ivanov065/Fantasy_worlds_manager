from django.contrib import admin
from .models import Nodes, NodePiece, NodesAllowedUsers, AccessModes

# Register your models here.

admin.site.register(Nodes)
admin.site.register(NodePiece)
admin.site.register(NodesAllowedUsers)
admin.site.register(AccessModes)