import argparse
import sys
import os
import pdfcrowd
from helpers import gen_urls, logger

def convert_pages(username, apikey, pages, out):
    if not os.path.isdir(out):
        os.makedirs(out)

    try:
        client = pdfcrowd.HtmlToPdfClient(username, apikey)
        client.setFailOnMainUrlError(True)

        for i, url in enumerate(gen_urls(pages)):
            file_name = os.path.join(out, 'generated_{}.pdf'.format(i))
            logger.info('creating %s from %s', file_name, url)
            client.convertUrlToFile(url, file_name)

    except pdfcrowd.Error as why:
        logger.error('Pdfcrowd Error: %s', why)
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Batch conversion for multiple URLs to PDFs.')
    parser.add_argument(
        '--user', help='Pdfcrowd username', required=True)
    parser.add_argument(
        '--key', help='Pdfcrowd API key', required=True)
    parser.add_argument(
        '--pages', help='File with URLs to be converted', required=True)
    parser.add_argument(
        '--out', help='Output folder', required=True)

    args = parser.parse_args()
    convert_pages(args.user, args.key, args.pages, args.out)
