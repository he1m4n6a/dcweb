#!/bin/bash
cd /dcweb
nohup python manage.py runserver 0.0.0.0:8888 &
