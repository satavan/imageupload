from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Task
from rest_framework import viewsets
from .Serializers import TaskSerializer,UserSerializer
from rest_framework import filters
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()  
    serializer_class = TaskSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields =  ('completed',)
    ordering  = ('-date_created',)

class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer



