# Pdfcrowd & ASP.NET Web Forms Demo

Sample for dynamic and static HTML to PDF conversions.

### Prerequisites

```
.NET
XSP
```

## Installing

```
nuget install -OutputDirectory packages
```

## Web Server Start

```
xsp --port=8080
```

## Test

   Open a sample web page <http://localhost:8080/>

   Invoke a conversion to PDF by pressing buttons at the bottom of the page.

## Pdfcrowd API License

   If you wish to use your Pdfcrowd API license, replace **demo** credentials with your Pdfcrowd username and API key in **[Default.aspx.cs](Default.aspx.cs#L55)** file.
   A [free trial](https://pdfcrowd.com/user/sign_up/?pid=api-trial2) API license can be used too.

## Documentation

* API Home:  <https://pdfcrowd.com/doc/api/>
* API Reference:  <https://pdfcrowd.com/doc/api/html-to-pdf/dotnet/>
