# Pywps-Django
PyWPS demo using django. Using WSGI apllication from PyWPS as a Django view (sort of WSGI wrapping around another WSGI) 

## Installation
Python dependencies are listed in the ``requirements.txt``  file. You can install them using pip:

```bash
$ pip3 install -r requirements.txt
```

This will add a src/ folder that will contain pywps and other code necessary to run the demo

## Running

Two options, calling the ``demo.py`` script on folder ``pywpsProject``
```bash
$ python3 demo.py
```

Or using Django's ``manage.py``:

```bash
$ python3 manage.py runserver
```




 

