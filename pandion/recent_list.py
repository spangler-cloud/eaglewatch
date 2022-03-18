from .models import Notable

def ListFunction():
    rare_list = []
    existing_rares = []
    for rare in Notable.objects.filter().values_list('comName', 'locName', "obsDt", "speciesCode").order_by('-id')[:20:-1]:
        if rare[3] not in existing_rares:
            rare_list.append(rare)
            existing_rares.append(rare[3])
    return rare_list
