"""Unit Conversion Microservice — Flask REST API."""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Length conversions (to meters)
TO_METERS = {
    "m": 1.0, "meter": 1.0, "meters": 1.0,
    "km": 1000.0, "kilometer": 1000.0, "kilometers": 1000.0,
    "cm": 0.01, "centimeter": 0.01, "centimeters": 0.01,
    "ft": 0.3048, "foot": 0.3048, "feet": 0.3048,
    "in": 0.0254, "inch": 0.0254, "inches": 0.0254,
}

# Weight conversions (to grams)
TO_GRAMS = {
    "g": 1.0, "gram": 1.0, "grams": 1.0,
    "kg": 1000.0, "kilogram": 1000.0, "kilograms": 1000.0,
    "lb": 453.592, "lbs": 453.592, "pound": 453.592, "pounds": 453.592,
    "oz": 28.3495, "ounce": 28.3495, "ounces": 28.3495,
}


@app.get("/convert")
def convert():
    value_raw = request.args.get("value")
    source = (request.args.get("from_unit") or request.args.get("from") or "").strip().lower()
    target = (request.args.get("to_unit") or request.args.get("to") or "").strip().lower()

    if value_raw is None or not source or not target:
        return jsonify({
            "error": "Query params required: value, from_unit, to_unit",
            "example": "/convert?value=225&from_unit=pounds&to_unit=kilograms",
        }), 400

    try:
        value = float(value_raw)
    except ValueError:
        return jsonify({"error": "value must be a number"}), 400

    if source in TO_GRAMS and target in TO_GRAMS:
        grams = value * TO_GRAMS[source]
        result = grams / TO_GRAMS[target]
    elif source in TO_METERS and target in TO_METERS:
        meters = value * TO_METERS[source]
        result = meters / TO_METERS[target]
    else:
        return jsonify({"error": "unsupported unit or mismatched categories"}), 400

    return jsonify({
        "original_value": value,
        "original_unit": source,
        "converted_value": round(result, 2),
        "converted_unit": target,
    })


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "unit-conversion"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)