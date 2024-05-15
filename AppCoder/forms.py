from django import forms 


class ClienteFormulario(forms.Form):
    cliente = forms.CharField()
    nCliente = forms.IntegerField()
    email= forms.EmailField()


class ContratoFormulario(forms.Form):   
    clienteNombre= forms.CharField()
    tipoContrato= forms.CharField()
    numContrato = forms.IntegerField()


class CentralFormulario(forms.Form):   
    nombreCentral= forms.CharField()
    cantidadContratos = forms.IntegerField()