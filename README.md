# Introduction

This is a demo project to show how to check code syntax. Supported languages are: Python/JavaScript/Java/C/CPP

## How to run

```bash
python check.py
```

## API concurrency test

```bash
pip install -r requirements.txt
flask --app flask_app run --debug
locust -f locustfile.py # then open http://127.0.0.1:8089/ to run test
```
