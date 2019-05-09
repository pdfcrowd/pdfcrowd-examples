# Pdfcrowd & Ruby on Rails Demo

Sample for dynamic and static HTML to PDF conversions.

### Prerequisites

```
ruby
ruby-dev
ruby-bundler
```

## Installing

```
gem install rails
bundle install
```

## Web Server Start

```
rails server -p 8080
```

## Test

   Open a sample web page <http://localhost:8080/>

   Invoke a conversion to PDF by pressing buttons at the bottom of the page.

## Pdfcrowd API License

   If you wish to use your Pdfcrowd API license, replace **demo** credentials with your Pdfcrowd username and API key in **[app/controllers/demo_controller.rb](app/controllers/demo_controller.rb#L45)** file.
   A [free trial](https://pdfcrowd.com/user/sign_up/?pid=api-trial2) API license can be used too.

## Documentation

* API Home:  <https://pdfcrowd.com/doc/api/>
* API Reference:  <https://pdfcrowd.com/doc/api/html-to-pdf/ruby/>
