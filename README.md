# thai-romanizer-api
Flask API to romanize Thai text using PyThaiNLP

# Thai Romanizer API

Simple Flask-based API to romanize Thai text using PyThaiNLP.

## Endpoints

- `POST /romanize`
  - Request JSON: `{ "text": "<Thai text>" }`
  - Response JSON: `{ "romanized": "<Thai romanization>" }`
