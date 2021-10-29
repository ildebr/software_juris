from django.shortcuts import render
from juris.models.legal_record import LegalRecord
from juris.models.proceeding import Proceeding

def index(request):

    if request.method == "POST":
        num= request.POST.get('numero_de_fiscalia', None)
        tri = request.POST.get('tribunal', None)
        let = request.POST.get('letra', None)
        año = request.POST.get('año', None)
        num_exp = request.POST.get('numero_expediente')
        if num:
            resultado = LegalRecord.objects.get(prosecutor_number=num, court_number= tri, letter=let, start_date__year=año, record_number=num_exp)
            actualizaciones = Proceeding.objects.filter(legal_record=1)
            return render(request, 'index.html', {'resultado': resultado, 'actualizaciones': actualizaciones})
    return render(request, "index.html")
