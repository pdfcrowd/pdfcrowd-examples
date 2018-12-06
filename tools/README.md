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

A utility for converting URLs from a text file into PDF files. Run Wikipedia example with:
```
python convert_pages.py --user $USER_NAME --key $API_KEY --pages urls.txt --out out
```

## Multiple URLs to a Single PDF File

A utility for converting multiple URLs from a text file into a single PDF file. Run Wikipedia example with:
```
python convert_pages_to_single_pdf.py --user $USER_NAME --key $API_KEY --pages urls.txt --out wiki.pdf
```

## Create a Brochure from Multiple HTML Pages

A demo utility for converting multiple URLs into a single PDF file. Run the demo with:
```
python create_brochure.py --user $USER_NAME --key $API_KEY --out brochure.pdf
```

## Documentation

* API Home:  <https://pdfcrowd.com/doc/api/>
* API Reference:  <https://pdfcrowd.com/doc/api/html-to-pdf/python/>
