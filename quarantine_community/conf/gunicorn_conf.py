import multiprocessing

bind = "0.0.0.0:8808"   #绑定的ip与端口
workers = 4                #进程数
# errorlog = '/var/log/gunicorn/gunicorn.error.log' #发生错误时log的路径
# accesslog = '/var/log/gunicorn/gunicorn.access.log' #正常时的log路径
#loglevel = 'debug'   #日志等级
proc_name = 'quarantine_community'   #进程名