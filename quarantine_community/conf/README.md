# Run with Gunicorn

## Install Gunicorn

```shell
pip install gunicorn
ln -s /usr/local/python3/bin/gunicorn /usr/bin/gunicorn
```

## Config file

`project_name/conf/gunicorn_conf.py`
```python
import multiprocessing

bind = ["0.0.0.0:8199"]    # 与nginx配置的端口一致
chdir = "/usr/fin/test_blog/project_name"
timeout = 30
errorlog = "/usr/fin/test_blog/project_name/logs/error.log"
#accesslog = "/usr/fin/test_blog/project_name/logs/access.log"
#loglevel = 'debug'
proc_name = 'project_name'      # 工程名

keepalive = 6
timeout = 65
graceful_timeout = 10
worker_connections = 100

```

## Run

```shell
gunicorn -c project_name/gunicorn-config.py project_name.wsgi
# or
gunicorn --bind 0.0.0.0:8199 project_name.wsgi:application
```