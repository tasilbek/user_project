from django.views.generic import ListView
from .models import User

# Create your views here.
class UserPageView(ListView):
    model = User
    template_name = 'users/user_list.html'