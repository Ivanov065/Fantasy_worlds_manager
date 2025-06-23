from django.contrib import admin
from .models import Nodes, NodePiece, AccessModes

# Register your models here.

admin.site.register(Nodes)
admin.site.register(NodePiece)
admin.site.register(AccessModes)