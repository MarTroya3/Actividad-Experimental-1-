from django.shortcuts import render
from inventario.models import Entidadinventario, Entidadproducto

# Create your views here.
def stock(request):
	mi_stock = Entidadinventario.objects.all()
	num_stock = len(mi_stock)
	informacion_template = {"mis_entidades":mi_stock, "num_entidades":num_stock};
	return render(request, "stock.html", informacion_template)