# Unit Conversion Microservice

CS361 microservice that converts values between units over a REST API with JSON.

## Assigned teammates

- Person 2
- Person 3
- Person 4
- Person 5

## Communication pipe

Other programs submit a value, source unit, and target unit. The service calculates the conversion and returns the result as JSON.

### How other programs request data

Send a **GET** request to `/convert`.

Example:

```bash
curl "http://localhost:5003/convert?value=10&from=ft&to=m"
```

Query parameters:

| Param | Meaning |
|-------|---------|
| `value` | Number to convert |
| `from` | Source unit |
| `to` | Target unit |

## How to run

1. Python 3.10+
2. From this folder:

```bash
pip install -r requirements.txt
python app.py
```

Service runs on `http://localhost:5003`.

## Project status

Starter scaffold with a small length-conversion table. Teammates should expand supported units and categories (weight, volume, temperature, etc.).
