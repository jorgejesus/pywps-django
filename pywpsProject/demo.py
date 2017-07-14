#!/usr/bin/env python3

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pywpsProject.settings")
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application 

#WSGI
application = get_wsgi_application()


if __name__ == "__main__":
    
    import argparse
    parser = argparse.ArgumentParser(
        description="""Script for starting an example PyWPS using django and runserver""",
        epilog="""Do not use this service in a production environment.
         It's intended to be running in test environment only!
        For more documentation, visit http://pywps.org/doc
        """
        )
    parser.add_argument('-p', '--port', help="Port to run Django serverm, otherwisse defaul:8000", type=int, default=8000)
    parser.add_argument('-a','--all-addresses',
                        action='store_true', help="runserver using IPv4 0.0.0.0 (all network interfaces),"  +  
                            "otherwise bind to 127.0.0.1 (localhost)") 
    args = parser.parse_args()
    
    if args.all_addresses:
        bind_host='0.0.0.0'
    else:
        bind_host='127.0.0.1'

    if args.port:
        bind_port = args.port
   
    call_command('runserver',  str(bind_host)+ ":" + str(bind_port) )        



