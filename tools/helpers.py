import logging

# configure logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel('INFO')

def gen_urls(file_name):
    with open(file_name) as f:
        for url in f.readlines():
            url = url.strip()
            if url and not url.startswith('#'):
                yield url

