# Pdfcrowd & Ruby on Rails Demo

Sample for dynamic and static HTML to PDF conversions.

### Prerequisites

```
ruby
ruby-dev
ruby-bundler
```

Replace **'your_username'** with your Pdfcrowd username and **'your_apikey'** with your Pdfcrowd API key in **[app/controllers/demo_controller.rb](app/controllers/demo_controller.rb#L39)** file. Sign up for a [free trial](https://pdfcrowd.com/user/sign_up/?pid=api-trial2) if you don't have the credentials.

## Installing

```
gem install rails
bundle install
```

## Web server start

```
rails server
```

## Test

   Open a sample web page <http://localhost:8080/>

   Invoke a conversion to PDF by pressing buttons at the bottom of the page.

## Documentation

* API Home:  <https://pdfcrowd.com/doc/api/>
* API Reference:  <https://pdfcrowd.com/doc/api/html-to-pdf/ruby/>
