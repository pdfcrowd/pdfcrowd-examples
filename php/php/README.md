# Pdfcrowd & PHP Web Server Demo

Sample for dynamic and static HTML to PDF conversions.

### Prerequisites

```
php
composer
```

Replace **'your_username'** with your Pdfcrowd username and **'your_apikey'** with your Pdfcrowd API key in **[index.php](index.php#L42)** file. Sign up for a [free trial](https://pdfcrowd.com/user/sign_up/?pid=api-trial2) if you don't have the credentials.

## Installing

```
composer install
```

## Web server start

```
php -S localhost:8080 index.php
```

## Test

   Open a sample web page <http://localhost:8080/>

   Invoke a conversion to PDF by pressing buttons at the bottom of the page.

## Documentation

* API Home:  <https://pdfcrowd.com/doc/api/>
* API Reference:  <https://pdfcrowd.com/doc/api/html-to-pdf/php/>
