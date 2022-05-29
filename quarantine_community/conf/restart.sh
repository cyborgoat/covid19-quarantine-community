echo "stopping process..."
pkill -f gunicorn
fuser -k 80/tcp
service nginx restart
sleep 0.5
gunicorn -c conf/gunicorn_conf.py quarantien_community.wsgi --daemon
echo "Webapp Started!"