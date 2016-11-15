sudo ln -sf /home/leonid/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/leonid/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/leonid/web/etc/ask.py /etc/gunicorn.d/ask.py
sudo /etc/init.d/gunicorn restart
