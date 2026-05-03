# BUCKETS
Buckets is a list making program made with python for linux

## BUILD DEPENDENCIES
* python3-dev
* pip
* setuptools
* cython
* gcc

## INSTALLATION
The installation is very simple, you only need to do this:
```
git clone https://github.com/bangkemono/buckets
cd buckets
cython --embed -o buckets.c buckets.py
gcc -Os $(python3-config --includes) buckets.c $(python3-config --ldflags --embed) -o buckets
sudo mv buckets /usr/local/bin/
```

then you're all good to go

## FEATURES TBA
* Windows Compatibility (WIP. For now, please use pyinstaller)
* Built-in list editor
