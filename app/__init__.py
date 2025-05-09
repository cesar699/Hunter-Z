from flask import Flask
from flask_cors import CORS
from redis import Redis
from celery import Celery

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    class ContextTask(celery.Task):
        def __call__(self,*args,**kwargs):
            with app.app_context():
                return super().__call__(*args,**kwargs)
    celery.Task = ContextTask
    return celery

def create_app(config_object=None):
    app = Flask(__name__)
    app.config.from_object(config_object or 'app.config.Config')
    CORS(app)

    # 蓝图注册
    from .routes import proxy, download, metrics
    app.register_blueprint(proxy.bp)
    app.register_blueprint(download.bp)
    app.register_blueprint(metrics.bp)

    # 启动监控线程
    from .services import metrics as metrics_service
    metrics_service.start_collector(app)

    app.celery = make_celery(app)
    return app
