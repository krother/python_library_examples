
import httpx

# Search scientific articles on PubMed:
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
param_dict = {'db':'pubmed', 'term':'escherichia', 'rettype':'uilist'}

r = httpx.get(url, params=param_dict)
print(r.text)
