import requests
import time
import yaml

def check_health(endpoint):
    try:
        response = requests.request(
            method=endpoint.get('method', 'GET'),
            url=endpoint['url'],
            headers=endpoint.get('headers'),
            data=endpoint.get('body')
        )
        return 'UP' if response.ok and response.elapsed.total_seconds() * 1000 < 500 else 'DOWN'
    except requests.RequestException:
        return 'DOWN'

def parse_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def main(file_path):
    endpoints = parse_yaml(file_path)
    domain_total = {}
    total_tries = 0

    try:
        while True:
            for endpoint in endpoints:
                domain = endpoint['url'].split('/')[2]  # Extracting domain from URL
                status = check_health(endpoint)
                availability = 1 if status == 'UP' else 0
                if domain not in domain_total:
                    domain_total[domain] = {
                        'total_hits': 0,
                        'total_tries': 0
                    }
                domain_total[domain]['total_hits'] += availability
                domain_total[domain]['total_tries'] += 1

            for domain, stats in domain_total.items():
                print(f"{domain} has {round((stats['total_hits'] / stats['total_tries']) * 100)}% availability")

            time.sleep(15)

    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
    file_path = "input.yaml"  
    main(file_path)