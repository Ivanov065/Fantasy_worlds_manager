from django.contrib import admin
from .models import Nodes, NodePieces, NodesAllowedUsers, AccessModes

# Register your models here.

admin.site.register(Nodes)
admin.site.register(NodePieces)
admin.site.register(NodesAllowedUsers)
admin.site.register(AccessModes)