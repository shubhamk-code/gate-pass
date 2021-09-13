from django import forms
from .models import Visitor, Contractor


class VisitorForm(forms.ModelForm):

    class Meta:
        model = Visitor
        # fields = ['name', 'email', ]
        fields = '__all__'
        exclude = ['image']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(VisitorForm, self).__init__(*args, **kwargs)

        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'input'})


class ContractorForm(forms.ModelForm):

    class Meta:
        model = Contractor
        # fields = ['name', 'email', ]
        fields = '__all__'
        exclude = ['image']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ContractorForm, self).__init__(*args, **kwargs)

        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'input'})
