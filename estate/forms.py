from django import forms

from estate.models import PropertyDetails

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class RealEstateCreateForm(forms.ModelForm):
    
    class Meta:
        model = PropertyDetails
        exclude = ('owner',)
        
        widgets={
            "property_name":forms.TextInput(attrs={"class":"form-control mb-2"}),
            "property_type":forms.Select(attrs={"class":"form-control form-select mb-2"}),
            "property_status":forms.Select(attrs={"class":"form-control form-select mb-2"}),
            "location":forms.Select(attrs={"class":"form-control form-select mb-2"}),
            "address":forms.TextInput(attrs={"class":"form-control mb-2"}),
            "price":forms.NumberInput(attrs={"class":"form-control mb-2"}),
            "area":forms.NumberInput(attrs={"class":"form-control mb-2"}),
            "no_of_rooms":forms.NumberInput(attrs={"class":"form-control mb-2"}),
            "furnished_status":forms.Select(attrs={"class":"form-control form-select mb-2"})
        }
    
    # property_name = forms.CharField()
    
    # property_type = forms.ChoiceField(choices=PropertyDetails.PROPERTY_OPTIONS)
    
    # property_status = forms.ChoiceField(choices=PropertyDetails.STATUS_OPTIONS)
    
    # location = forms.ChoiceField(choices=PropertyDetails.LOCATION_OPTIONS)
    
    # address = forms.CharField()
    
    # price = forms.FloatField()
    
    # area = forms.FloatField()
    
    # no_of_rooms = forms.IntegerField()
    
    # furnished_status = forms.ChoiceField(choices=PropertyDetails.FURNISHED_OPTIONS)
    
class SignUpForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-1","placeholder":"Enter your name here"}))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control mb-1","placeholder":"Enter your Email id"}))
    
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class":"form-control mb-1","placeholder":"Enter your password"}))
    
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={"class":"form-control mb-1","placeholder":" Re-Enter password"}))
    
    class Meta:
        
        model = User
        
        fields = ["username","email","password1","password2"]
        
class LoginForm(forms.Form):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Enter your name "}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Enter your password"}))