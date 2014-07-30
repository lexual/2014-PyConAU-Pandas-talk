urls = [
    'http://www.bom.gov.au/fwo/IDN60903/IDN60903.94926.axf',
    'http://www.bom.gov.au/fwo/IDN60903/IDN60903.94926.json',
    'http://www.bom.gov.au/fwo/IDN60901/IDN60901.94768.axf',
    'http://www.bom.gov.au/fwo/IDN60901/IDN60901.94768.json',
    'http://www.bom.gov.au/fwo/IDV60901/IDV60901.94868.axf',
    'http://www.bom.gov.au/fwo/IDV60901/IDV60901.94868.json',
    'http://www.bom.gov.au/fwo/IDQ60901/IDQ60901.94576.axf',
    'http://www.bom.gov.au/fwo/IDQ60901/IDQ60901.94576.json',
    'http://www.bom.gov.au/fwo/IDS60901/IDS60901.94675.axf',
    'http://www.bom.gov.au/fwo/IDS60901/IDS60901.94675.json',
    'http://www.bom.gov.au/fwo/IDW60901/IDW60901.94608.axf',
    'http://www.bom.gov.au/fwo/IDW60901/IDW60901.94608.json',
    'http://www.bom.gov.au/fwo/IDT60901/IDT60901.94970.axf',
    'http://www.bom.gov.au/fwo/IDT60901/IDT60901.94970.json',
    'http://www.bom.gov.au/fwo/IDD60901/IDD60901.94120.axf',
    'http://www.bom.gov.au/fwo/IDD60901/IDD60901.94120.json',
]

import os
import datetime

now = datetime.datetime.now()

for url in urls:
    print url
    base = os.path.basename(url)
    print base
    output_fname = base.replace('.axf', '_%s.axf' % now.isoformat())
    output_fname = output_fname.replace('.json', '_%s.json' % now.isoformat())
    print output_fname
    os.system('wget {} -O {}'.format(url, output_fname))
