# 🕶️ GNU23 Cyberpunk Crawler  
*Scanner de links recursivo, no estilo Photon, com interface hacker estilo terminal*

![badge](https://img.shields.io/badge/versão-1.0-brightgreen?style=for-the-badge)
![badge](https://img.shields.io/badge/interface-cyberpunk-purple?style=for-the-badge)
![badge](https://img.shields.io/badge/feito%20por-gnu23-blue?style=for-the-badge)

---

## 🔥 Visão Geral

**GNU23 Cyberpunk Crawler** é uma ferramenta de varredura de links (web crawler) desenvolvida para pentesters e entusiastas do submundo cibernético.  
Inspirada na pegada visual do **Photon** e dos terminais de filmes como Mr. Robot e Matrix, ela **recursivamente extrai todos os links de um site**, com suporte a filtros por extensão e exibição em modo neon terminal-style. ☠️💻

---

## ⚙️ Recursos

- 🕵️‍♂️ Extração de links HTML (`href`, `src`) com BeautifulSoup
- 🔁 Varredura recursiva com profundidade customizável
- 🎯 Filtro por tipo de arquivo (ex: `.php`, `.js`, `.json`)
- 🌐 Segue apenas links dentro do domínio
- ✨ Interface colorida estilo cyberpunk com banner em ASCII
- 📂 Exportação para `found_links.txt`

---

## 📦 Requisitos

- Python 3.x
- Módulos:
  - `requests`
  - `beautifulsoup4`
  - `pyfiglet`
  - `tqdm`

Instale com:

```bash
pip install requests beautifulsoup4 pyfiglet tqdm

🚀 Como Usar

python3 cyberpunk_gnu23_crawler.py -u https://exemplo.com -d 2 -e .php .js


| Flag     | Descrição                             |
|----------|----------------------------------------|
| `-u`     | URL base do alvo (obrigatório)         |
| `-d`     | Profundidade recursiva (padrão: 2)     |
| `-e`     | Extensões a filtrar (opcional)         |
