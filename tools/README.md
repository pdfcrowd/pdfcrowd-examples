# Pdfcrowd Helper and Demo Utilities

Example utilities for HTML to PDF conversions.

### Prerequisites

```
python
```

Sign up for a [free trial](https://pdfcrowd.com/user/sign_up/?pid=api-trial2) if you don't have Pdfcrowd username and API key.

## Installing

```
pip install pdfcrowd
```

## Batch HTML to PDF Conversion

A utility for converting URLs into PDF files. URLs may be specified in a text file or a sitemap XML file.

Run Wikipedia examples with:
```
python convert_pages.py --user $USER_NAME --key $API_KEY --pages sample_urls.txt --out output.pdf
```
```
python convert_pages.py --user $USER_NAME --key $API_KEY --pages sample_sitemap.xml --out output.pdf
```

## Multiple URLs to a Single PDF File

A utility that can convert multiple URLs into a single PDF file. The URLs can be specified in a text file or a sitemap XML file.

INFO: The script limits the number of PDF pages to 10 by default. You can use the`--max-pages` option to lift that limit but please note that this can potentionally consume a lot of API conversion credits. Use the `-h` option to see all available options.

Run Wikipedia example with:
```
python convert_pages_to_single_pdf.py --user $USER_NAME --key $API_KEY --pages sample_urls.txt --out wiki.pdf
```

```
python convert_pages_to_single_pdf.py --user $USER_NAME --key $API_KEY --pages sample_sitemap.xml --out wiki.pdf
```

Hint: you can create the sitemap.xml for your site by e.g. [Online Generator](https://www.xml-sitemaps.com/)

## Create a Brochure from Multiple HTML Pages

A demo utility for converting multiple URLs into a single PDF file with different pages orientation.

Run the demo with:
```
python create_brochure.py --user $USER_NAME --key $API_KEY --out brochure.pdf
```

## Documentation

* API Home:  <https://pdfcrowd.com/doc/api/>
* API Reference:  <https://pdfcrowd.com/doc/api/html-to-pdf/python/>
