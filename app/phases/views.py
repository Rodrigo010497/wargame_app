from django.template.response import TemplateResponse
from .modules.army_loader import unit
from .modules.Army import Army
from django.shortcuts import redirect

troop = unit('Brother-Captain')
args = {}
army = Army([unit(i) for i in troop.get_all_army_units()])
args['army'] = army.army_list
args['phases'] = ["command", "movement", "shooting", "charge", "fighting"]

def phases(request):
    args['phase'] = army.phase
    return TemplateResponse(request, 'phases.html', args)
    # template = loader.get_template('phases.html')
    # return HttpResponse(template.render())

def change_view_phase(request, phase):
    print(phase)
    army.change_phase(phase)
    return redirect("phases")