echo "stopping process..."
pkill -f gunicorn
fuser -k 80/tcp
systemctl reestart nginx
sleep 0.5
gunicorn -c conf/gunicorn_conf.py quarantien_community.wsgi --daemon
echo "Webapp Started!"