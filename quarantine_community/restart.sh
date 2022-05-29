echo "stopping process..."
pkill -f gunicorn
fuser -k 8808/tcp
service nginx restart
sleep 0.5
gunicorn quarantine_community.wsgi:application -b 0.0.0.0:8808
echo "Webapp Started!"