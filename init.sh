#!/bin/bash
sudo ln -sf /home/dubrovskiy/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx stop
sudo /etc/init.d/nginx start
