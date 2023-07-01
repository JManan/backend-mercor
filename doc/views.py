from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def scrape(request):
    drug = request.query_params.get("searchitem")
    url = f"https://www.drugs.com/{drug}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')
    content = soup.find(id="content")  # bs4.element.tag
    values = []
    blocks = {}
    for heading in content.find_all("h2"):
        if(heading.get("id") == "uses" or heading.get("id") == "side-effects" or heading.get("id") == "dosage"):            # find separators, in this case h2 nodes
            for sibling in heading.find_next_siblings():
                if sibling.name == "h2":  # iterate through siblings until separator is encoutnered
                    break
                values.append(sibling.text)
            blocks[heading.text] = values
            
    return Response(blocks)
