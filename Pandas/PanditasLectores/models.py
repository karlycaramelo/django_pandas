from django.db import models
from django.core.validators import FileExtensionValidator


# Model to store the groups including the xlsx file (list of students)
class Grupo(models.Model):
    def __int__(self) -> int:
        return self.grupo_num
    def __str__(self) -> str:
        return str(self.grupo_num)
    grupo_num = models.IntegerField()
    file = models.FileField(upload_to='GroupFiles', null=True,  blank=True,  validators=[FileExtensionValidator( ['xls','xlsx'] )])
