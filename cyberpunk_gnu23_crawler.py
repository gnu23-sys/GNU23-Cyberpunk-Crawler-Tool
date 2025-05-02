
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from tqdm import tqdm
from pyfiglet import figlet_format
import os

visited = set()
found_links = []
req_count = 0

headers = {
    "User-Agent": "Mozilla/5.0 (GNU23 Cyberpunk Scanner)"
}

def banner():
    print("\033[96m" + figlet_format("GNU23 Crawler") + "\033[0m")
    print("""[95m
██████╗ ███████╗███████╗██████╗ ███╗   ██╗████████╗
██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║╚══██╔══╝
██████╔╝█████╗  █████╗  ██████╔╝██╔██╗ ██║   ██║   
██╔═══╝ ██╔══╝  ██╔══╝  ██╔═══╝ ██║╚██╗██║   ██║   
██║     ███████╗███████╗██║     ██║ ╚████║   ██║   
╚═╝     ╚══════╝╚══════╝╚═╝     ╚═╝  ╚═══╝   ╚═╝   

 [92mInterface Cyberpunk • Terminal Hacker Style • v1.0
[0m""")

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def crawl(url, base_url, depth, extensions):
    global req_count
    if depth == 0 or url in visited:
        return
    try:
        response = requests.get(url, headers=headers, timeout=5)
        req_count += 1
        visited.add(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for tag in soup.find_all(['a', 'link', 'script', 'img']):
            attr = 'href' if tag.name in ['a', 'link'] else 'src'
            link = tag.get(attr)
            if not link:
                continue
            full_url = urljoin(url, link)
            if base_url in full_url and is_valid(full_url):
                if extensions:
                    if any(full_url.endswith(ext) for ext in extensions):
                        print(f"\033[92m[+][0m {full_url}")
                        found_links.append(full_url)
                else:
                    print(f"\033[92m[+][0m {full_url}")
                    found_links.append(full_url)
                crawl(full_url, base_url, depth - 1, extensions)
    except Exception as e:
        print(f"\033[91m[!][0m Erro em {url}: {e}")

def main():
    parser = argparse.ArgumentParser(description="🚀 GNU23 Cyberpunk Web Crawler")
    parser.add_argument("-u", "--url", required=True, help="URL base do alvo")
    parser.add_argument("-d", "--depth", type=int, default=2, help="Profundidade de recursão")
    parser.add_argument("-e", "--ext", nargs='*', help="Extensões a filtrar (ex: .php .js .json)")
    args = parser.parse_args()

    banner()
    print(f"\033[94m[INFO][0m Alvo: {args.url}")
    print(f"\033[94m[INFO][0m Profundidade: {args.depth}")
    if args.ext:
        print(f"\033[94m[INFO][0m Filtro de extensões: {args.ext}")
    print("\033[93m[***] Iniciando varredura...\033[0m\n")

    crawl(args.url, args.url, args.depth, args.ext)

    print(f"\n\033[96m[✓] Total de links encontrados: {len(set(found_links))}\033[0m")
    print(f"\033[96m[✓] Total de requisições feitas: {req_count}\033[0m")

    output_file = "found_links.txt"
    with open(output_file, "w") as f:
        for link in sorted(set(found_links)):
            f.write(link + "\n")
    print(f"\033[92m[✔] Links salvos em:[0m {output_file}")

if __name__ == "__main__":
    main()
