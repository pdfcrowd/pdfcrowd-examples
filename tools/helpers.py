import logging
import re

# configure logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel('INFO')

# parse locations by own, so etree is not needed to be installed
RE_XML_LOC = re.compile('^<loc>(.*)</loc>$')
def xml_parse(line):
    m = RE_XML_LOC.match(line)
    return m.groups()[0] if m else None

def text_parse(line):
    return None if line.startswith('#') else line

def gen_urls(file_name):
    with open(file_name) as f:
        data = f.readlines()

        if len(data) == 0:
            raise Exception('no URL specified')

        # detect file format
        if data[0].startswith('<?xml'):
            parser = xml_parse
        else:
            parser = text_parse

        for line in data:
            line = line.strip()
            if line:
                url = parser(line)
                if url:
                    yield url


