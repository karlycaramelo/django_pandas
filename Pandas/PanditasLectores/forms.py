from django.forms import ModelForm
from .models import Grupo

class GrupoForm(ModelForm):
    class Meta:
        model = Grupo #modelo que se le pasa al form
        fields = ['grupo_num', 'file']
#Creando un form para agregar un grupo.
form = GrupoForm()
