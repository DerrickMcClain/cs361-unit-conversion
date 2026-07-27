"""Unit Conversion Microservice — Flask REST API starter."""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Minimal starter conversions — teammates should expand coverage.
TO_METERS = {
    "m": 1.0,
    "meter": 1.0,
    "meters": 1.0,
    "km": 1000.0,
    "kilometer": 1000.0,
    "kilometers": 1000.0,
    "cm": 0.01,
    "centimeter": 0.01,
    "centimeters": 0.01,
    "ft": 0.3048,
    "foot": 0.3048,
    "feet": 0.3048,
    "in": 0.0254,
    "inch": 0.0254,
    "inches": 0.0254,
}


@app.get("/convert")
def convert():
    """Convert a value from a source unit to a target unit.

    Query params:
      value  — number to convert
      from   — source unit
      to     — target unit

    Example:
      GET /convert?value=10&from=ft&to=m
    """
    value_raw = request.args.get("value")
    source = (request.args.get("from") or "").strip().lower()
    target = (request.args.get("to") or "").strip().lower()

    if value_raw is None or not source or not target:
        return (
            jsonify(
                {
                    "error": "Query params required: value, from, to",
                    "example": "/convert?value=10&from=ft&to=m",
                }
            ),
            400,
        )

    try:
        value = float(value_raw)
    except ValueError:
        return jsonify({"error": "value must be a number"}), 400

    if source not in TO_METERS or target not in TO_METERS:
        return (
            jsonify(
                {
                    "error": "unsupported unit",
                    "supported": sorted(set(TO_METERS.keys())),
                }
            ),
            400,
        )

    meters = value * TO_METERS[source]
    result = meters / TO_METERS[target]

    return jsonify(
        {
            "value": value,
            "from": source,
            "to": target,
            "result": result,
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "unit-conversion"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
