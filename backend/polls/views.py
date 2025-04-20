from django.shortcuts import render
from django.contrib.auth.models import Group, User
from polls.serializers import UserSerializer, GroupSerializer
from rest_framework import permissions, viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    

def index(request):
    # Данные для передачи в шаблон
    context = {
        'name': 'Иван Иванов',
        'age': 28,
        'skills': ['Python', 'Django', 'HTML']
    }
    
    # Рендеринг шаблона my_template.html с переданным контекстом
    return render(request, 'polls/index.html', context)
