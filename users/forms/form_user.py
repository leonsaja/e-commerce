from django.contrib.auth import forms
from users.models import User

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User
        
class UserCreateForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User