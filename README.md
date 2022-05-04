# Mini Docker Redirect

A minimal container running flask+gunicorn to redirect to a page. Ideal to host
a single short-url on your on domain to dynamically redirect (for example with a
QR code.)

To run, simply:

```bash
docker-compose up --build
```

or locally:

```bash
python -m pip install -r requirements.txt
DEBUG=1 python app/main.py # note the DEBUG=1 env variable
```
