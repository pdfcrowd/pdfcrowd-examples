# Pdfcrowd & Django Demo

Sample for dynamic and static HTML to PDF conversions.

### Prerequisites

```
python
```

## Installing

```
pip install -r requirements.txt
```

## Web Server Start

```
python manage.py runserver 8080
```

## Test

   Open a sample web page <http://localhost:8080/>

   Invoke a conversion to PDF by pressing buttons at the bottom of the page.

## Pdfcrowd API License

   If you wish to use your Pdfcrowd API license, replace **demo** credentials with your Pdfcrowd username and API key in **[demo/views.py](demo/views.py#L37)** file.
   A [free trial](https://pdfcrowd.com/user/sign_up/?pid=api-trial2) API license can be used too.

## Documentation

* API Home:  <https://pdfcrowd.com/doc/api/>
* API Reference:  <https://pdfcrowd.com/doc/api/html-to-pdf/python/>
