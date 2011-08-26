#!/bin/bash

python manage.py show_models 2> $(date +'%Y-%m-%d').dat 1> /dev/null