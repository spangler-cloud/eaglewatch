from BirdCounter.models import TopLocations


def AddTotal(location_id, location_name, how_many, state_name):
    if TopLocations.objects.filter(locId=location_id).exists() == True:
        q = State.objects.filter(locId=location_id)
        q.howMany += int(how_many)
        q.save()
    else:
        q = TopLocations(locId = location_id, locName = location_name, state =  state_name, howMany =  int(how_many))
        q.save()


