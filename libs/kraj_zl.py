from . import utils
from urllib.parse import urljoin

class web:
  kraj= 'Zlínský kraj'
  
  def crawl(self):
    results = []
    pocet_okresu = 4
    url = 'http://www.khszlin.cz/25304-novy-koronavirus-2019-ncov'
    page = utils.get_url(url)
    doc = page.select_one('a.pdf[href*=info_cov19]')['href']
    url = urljoin(url, doc)
    lines = [line for line in utils.get_pdfminer(url) if len(line.replace(' ', '')) > 0]
    start_index = None
    distance_to_counts = None
    for i, line in enumerate(lines):
      if line.startswith('okres'):
        start_index = i
        break
    #distance_to_counts = pocet_okresu * 2
    distance_to_counts = pocet_okresu + 1
    if start_index and distance_to_counts:
      for i in range(start_index, start_index + pocet_okresu):
        name = lines[i].strip().replace('okres ', '')
        results.append({'okres': name, 'kraj': self.kraj, 'hodnota': int(lines[i + distance_to_counts].strip())})

    return results
