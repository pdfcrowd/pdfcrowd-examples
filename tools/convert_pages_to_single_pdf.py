import argparse
import sys
import os
import pdfcrowd
from helpers import gen_urls, logger

def gen_pdfs(username, apikey, urls):
    # create the API client instance
    client = pdfcrowd.HtmlToPdfClient(username, apikey)
    client.setFailOnMainUrlError(True)

    for url in urls:
        logger.info('converting %s', url)
        yield client.convertUrl(url)

def convert_pages(username, apikey, pages, out):
    try:
        client = pdfcrowd.PdfToPdfClient(username, apikey)

        for pdf in gen_pdfs(username, apikey, gen_urls(pages)):
            client.addPdfRawData(pdf)

        logger.info('joining PDF files into %s', out)
        client.convertToFile(out)

    except pdfcrowd.Error as why:
        logger.error('Pdfcrowd Error: %s', why)
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Batch conversion for multiple URLs to a single PDF.')
    parser.add_argument(
        '--user', help='Pdfcrowd username', required=True)
    parser.add_argument(
        '--key', help='Pdfcrowd API key', required=True)
    parser.add_argument(
        '--pages', help='File with pages to be converted', required=True)
    parser.add_argument(
        '--out', help='PDF output file name', required=True)

    args = parser.parse_args()
    convert_pages(args.user, args.key, args.pages, args.out)
