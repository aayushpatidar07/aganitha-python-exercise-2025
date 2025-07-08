import requests
import pandas as pd

def is_academic(affiliation):
    if affiliation is None:
        return False
    keywords = ["university", "institute", "college", "school", "faculty", "department"]
    return any(word in affiliation.lower() for word in keywords)

def fetch_papers(query, max_results=20):
    print(f"Fetching papers for query: {query}...\n")
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {"db": "pubmed", "term": query, "retmax": max_results, "retmode": "json"}
    response = requests.get(url, params=params)
    ids = response.json()['esearchresult']['idlist']
    return ids

def fetch_details(ids):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {"db": "pubmed", "id": ",".join(ids), "retmode": "xml"}
    response = requests.get(url, params=params)
    return response.text

def parse_and_filter(xml_data):
    from xml.etree import ElementTree as ET
    root = ET.fromstring(xml_data)
    filtered = []

    for article in root.findall(".//PubmedArticle"):
        title = article.findtext(".//ArticleTitle", default="No Title")
        affiliations = [aff.text for aff in article.findall(".//Affiliation")]
        if not affiliations:
            continue

        if all(is_academic(aff) for aff in affiliations if aff):
            continue

        filtered.append({"title": title, "affiliations": "; ".join(affiliations)})

    return filtered

def save_to_csv(data, filename="filtered_output.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"\n✅ Done! Filtered papers saved to '{filename}'")

if __name__ == "__main__":
    query = input("🔍 Enter your PubMed search keyword: ")
    ids = fetch_papers(query)
    xml_data = fetch_details(ids)
    filtered = parse_and_filter(xml_data)
    save_to_csv(filtered)
