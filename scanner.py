import requests

class VulnerabilityScanner:
    def __init__(self, targets, api_key):
        self.targets = targets
        self.api_key = api_key

    def scan_target(self, target):
        url = "https://vulners.com/api/v3/search/lucene/"
        query = f"{target}"
        payload = {"query": query, "apiKey": self.api_key}
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            vulns = data.get('data', {}).get('search', [])
            return vulns
        else:
            print(f"Error {response.status_code} al buscar vulnerabilidades.")
            return []

if __name__ == "__main__":
    scanner = VulnerabilityScanner(["Apache 2.4.52"], "AQUI_TU_API_KEY")
    results = scanner.scan_target("Apache 2.4.52")
    print(results)
