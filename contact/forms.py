from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Your Message'}),
        }
