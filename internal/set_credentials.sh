#!/bin/bash -e

set -u

THIS_DIR=`dirname $(readlink -f "$0")`
PROJECT_DIR=$THIS_DIR/..

USERNAME=$1
APIKEY=$2

for SRC in php/php/index.php \
               java/spring/src/main/java/demo/DemoController.java \
               nodejs/nodejs/server.js \
               nodejs/express/app.js \
               python/django/demo/views.py \
               dotnet/asp-net-web-forms/Default.aspx.cs \
               ruby/rails/app/controllers/demo_controller.rb
do
    SRC=$PROJECT_DIR/$SRC
    sed -i s/your_username/$USERNAME/g $SRC
    sed -i s/your_apikey/$APIKEY/g $SRC
done
