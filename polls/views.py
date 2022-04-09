from django.http import HttpResponse
import requests
import json

headers = {'Content-Type': 'application/json'}
fhirbaseURL = "https://fhir.dicom.tw/fhir/"



def index(request):
   
    return HttpResponse("Hello~")

def fhirdemo(request):
    
    r = requests.get(fhirbaseURL+"Patient", verify=False)
    PatJson = r.json()["entry"]
    for entry in PatJson:
        print(entry['resource'])

    return HttpResponse(len(PatJson))