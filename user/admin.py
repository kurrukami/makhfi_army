from django.contrib import admin
from .models import *

from django.contrib.auth.admin import  UserAdmin
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# Register your models here.

def pswd_repr():
    return 'u cant see it bastard , Check ur momys phone'

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = compte
        fields = ('email', 'image_profile', 'CIN', 'date_joined')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = compte
        fields = ('pseudo', 'email', 'password', 'CIN', 'image_profile', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class compteAdmin(UserAdmin):
    list_display = ('pseudo', 'email', 'CIN', 'created', 'last_login', 'is_admin')
    search_fields = ('pseudo', 'email', 'CIN')
    readonly_fields = ('created', 'last_login')

    filter_horizontal = ()
    list_filter = ('is_admin',)
    fieldsets = ()

admin.site.register(compte, compteAdmin)
admin.site.register(reclamation)
