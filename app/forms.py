from django import forms

from app.models import user,User


class userform(forms.ModelForm):

    class Meta:
        model = user

        fields = ['name','age','profile_pic']

class myform(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username','first_name','last_name','email','password']

        widgets = {'password':forms.PasswordInput()}
        



