# Jumpstart Cerebral - Appendix

## MQTT simulated equipment metrics

The following table details the  types and metrics being simulated through MQTT for Contoso Hypermarket's operations:

> **Note**: The simulation generates realistic data streams for each device type, enabling testing, demonstrations, and development. Device IDs are formatted with sequential numbering (e.g., Refrigerator01, Refrigerator02). All metrics are published to the MQTT broker and InfluxDB and can be queried through Cerebral using natural language.

| Equipment Type     | Device Format         | Fields Monitored                                                                 | Example Metrics                              |
|--------------------|-----------------------|----------------------------------------------------------------------------------|----------------------------------------------|
| Refrigerator       | `Refrigerator{01..XX}`| - temperature_celsius<br>- door_open<br>- power_usage_kwh                         | - Current temperature<br>- Door status (open/closed)<br>- Power consumption |
| Scale              | `Scale{01..XX}`       | - weight_kg<br>- tare_weight_kg                                                   | - Current weight<br>- Tare weight settings   |
| POS                | `POS{01..XX}`         | - items_sold<br>- total_amount_usd<br>- payment_method<br>- failure_type          | - Transaction volume<br>- Sales amount<br>- Payment types<br>- Error states |
| SmartShelf         | `SmartShelf{01..XX}`  | - product_id<br>- stock_level<br>- threshold_stock_level<br>- last_restocked      | - Current inventory<br>- Stock thresholds<br>- Restock timing |
| HVAC               | `HVAC{01..XX}`        | - temperature_celsius<br>- humidity_percent<br>- power_usage_kwh<br>- operating_mode | - Air temperature<br>- Humidity levels<br>- Energy usage<br>- Mode (heating/cooling) |
| LightingSystem     | `LightingSystem{01..XX}` | - brightness_level<br>- power_usage_kwh<br>- status                               | - Light intensity<br>- Power consumption<br>- Operational status |
| AutomatedCheckout  | `AutomatedCheckout{01..XX}` | - items_scanned<br>- total_amount_usd<br>- payment_method<br>- errors<br>- queueLength<br>- avgWaitTime | - Scanning activity<br>- Transaction values<br>- Error states<br>- Queue metrics |

