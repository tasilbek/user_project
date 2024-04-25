from rest_framework.generics import ListAPIView
from users.models import User
from .serializers import UserSerializers

# Create your views here.
class UserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers