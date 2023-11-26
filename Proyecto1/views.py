from django.http import HttpResponse
from django.template import Template, Context

def primerTemplate(self):
    
    miHtml = open("C:/Users/Imanol Calvo/Desktop/Curso Python/Proyecto1/Proyecto1/Plantillas/template1.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    mi_contexto = Context()

    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)
