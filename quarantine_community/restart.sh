echo "stopping process..."
pkill -f gunicorn
fuser -k 80/tcp
service nginx restart
sleep 0.5
#nohup gunicorn quarantine_community.wsgi:application -b 0.0.0.0:8808 &
gunicorn quarantine_community.wsgi:application -c /root/pyCharmProjects/quarantine_community/conf/gunicorn_conf.py --daemon
#gunicorn quarantine_community.wsgi:application -c /root/home/cyborgoat/pyCharmProjects/quarantine_community/conf/gunicorn_conf.py --daemon