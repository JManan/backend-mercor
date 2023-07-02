from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DocSerializer
from .models import Doc
from django.http import JsonResponse
from patient.serializers import PatientSerializer

def index(request):
    return render(request, "doc/index.html")

@api_view(['GET'])
def scrape(request):
    drug = request.query_params.get("searchitem")
    url = f"https://www.drugs.com/{drug}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')
    content = soup.find(id="content")  # bs4.element.tag
    values = []
    blocks = {}
    blocks["drug name"] = drug
    myp = soup.find_all("p", {"class": "drug-subtitle"})

    for i in myp:
        t = i.text

    li = list(t.split(" "))
    count = 0

    for ele in li:
        count = count + 1
        if(ele == 'class:'):
            break

    str = ''
    while count < len(li):
        str += li[count] 
        str += " "
        count = count + 1

        str.strip()
        blocks["drug class"] = str
    for heading in content.find_all("h2"):
        if(heading.get("id") == "uses" or heading.get("id") == "side-effects" or heading.get("id") == "dosage"):            # find separators, in this case h2 nodes
            for sibling in heading.find_next_siblings():
                if sibling.name == "h2":
                    break
                values.append(sibling.text)
            blocks[heading.text] = values
    return Response(blocks)

@api_view(['GET', 'POST'])
def doc_data(request):
    if request.method == "POST":
        serializer = DocSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        short_uuid = request.query_params.get("id")
        try:
            doc = Doc.objects.get(short_uuid=short_uuid)
        except:
            doc = None
        serializer = DocSerializer(doc)
        return JsonResponse(serializer.data)

@api_view(['GET'])
def patient_list(request):
    id = request.query_params.get("id")
    doc = Doc.objects.get(short_uuid=id)
    patients = doc.patients.all()
    serializer = PatientSerializer(patients, many=True)
    return JsonResponse(serializer.data, safe=False)