from django import forms


class CarterasFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    codigo = forms.CharField(max_length=50)
    stock = forms.IntegerField()

class CamperasFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    codigo = forms.CharField(max_length=50)
    stock = forms.IntegerField()

class ZapatosFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    codigo = forms.CharField(max_length=50)
    stock = forms.IntegerField()

class AccesoriosFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    codigo = forms.CharField(max_length=50)
    stock = forms.IntegerField()