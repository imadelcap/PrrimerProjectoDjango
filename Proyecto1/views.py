from django.http import HttpResponse
from django.template import loader


def primerTemplate(self):
    
    #miHtml = open("C:/Users/Imanol Calvo/Desktop/Curso Python/Proyecto1/Proyecto1/Plantillas/template1.html")

    plantilla = loader.get_template("template1.html")
    
    #miHtml.close()

    #mi_contexto = Context()
    documento = plantilla.render()

    return HttpResponse(documento)
