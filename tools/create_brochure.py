# -*- coding: utf-8 -*-

import argparse
import sys
import os
from datetime import datetime
import logging
import pdfcrowd
from helpers import gen_urls, logger

def gen_pdfs(username, apikey):
    # create the API client instance
    logger.info('converting a cover page')
    client = pdfcrowd.HtmlToPdfClient(username, apikey)
    client.setMarginTop('3in')
    client.setPageBackgroundColor('3366cc30')
    yield client.convertString('<center><h1>Wikipedia Article Demo</h1></center><ul><li>multiple URLs and page orientations in a single PDF</li><li>hyperlinks in a header</li><li>page numbers in a footer</li></ul><center><p>powered by <a href="https://pdfcrowd.com/">Pdfcrowd</a>, <i>{}</i></p></center>'.format(
        datetime.now().date()))
    offset = -1

    for title, url in (('Main', 'https://www.wikipedia.org/'),
                       ('Article:PDF', 'https://en.wikipedia.org/wiki/PDF'),
                       ('Talk:PDF', 'https://en.wikipedia.org/wiki/Talk:PDF')):
        logger.info('converting %s', url)
        client = pdfcrowd.HtmlToPdfClient(username, apikey)
        client.setPageNumberingOffset(offset)
        client.setNoMargins(True)
        if title == 'Main':
            client.setOrientation('landscape')
        client.setHeaderHtml('<center><a href="{}">Wikipedia - {}</a></center>'.format(url, title))
        client.setFooterHtml('<center>~ <span class="pdfcrowd-page-number"></span> ~</center>')
        client.setFailOnMainUrlError(True)
        pdf = client.convertUrl(url)
        offset -= client.getPageCount()
        yield pdf

def create_brochure(username, apikey, out):
    try:
        client = pdfcrowd.PdfToPdfClient(username, apikey)

        for pdf in gen_pdfs(username, apikey):
            client.addPdfRawData(pdf)

        logger.info('joining PDF files into %s', out)
        client.convertToFile(out)

    except pdfcrowd.Error as why:
        # report the error to the standard error stream
        sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Demo for creating a brochure from Wikipedia.')
    parser.add_argument(
        '--user', help='Pdfcrowd username', required=True)
    parser.add_argument(
        '--key', help='Pdfcrowd API key', required=True)
    parser.add_argument(
        '--out', help='PDF output file name', required=True)

    args = parser.parse_args()
    create_brochure(args.user, args.key, args.out)
