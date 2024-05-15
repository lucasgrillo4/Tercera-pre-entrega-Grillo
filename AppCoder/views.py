from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.


def contratoFormulario(request):
    if request.method == "POST":
        
        miFormulario = ContratoFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            micontrato = Contrato(clienteNombre=informacion['clienteNombre'],tipoContrato=informacion['tipoContrato'],numContrato=informacion['numContrato'])
            
            micontrato.save()

            return render(request,"AppCoder/buscarCentral.html")
    else:
        miFormulario=ContratoFormulario()
    
    return render(request, "AppCoder/contratoFormulario.html",{"miFormulario":miFormulario})


def cliente(request):
    if request.method == "POST":
        
        miFormulario = ClienteFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            miCliente = Cliente(cliente=informacion['cliente'],nCliente=informacion['nCliente'],email=informacion['email'])
            
            miCliente.save()

            return render(request,"AppCoder/buscarCentral.html")
    else:
        miFormulario=ClienteFormulario()
    
    return render(request, "AppCoder/cliente.html",{"miFormulario":miFormulario})

def central(request):
    if request.method == "POST":
        
        miFormulario = CentralFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            miCentral = Central(nombreCentral=informacion['nombreCentral'],cantidadContratos=informacion['cantidadContratos'])
            
            miCentral.save()

            return render(request,"AppCoder/buscarCentral.html")
    else:
        miFormulario=CentralFormulario()
    
    return render(request, "AppCoder/central.html",{"miFormulario":miFormulario})

def buscarCentral(request):
    return render(request,"AppCoder/buscarCentral.html")

def buscar(request):
    if request.GET["nombreCentral"]:
        nombreCentral = request.GET['nombreCentral']
        centrales = Central.objects.filter(nombreCentral = nombreCentral)
        
        return render(request,"AppCoder/resultadosPorBusqueda.html",{"centrales":centrales,"nombreCentral":nombreCentral})    
    else:
        respuesta ="No enviaste datos"
        
    return HttpResponse(respuesta)

def inicio(request):
    return render(request,"AppCoder/inicio.html")





