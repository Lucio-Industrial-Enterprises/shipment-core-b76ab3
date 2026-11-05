# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a delivery quote
in USD. Zones are `local` and `regional`; weights must be positive.

| Service    | Local base | Regional base | Surcharge |
|------------|-----------|---------------|-----------|
| `standard` | $5.00     | $8.00         | —         |
| `express`  | $5.00     | $8.00         | +$7.00    |

All services add $1.50 per kg on top of the base. Unknown zones or services
raise `ValueError`.

### Command-line usage

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```
# Standard quote – 3 kg, local zone
python -m warehouse.cli 3 local
# $9.50

# Express quote – 3 kg, regional zone
python -m warehouse.cli 3 regional --service express
# $19.50
```
