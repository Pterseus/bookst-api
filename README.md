# Markdown to JSON API

Run the server with:

```bash
fastapi dev main.py
```

## Packaging for AWS Lambda

Install required dependencies into a lib directory:

```bash
pip install -t lib -r requirements.txt
```

Zip the dependencies into `lambda_function.zip`:

```bash
(cd lib; zip ../lambda_function.zip -r .)
```

Add your FastAPI file and any other necessary files:

```bash
zip lambda_function.zip -u main.py
```
