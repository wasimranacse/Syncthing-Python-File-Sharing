from django.shortcuts import render
from django.http import HttpResponse
import requests
import json


def get_system_info(request):
    url = 'http://localhost:8384/rest/system/version'
    response = requests.get(url)
    data = json.load(response.content)
    return HttpResponse(f'Syncthing version: {data["version"]}')





