mport os, sys 
mport django.core.handlers.wsgi
apache_configuration=os.path.dirname(__file__)
project=os.path.dirname(apache_configuration)
workspace=os.path.dirname(project)
sys.path.append(workspace)
sys.path.append('/usr/lib/python2.7/dist-packages/')
sys.path.append('/home/arkusc/www/www/')
os.environ['DJANGO_SETTINGS_MODULE']='www.setiings'
application=dsjango.core.handlers.wsgi.WSGIHandler()
