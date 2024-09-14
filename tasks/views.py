from rest_framework import viewsets
from .serializers import TasSerializer
from .models import Task
# Create your views here.


class TaskVeiew(viewsets.ModelViewSet):
    serializer_class = TasSerializer
    queryset = Task.objects.all()

