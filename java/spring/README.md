# Pdfcrowd & Spring Demo

Sample for dynamic and static HTML to PDF conversions.

### Prerequisites

```
java
gradle
```

## Installing

```
./gradlew build
```

## Web Server Start

```
java -jar build/libs/pdfcrowd-demo-0.1.0.jar
```

## Test

   Open a sample web page <http://localhost:8080/>

   Invoke a conversion to PDF by pressing buttons at the bottom of the page.

## Pdfcrowd API License

   If you wish to use your Pdfcrowd API license, replace **demo** credentials with your Pdfcrowd username and API key in **[src/main/java/demo/DemoController.java](src/main/java/demo/DemoController.java#L39)** file.
   A [free trial](https://pdfcrowd.com/user/sign_up/?pid=api-trial2) API license can be used too.

## Documentation

* API Home:  <https://pdfcrowd.com/doc/api/>
* API Reference:  <https://pdfcrowd.com/doc/api/html-to-pdf/java/>
