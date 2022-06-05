from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from django import forms
from .models import cash_male
class register(UserCreationForm):
    username = forms.CharField(label='ឈ្មោះអ្នកប្រើប្រាស់')
    password1 = forms.CharField(label='លេខសំងាត់')
    password2 = forms.CharField(label='បញ្ជាក់លេខសំងាត់')


    class Meta:
        model = User
        fields = ['username','password1']

    def __init__(self, *args, **kwargs):
        super(register, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2', ]:
            self.fields[fieldname].help_text = None


GEEKS_CHOICES =(
    ("ស្រី", "ស្រី"),
    ("ប្រុស", "ប្រុស"),
)


class add_item(forms.ModelForm):
    guest_name = forms.CharField(required='',label='ឈ្មោះភ្ញៀវ')
    guest_name.widget.attrs.update({'style': 'font-size: 20px',
                                  })
    dollar = forms.CharField(required='',label='ចងជាដុល្លារ')
    dollar.widget.attrs.update({"value":'0','style': 'font-size: 20px',
                                  })
    riel = forms.CharField(required='',label='ចងជារៀល')
    riel.widget.attrs.update({"value": '0','style': 'font-size: 20px',
                                  })
    sex = forms.ChoiceField(label='ជ្រើសរើសភេទ',choices = GEEKS_CHOICES)
    sex.widget.attrs.update({'style': 'font-size: 20px'
                                  })

    class Meta:
        model = cash_male
        fields =['guest_name','dollar','riel','sex']


