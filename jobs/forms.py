from django import forms 
from .models import Job

class PostJobForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'required': '',
            'name': 'title',
            'id': 'title',
            'type': 'text',
            'placeholder': 'Job Title',
            'class': 'text'

        })
        
        
        self.fields['description'].widget.attrs.update({
            'required': '',
            'name': 'description',
            'id': 'description',
            'type': 'text',
            'placeholder': 'Job Description',
            'class': 'text w3lpass'

        })
        
        self.fields['location'].widget.attrs.update({
            'required': '',
            'name': 'location',
            'id': 'location',
            'type': 'text',
            'placeholder': 'Job Location',
            'class': 'text w3lpass'

        })
        
        self.fields['company_name'].widget.attrs.update({
            'required': '',
            'name': 'company_name',
            'id': 'company_name',
            'type': 'text',
            'placeholder': 'Company Name',
            'class': 'text w3lpass'

        })
        
        self.fields['company_description'].widget.attrs.update({
            'required': '',
            'name': 'company_description',
            'id': 'company_description',
            'type': 'text',
            'placeholder': 'Company Description',
            'class': 'text w3lpass'

        })
        
        self.fields['website'].widget.attrs.update({
            'required': '',
            'name': 'website',
            'id': 'website',
            'type': 'text',
            'placeholder': 'Website',
            'class': 'text w3lpass'

        })
        
    type = forms.ChoiceField(choices=Job.JOB_TYPE_CHOICES)
    salary = forms.DecimalField(label='Salary')
        
    class Meta:
        model = Job
        fields = ['user', 'type', 'title', 'description', 'location', 'company_name', 'company_description', 'website', 'salary']
        widgets = {
            'description': forms.TextInput(
                attrs={
                    'cols': 20,
                    'rows': 20
                }
            ),
            'company_description': forms.TextInput(),
        }
        