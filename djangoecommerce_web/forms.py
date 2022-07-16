from django import forms
from django.forms import ModelForm, TextInput
from djangoecommerce_app.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "message"]
        widgets = {
            'name': TextInput(attrs={'id': 'input_name','class':'form_input input_name input_ph', 'name': 'your-name', 'placeholder':'Name','data-error':'Name is required'}),
            'email': TextInput(attrs={'id': 'input_email','class':'form_input input_email input_ph', 'name': 'your-email', 'placeholder':'Email','data-error':'Valid email is required.'}),
            'subject': TextInput(attrs={'id': 'subject','class':'form_input input_name input_ph', 'name': 'your-subject', 'placeholder':'Subject','data-error':'Name is required'}),
            'message': TextInput(attrs={'id': 'subject','class':'input_ph input_message', 'name': 'your-message', 'placeholder':'Message','data-error':'Please, write us a message'}),
}
