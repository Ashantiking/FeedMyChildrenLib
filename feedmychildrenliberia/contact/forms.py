from django import forms

class ContactForm(forms.Form):
    user_name = forms.CharField(error_messages={'required': 'Please enter your name'})
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    cc_myself = forms.BooleanField(required=False)