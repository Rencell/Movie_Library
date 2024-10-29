#!/bin/bash

cd mysite/
source venv/Scripts/activate

python manage.py runserver &

cd ../frontend/Movie-interface || exit

npm run dev