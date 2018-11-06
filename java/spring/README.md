# Pdfcrowd & Spring Demo

Sample for dynamic and static HTML to PDF conversions.

### Prerequisites

```
java
gradle
```

Replace **'your_username'** with your Pdfcrowd username and **'your_apikey'** with your Pdfcrowd API key in **[src/main/java/demo/DemoController.java](src/main/java/demo/DemoController.java#L38)** file. Sign up for a [free trial](https://pdfcrowd.com/user/sign_up/?pid=api-trial2) if you don't have the credentials.

## Installing

```
./gradlew build
```

## Web server start

```
java -jar build/libs/pdfcrowd-demo-0.1.0.jar
```

## Test

   Open a sample web page <http://localhost:8080/>

   Invoke a conversion to PDF by pressing buttons at the bottom of the page.

## Documentation

* API Home:  <https://pdfcrowd.com/doc/api/>
* API Reference:  <https://pdfcrowd.com/doc/api/html-to-pdf/java/>
