#!/bin/bash

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/hello.py   /etc/gunicorn.d/hello.py
#sudo ln -sf /home/box/web/ask/ask/wsgi.py   /etc/gunicorn.d/ask.py
