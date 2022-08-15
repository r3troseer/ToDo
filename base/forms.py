from django import forms
from .models import Task


# task form to create or edit tasks
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = { 'name' : forms.TextInput(attrs={'class':'form-control','id':'floatingInput','placeholder':'name',}),
                    'description': forms.Textarea(attrs={'class':'form-control','id':'floatingTextarea','placeholder':'name',}),
                    'date': forms.DateInput(attrs={'class':'form-control','id':'floatingInput date','type':'date',}),
                    'time': forms.TimeInput(attrs={'class':'form-control','id':'floatingInput time','type':'time',}),
                    'priority': forms.Select(attrs={'class':'form-select','id':'floatingSelect',}),
                    'repeat': forms.Select(attrs={'class':'form-select','id':'floatingSelect',}),
                    'tag': forms.Select(attrs={'class':'form-select','id':'floatingSelect',}),
                        # 'venuetypes' : forms.Select(queryset=Venuetypes.objects.all, 
                        #                             attrs={'class' : 'venue_type_select'}
                        #                             )
                       } 
    # name= forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','id':'floatingInput'}))
