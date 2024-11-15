# Jumpstart Cerebral - Appendix

## Prompt examples

The following table details the various Cerebral user prompt examples:

| Type of Query         | Example Question                                | Sample Response                       |
|-----------------------|-------------------------------------------------|---------------------------------------|
| Technical Support     | "The cash dispenser in POS-01 is stuck. How do I fix it?" | ![Technical support Example](./img/technical-support-example.png) |
| Sales Analysis        | "What are our top 5 selling products this week?" | ![Sales Analysis Example](./img/sales_analyst_example.png) |
| Equipment Monitoring  | "What's the power usage for HVAC unit 02?"      | ![Equipment monitoring](./img/equipment_monitoring.png) |
| Inventory Management  | "Show me all products below reorder threshold"  | ![Inventory management](./img/inventory.png) |

## MQTT simulated equipment metrics

The following table details the various types and metrics being simulated through MQTT for Contoso Hypermarket's operations:

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

## Relational database structure

The following table details the relational database structure used by Contoso Hypermarket for commercial and operational data:

| Table Name     | Description               | Key Fields                                                                                                           | Example Data                                                                                   |
|----------------|---------------------------|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Sales          | Transaction records       | - sale_id VARCHAR(50) <br> - sale_date DATETIME2 <br> - store_id VARCHAR(10) <br> - store_city VARCHAR(100) <br> - product_id VARCHAR(50) <br> - quantity INT <br> - item_total DECIMAL(10,2) <br> - payment_method VARCHAR(50) <br> - customer_id VARCHAR(50) <br> - register_id VARCHAR(20) | - 'SAL20240312001' <br> - '2024-03-12 14:30:00' <br> - 'SEA' <br> - 'Seattle' <br> - 'PROD001' <br> - 2 <br> - 4.99 <br> - 'credit_card' <br> - 'CUST123' <br> - 'REG01' |
| Products       | Product catalog           | - product_id VARCHAR(50) <br> - name VARCHAR(200) <br> - category VARCHAR(100) <br> - price_min DECIMAL(10,2) <br> - price_max DECIMAL(10,2) <br> - stock INT <br> - photo_path VARCHAR(500) | - 'PROD001' <br> - 'Red Apple' <br> - 'Fruits' <br> - 0.20 <br> - 0.40 <br> - 1000 <br> - '/img/products/apple.jpg' |
| Inventory      | Current stock levels      | - id INT <br> - date_time DATETIME2 <br> - store_id VARCHAR(10) <br> - product_id VARCHAR(50) <br> - retail_price DECIMAL(10,2) <br> - in_stock INT <br> - reorder_threshold INT <br> - last_restocked DATETIME2 | - 1 <br> - '2024-03-12 15:00:00' <br> - 'SEA' <br> - 'PROD001' <br> - 0.35 <br> - 850 <br> - 200 <br> - '2024-03-11 08:00:00' |
| Stores         | Store locations           | - store_id VARCHAR(10) <br> - city VARCHAR(100) <br> - state VARCHAR(50) <br> - country VARCHAR(100)                       | - 'SEA' <br> - 'Seattle' <br> - 'WA' <br> - 'United States'                                           |
| DeviceMetrics  | Equipment telemetry history | - id INT <br> - timestamp DATETIME2 <br> - device_id VARCHAR(50) <br> - equipment_type VARCHAR(50) <br> - metric_name VARCHAR(100) <br> - metric_value DECIMAL(18,4) <br> - metric_unit VARCHAR(20) | - 1 <br> - '2024-03-12 15:01:00' <br> - 'HVAC01' <br> - 'HVAC' <br> - 'temperature' <br> - 22.5 <br> - 'celsius' |

## Available technical manuals

The following table details the current available technical manuals used by Contoso Hypermarket for operational needs:

