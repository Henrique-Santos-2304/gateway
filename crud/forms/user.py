from django import forms
from django.contrib.auth.hashers import make_password, check_password
from crud.models import SoilUser
from django.contrib.auth import get_user_model

import uuid


class UserForm(forms.ModelForm):

    model = SoilUser
    fields = ('username', 'user_type', "password", "user_id")
        

    def clean_password1(self):
        return make_password(self.cleaned_data["password"])

    def save(self, commit=True):
        user = super().save(commit=False)
        
        if not user.user_id:
            user.user_id = uuid.uuid4()
        
        if user.user_type == "SUDO":
            user.first_name = user.username
            user.is_superuser = True
            user.is_active = True 
            user.is_staff = True
            
            
        if commit:
            user.save()
            
        return user
        

        
        
        
    

        
