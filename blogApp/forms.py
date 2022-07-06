from django import forms
from .models import *

from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget

class FormArticulo(forms.Form):
    title = forms.CharField(max_length=150,label="Titulo")
    content = forms.CharField(widget=CKEditorWidget())   