| System | Description | Documentation |
|--------|-------------|---------------|
| Automated Checkout | Complete guide for operation and maintenance of self-checkout systems | [User Manual](https://download.microsoft.com/download/3ae1d7aa-a642-48cf-b848-67b4eaa81292/Automated%20Checkout%20System%20User%20Manual%20for%20Contoso%20Hypermarket.pdf) |
| SmartShelf | Technical documentation for electronic shelf labeling and inventory tracking | [User Manual](https://download.microsoft.com/download/3ae1d7aa-a642-48cf-b848-67b4eaa81292/SmartShelf%20System%20User%20Manual%20for%20Contoso%20Hypermarket.pdf) |
| Refrigeration | Maintenance and operation guides for refrigeration units | [User Manual](https://download.microsoft.com/download/3ae1d7aa-a642-48cf-b848-67b4eaa81292/Refrigeration%20System%20User%20Manual%20for%20Contoso%20Hypermarket.pdf) |
| HVAC | Environmental control system documentation | [User Manual](https://download.microsoft.com/download/3ae1d7aa-a642-48cf-b848-67b4eaa81292/HVAC%20System%20User%20Manual%20for%20Contoso%20Hypermarket.pdf) |
| Scale Systems | Calibration and operation procedures for weighing equipment | [User Manual](https://download.microsoft.com/download/3ae1d7aa-a642-48cf-b848-67b4eaa81292/Scale%20System%20User%20Manual%20for%20Contoso%20Hypermarket.pdf) |

## Industry and Role support

The following table details the current supported industries and roles by Cerebral:

| Industry | Roles | Examples |
|----------|-------|----------|
| Retail | - Store Manager<br>- Inventory Manager<br>- Maintenance Worker | - Store performance metrics<br>- Stock level monitoring<br>- Equipment maintenance |
| Manufacturing | - Maintenance Engineer<br>- Shift Supervisor<br>- Production Manager | - Machine diagnostics<br>- Production line metrics<br>- Quality control data |
| Automotive | - Line Supervisor<br>- Quality Inspector<br>- Maintenance Technician | - Assembly line monitoring<br>- Quality assurance checks<br>- Equipment maintenance |
| Hypermarket | - Store Manager<br>- Shopper<br>- Maintenance Worker | - Sales analytics<br>- Product location<br>- Facility maintenance |

## Common prompts Cerebral can handle

| Category | Prompt Example | Expected Response Type |
|----------|--------------|----------------------|
| Documentation and Procedures | _"What are the steps to close the store at the end of the day?"_ | Step-by-step procedure with checklist |
|| _"How do I perform the daily cleaning routine for the meat department?"_ | Detailed cleaning protocol with safety guidelines |
|| _"What's the emergency shutdown procedure for the refrigeration system?"_ | Emergency procedure with critical steps highlighted |
|| _"Show me the maintenance checklist for the automated checkout machines"_ | Maintenance checklist with technical specifications |
|| _"What are the safety protocols for handling spills in the produce area?"_ | Safety guidelines and cleaning procedures |
| Real-time Operations | _"What's the current capacity of all automated checkouts in use?"_ | Real-time usage metrics and availability status |
|| _"Show me the temperature trends for all refrigeration units in the last hour"_ | Temperature graphs and anomaly indicators |
|| _"Are any SmartShelves reporting low stock alerts right now?"_ | Current stock alerts and locations |
|| _"What's the average wait time at the deli counter currently?"_ | Current wait times and historical comparison |
|| _"How is HVAC-02 performing compared to its normal baseline?"_ | Performance metrics with baseline comparison |
| Commercial Data | "Which products in the dairy section need restocking?"_ | List of products below threshold with quantities |
|| _"What was our busiest hour for sales yesterday?"_ | Sales volume analysis with peak times |
|| _"Show me the performance of our seasonal products this month"_ | Sales trends and inventory analysis |
|| _"What's the current inventory level for fresh produce?"_ | Current stock levels with reorder recommendations |
|| _"Which payment method was most used in the last week?"_ | Payment method breakdown with percentages |
