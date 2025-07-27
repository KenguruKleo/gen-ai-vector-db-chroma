Init VENV
```
pipenv --python $(which python3.10) install
```

Activate VENV
```
source venv/bin/activate
```

Install packages
```
pip install -r requirements.txt
```

Update requirements.txt

```
pip freeze > requirements.txt
```