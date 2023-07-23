import requests
from bs4 import BeautifulSoup

def get_targets(req) -> list:
    original = req.GET.get("from", None)
    
    url = f"http://hgdownload.cse.ucsc.edu/goldenPath/{original}/liftOver/"
    
    result = requests.get(url)
    soup = BeautifulSoup(result.content, "html.parser")
    
    links = [link for link in soup.find_all("a") if link.get("href").endswith(".over.chain.gz")]
    
    targets = []
    
    for link in links:
        file_name = link.get("href").split(".")[0]
        file_name = file_name.replace(f"{original}To", "")
        targets.append(file_name)
    
    return targets