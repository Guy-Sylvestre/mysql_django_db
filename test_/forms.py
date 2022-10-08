from django.forms import ModelForm, widgets
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    """
        Creer un formulaire avec le model ModelForm de django
    """
    class Meta:
        """
            Definir le nom de la table ciblee (model) et ses differents champs (fields)
        """
        model = Project
        fields = ['title', 'description']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        """
            Styliser le formulaire avec une class deja definit.
            Pour la class deja definit c'est: input.
            Le style etant repetitif, nous la parcourons avec un for
        """
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    'class': 'input'
                }
            )
            
        # self.fields['title'].widget.attrs.update(
        #         {
        #             'class': 'input'
        #         }
        #     )

        # self.fields['description'].widget.attrs.update(
        #         {
        #             'class': 'input'
        #         }
        #     )
        