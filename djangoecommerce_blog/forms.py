from django import forms
from djangoecommerce_blog.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "message"]
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name', 'name': 'your-name', 'placeholder':'Name'}),
            'email': forms.TextInput(attrs={'id': 'email', 'name': 'your-email', 'placeholder':'Email'}),
            'subject': forms.TextInput(attrs={'id': 'subject', 'name': 'your-subject', 'placeholder':'Subject'}),
        }
