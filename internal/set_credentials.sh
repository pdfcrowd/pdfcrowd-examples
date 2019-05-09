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
               ajax/post_request.js \
               dotnet/asp-net-web-forms/Default.aspx.cs \
               ruby/rails/app/controllers/demo_controller.rb
do
    SRC=$PROJECT_DIR/$SRC
    sed -i s/demo/$USERNAME/g $SRC
    sed -i s/ce544b6ea52a5621fb9d55f8b542d14d/$APIKEY/g $SRC
done
