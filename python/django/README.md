# Pdfcrowd & Django Demo

Sample for dynamic and static HTML to PDF conversions.

### Prerequisites

```
python
```

Replace **'your_username'** with your Pdfcrowd username and **'your_apikey'** with your Pdfcrowd API key in **[demo/views.py](demo/views.py#L41)** file. Sign up for a [free trial](https://pdfcrowd.com/user/sign_up/?pid=api-trial2) if you don't have the credentials.

## Installing

```
pip install -r requirements.txt
```

## Web server start

```
python manage.py runserver 8080
```

## Test

   Open a sample web page <http://localhost:8080/>

   Invoke a conversion to PDF by pressing buttons at the bottom of the page.

## Documentation

* API Home:  <https://pdfcrowd.com/doc/api/>
* API Reference:  <https://pdfcrowd.com/doc/api/html-to-pdf/python/>
