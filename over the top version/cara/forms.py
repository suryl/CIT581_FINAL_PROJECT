from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'comment']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address', 'phone_number']