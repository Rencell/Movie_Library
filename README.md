# DjangoRestFramework
for practice

## Requirements for setup


### Go to mysite
```sh
cd mysite/
```

### Create virtual environment
```sh
python -m venv venv
```

### activate virtual environment (recommend to use command prompt and not powershell)
```sh
venv\Scripts\activate
```

### pip installs
```sh
pip install -r requirements.txt
```

### Database migrations
```sh
manage.py migrate
```

### Django run server
```sh
manage.py runserver
```

## Optionally after you build the frontend (kindly open frontend and read the README.md)

### Shell script command to run both Frontend and Backend
Open a terminal and switch to bash

### Change mode execution (NOTE: If you already type this, skip this and go to next step)
```sh
chmod +x start.sh
```

### Run the start.sh
```sh
./start.sh
```
