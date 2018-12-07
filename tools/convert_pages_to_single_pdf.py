import argparse
import sys
import os
import pdfcrowd
from helpers import gen_urls, logger

def gen_pdfs(username, apikey, max_pages, urls):
    # create the API client instance
    client = pdfcrowd.HtmlToPdfClient(username, apikey)
    client.setFailOnMainUrlError(True)

    for url in urls:
        pages_str = ''
        if max_pages > 0:
            logger.info('converting max %s pages from %s', max_pages, url)
            client.setPrintPageRange('-{}'.format(max_pages))
        else:
            logger.info('converting %s', url)
        yield client.convertUrl(url)
        logger.info('%s pages converted', client.getPageCount())
        if max_pages > 0:
            max_pages -= client.getPageCount()
            if max_pages <= 0:
                break

def convert_pages(username, apikey, pages, max_pages, out):
    try:
        client = pdfcrowd.PdfToPdfClient(username, apikey)

        for pdf in gen_pdfs(username, apikey, max_pages, gen_urls(pages)):
            client.addPdfRawData(pdf)

        logger.info('joining PDF files into %s', out)
        client.convertToFile(out)

    except pdfcrowd.Error as why:
        logger.error('Pdfcrowd Error: %s', why)
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""Batch conversion for multiple URLs to a single PDF.
        WARNING: This script is just for demo and can consume lots of Pdfcrowd credits! So there is a default limit of 10 pages. Use --max-pages option to increase the limit on your own risk.
        """)
    parser.add_argument(
        '--user', help='Pdfcrowd username', required=True)
    parser.add_argument(
        '--key', help='Pdfcrowd API key', required=True)
    parser.add_argument(
        '--pages', help='File with pages to be converted', required=True)
    parser.add_argument(
        '--max-pages', type=int, default=10,
        help='The maximum number of pages to be converted. -1 means no limit.')
    parser.add_argument(
        '--out', help='PDF output file name', required=True)

    args = parser.parse_args()
    convert_pages(args.user, args.key, args.pages, args.max_pages, args.out)
