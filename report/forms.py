from django import forms
from .models import Comment

class apply_form(forms.ModelForm):
    class Meta:
      model = Comment
      fields = ['name','email','comment']
      labels = {
            'name': '',
            'email': '',
            'comment': '',
        }
    def __init__(self, *args, **kwargs):
        super(apply_form, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'الاسم'})
        self.fields['email'].widget.attrs.update({'placeholder': 'البريد الإلكتروني'})
        self.fields['comment'].widget.attrs.update({'placeholder': 'رأيك'})