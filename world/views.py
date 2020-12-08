from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point
from django.utils import timezone
from django.views import generic
import requests
from opencage.geocoder import OpenCageGeocode

from .models import PreviousLocations


@login_required
def create_previous_location(request):
    try:
        point = request.POST["point"].split(",")
        point = [float(part) for part in point]
        point = Point(point, srid=4326)

        for previous_location in PreviousLocations.objects.filter(user=request.user):
            if previous_location.location == point:
                previous_location.created = timezone.now()
                previous_location.save()
                return JsonResponse({"message": f"Previous location: {point.wkt} updated."}, status=200)

        location = PreviousLocations(user=request.user, location=point, location_name=request.POST["location"])
        location.save()

        return JsonResponse({"message": f"Previous location: {point.wkt} added."}, status=200)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)


@login_required
def get_previous_locations(request):
    try:

        locations = serializers.serialize('python',
                                          PreviousLocations.objects.filter(user=request.user)[:10].only('created',
                                                                                                        'location',
                                                                                                        'location_name'))
        locations_json = [d['fields'] for d in locations]
        locations_json = [{k: v for k, v in d.items() if k != 'user'} for d in locations_json]

        return JsonResponse(locations_json, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)


def reverse_geocode(request):
    try:
        with open('opencage-apikey.txt') as k:
            apikey = k.read().strip()
        point = request.POST["point"].replace(" ", "").split(",")
        geocoder = OpenCageGeocode(apikey)

        results = geocoder.reverse_geocode(point[0], point[1])

        formatted_response = results[0]["components"]

        return JsonResponse(formatted_response, status=200)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)


def forward_geocode(request):
    try:
        with open('opencage-apikey.txt') as k:
            apikey = k.read().strip()
        search = request.POST["search"]
        geocoder = OpenCageGeocode(apikey)

        results = geocoder.geocode(search)

        if len(results) > 0:
            formatted_response = results[0]["geometry"]
            return JsonResponse(formatted_response, status=200)
        else:
            response = {"location": "not found"}
            return JsonResponse(response, status=200)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)


def get_weather(request):
    try:
        with open('openweathermap-apikey.txt') as k:
            apikey = k.read().strip()
        point = request.POST["point"].replace(" ", "").split(",")

        url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid={}".format(point[0],
                                                                                                           point[1],
                                                                                                           apikey)
        r = requests.get(url)
        return JsonResponse(r.json(), status=r.status_code)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)


# @method_decorator(login_required, name='dispatch')
class MapView(generic.TemplateView):
    template_name = "world/index.html"
