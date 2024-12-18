---
type: docs
weight: 2
title: Data pipeline and reporting across cloud and edge
linkTitle: Data pipeline and reporting across cloud and edge
summary: |
  One of Contoso's biggest objectives is how to use the data coming from their factories and visualize it for business intelligence by leveraging the power of the cloud.

  In this scenario, Contoso wants to use their data pipeline so data from their different factories and production lines, flow to [Azure Data Explorer (ADX)](https://learn.microsoft.com/azure/data-explorer/data-explorer-overview) database and generate near real-time reports. By doing so, Contoso management can leverage these reports to adjust their inventory and supply chain based on the product demand from customers across multiple filters - factories, day, week, month, and year. This helps optimize Contoso resources, stores supplies, saves significant costs and at the same time improves customer satisfaction and trust.
serviceOrPlatform: Manufacturing
technologyStack:
  - AZURE DATA EXPLORER
  - AZURE EVENT HUB
  - AZURE EVENT GRID
---

# Data pipeline and reporting across cloud and edge

## Overview

One of Contoso's biggest objectives is how to use the data coming from their manufacturing assembly line, welding robots, battery assemblies and visualize it for business intelligence by leveraging the power of the cloud.

In this scenario, Contoso wants to use their data pipeline so that data coming from automobile parts manufactured at various plants flow to [Azure Data Explorer (ADX)](https://learn.microsoft.com/azure/data-explorer/data-explorer-overview) database and generate near real-time reports for production and operational efficiency. By doing so, Contoso management can leverage these reports to adjust their production, improve quality, reduce wastage, and save manufacturing cost.

## Architecture

Below is an architecture diagram that shows how the data flows from the manufacturing plant and into the ADX database to generate near real-time reports of production line, batteries, and welding equipment received and processed in a single manufacturing plant. This architecture includes a local InfluxDB, running at the edge in the plant, [Azure Event Grid](https://learn.microsoft.com/azure/event-grid/overview), [Azure Event Hub](https://learn.microsoft.com/azure/event-hubs/event-hubs-about), and ADX cluster in Azure cloud. MQTT broker at the edge receives event data from MQTT simulator and sends to Azure Event Grid in the cloud. Azure Event Grid routes these messages into Azure Event Hub. Data connection that is created in ADX cluster connects to Azure Event Hub and ingests data into ADX database for realtime analytics and dashboard reports.

![Screenshot showing the data pipeline architecture diagram](./img/contoso_motors_edge_data_architecture.png)

Below is an architecture diagram that shows how the data flows from the manufacturing plant and into the ADX database to generate near real-time reports of production line, batteries, and welding equipment received and processed across various manufacturing plants.

![Screenshot showing the data pipeline architecture diagram](./img/contoso_motors_datapipeline_architecture.png)

## Industrial telemetry at the edge

### MQTT Explorer

The automation deploys and configures a simulator that simulates data from various manufacturing equipment, such as cars assembly line, battery assembly line, and welding robots, including a dedicated simulation for a cars production line. The MQTT listener captures this data and funnels it to InfluxDB which is optimized for time-series data.

Grafana, a leading open-source platform for monitoring and observability, taps into InfluxDB to render comprehensive dashboards and analytics, enabling the plant staff at Contoso to monitor and enhance the performance of the cars production line effectively. Those dashboards provide near real-time information and insights, often projected directly within the production line area, to enable immediate response and decision-making where it matters most.

- Open the MQTT explorer desktop shortcut, it is already configured to connect to the MQTT listener on the cluster.

  ![Screenshot showing opening MQTT explorer on the desktop](./img/open_mqtt_explorer.png)

- Click _Connect_ to connect to MQTT listener. Once connected, you will start seeing simulated data being transmitted with various metrics from the plant assets.

  ![Screenshot showing the simulated data](./img/mqtt_explorer.png)

  ![Screenshot showing the simulated data](./img/mqtt_events_assembly_line.png)

  ![Screenshot showing the simulated data](./img/mqtt_events_welding_robot.png)

  ![Screenshot showing the simulated data](./img/mqtt_events_assembly_batteries.png)

### InfluxDB Dashboard Reports

Contoso supports InfluxDB dashboard reports for the manufacturing analytics and monitoring at the edge. These reports are created in InfluxDB to allow staff who are working locally at the manufacturing plant to view dashboards reports. These reports are generated based on live data received from the sensors directly into InfluxDB database.

These reports are readily available to access through Edge browser. Follow the steps below to access these reports on the Client VM.

- On the Client VM (_Ag-VM-Client_), open Edge browser, expand InfluxDB favorite collection and chose Detroit or Monterrey plants to view dashboard reports.

  ![Screenshot showing how to open InfluxDB dashboard reports](./img/influxdb_open_dashboard_reports.png)

- Login with the _admin_ username and password provided when you created the deployment.

  ![Screenshot showing how to login to InfluxDB dashboard reports](./img/influxdb_dashboard_reports_login.png)

- Click on Dashboards icon as shown in the screen below to view list of available dashboard reports. There are 3 dashboard reports created to show car assembly line, battery line, and welding energy consumption reports.

  ![Screenshot showing how to open InfluxDB dashboard reports](./img/influxdb_list_dashboard_reports.png)

  ![Screenshot showing how to open InfluxDB dashboard reports](./img/influxdb_dashboard_reports.png)

- Click on _Contoso Motors - Assembly Car Line_ dashboard report to view. Contoso staff can start monitoring the car assembly production line. The most critical KPI featured is the Assembly Robot Efficiency. The Efficiency indicator is color-coded for at-a-glance status updates:

  | Color   | Indication                                                        |
  | ------- | ------------------------------------------------------------------ |
  | Green   | 🟩 Efficiency above the target range of 90% (optimal performance)        |
  | Yellow  | 🟨 Efficiency between 80% to 90% (acceptable but suboptimal performance) |
  | Red     | 🟥 Efficiency below 80% (immediate attention needed)                     |

  ![Screenshot showing car assembly line dashboard reports](./img/influxdb_dashboard_assembly_car_line.png)

- Additionally, the dashboard breaks down the components of Assembly Car Line report; _Availability_, _Cars produced_, and _Staff on shift_, to provide a detailed analysis. A key focus is on _Availability_, with constant monitoring of downtime to identify and classify lost time reasons, such as equipment malfunctions.

- Click on _Contoso Motors - Battery Line_ dashboard report to view. Contoso staff can start monitoring the car battery assembly line KPIs featured in the dashboard report.

  ![Screenshot showing battery assembly line dashboard reports](./img/influxdb_dashboard_assembly_battery_line.png)

- Click on _Contoso Motors - Welding Energy Consumption_ dashboard report to view. Contoso staff can start monitoring the welding enerty consumption KPIs featured in the dashboard report.

  ![Screenshot showing welding energy consumption dashboard reports](./img/influxdb_dashboard_welding_energy_consumption.png)

## Contoso Motors ADX dashboard reports

Contoso supports dashboard reports for the manufacturing analytics and monitoring. These reports are created in ADX to allow users to view dashboards reports. These reports are generated based on live data received from the MQTT Broker into the ADX database using data integration.

## Manually import dashboards

Follow the below steps in order to view the Contoso Motors dashboard reports as you will need to import these into ADX.

- On the Client VM (_Ag-VM-Client_), open Windows Explorer and navigate to folder _C:\Ag\AdxDashboards_ folder. This folder contains ADX dashboard report JSON file _adx-dashboard-contoso-motors-auto-parts.json_ with the ADX name and URI updated when the deployment PowerShell logon script is completed.

  ![Screenshot showing the dashboard report template files location](./img/adx_dashboard_report_files.png)

- Copy this ADX dashboards report JSON file on your local machine in a temporary folder to import into ADX dashboards. Alternatively, you can log in to ADX Dashboards directly on the Client VM.

  > **Note:** Depending on the account being used to log in to the ADX portal, the Microsoft Entra ID tenant of that account may have conditional access policies enabled to allow access only from corporate-managed devices (for example managed by Microsoft Intune) and might prevent login to ADX Dashboards from the Client VM as this VM is not managed by your organization.

- On your local machine open the browser of your choice OR on the Client VM open the Edge browser and log in to [ADX Dashboards](https://dataexplorer.azure.com/). Use the same user account that you deployed Jumpstart Agora in your subscription. Failure to use the same account will prevent access to the ADX manufacturing database to generate reports.

- Once you are logged in to ADX dashboards, click on Dashboards in the left navigation to import the Contoso Motors dashboard report.

  ![Screenshot showing how to navigate to ADX dashboard reports](./img/adx_view_dashboards.png)

- Select _Import dashboard from file_ to select previously copied file from the Client VM to your local machine or the _C:\Ag\AdxDashboards_ folder on the Client VM.

  ![Screenshot showing the import dashboard file](./img/adx_import_dashboard_file.png)

- Choose to import the _adx-dashboard-contoso-motors-auto-parts.json_ file.

  ![Screenshot showing the dashboard report JSON file to import](./img/adx_select_dashboard_file.png)

- Confirm the dashboard report name, accept the suggested name (or choose your own), and click Create.

  ![Screenshot showing the dashboard report name confirmation](./img/adx_confirm_dashboard_report_name.png)

- By default, there is no data available in the ADX manufacturing database to display in the report after deployment. Click Save to save the dashboard report in ADX.

  ![Screenshot showing the empty data in Contoso Motors dashboard report](./img/adx_manufacturing_report_empty_data.png)

  > **Note:** Depending on the type of user account being used to access ADX dashboards, you might have issues accessing data in the _manufacturing_ database in the ADX cluster with an error _User principal 'msauser=xyz@abc.com' is not authorized to read database 'manufacturing'_. If you experience this access issue, refer to [Jumpstart Agora - Contoso Motors scenario troubleshooting](../troubleshooting/#user-principal-is-not-authorized-to-read-database-manufacturing) guide to troubleshoot and address this access issue.

## Generate sample data using Data Emulator

Once the Agora Contoso Motors scenarios is deployed and fully functions, MQTT simulators start sending assemblyline, battery, and welding data to Azure Event Hub and is ingested to ADX database using ADX database connection. While this data is realtime, it takes time to produce enough data to view dashboards reports, this scenario comes with a Data Emulator tool available on the Agora client VM. Data Emulator can produce data for past several days or weeks to view dashboard reports. Use instructions below to generate sample data using the Data Emulator tool.

- On the Client VM, locate Data Emulator icon on the desktop.

  ![Screenshot showing the Data Emulator on the desktop](./img/locate_data_emulator_desktop.png)

- Double click on the Data Emulator desktop icon to launch executable and generate sample data. Confirm by entering option **1** for past data or **2** to start generating current data. Select 1 to generate past data.

  > **Note:** You can still generate additional sample data by running this tool multiple times, but there might be duplicate key errors and fails to generate data in subsequent attempts.

- Enter no of days to generate past data until current date and time.

  ![Screenshot showing the sample data generation confirmation](./img/confirm_sample_data_generation.png)

  ![Screenshot showing the generating sample data](./img/confirm_sample_data_past_days.png)

  ![Screenshot showing the generating sample data](./img/sample_data_generation.png)

- Once the sample data generation is complete, from [ADX Dashboards](https://dataexplorer.azure.com/) open Contoso Motors and Auto Parts dashboard report to view simulated manufacturing data. Allow some time to propagate data into the ADX database using an integrated data pipeline.

  ![Screenshot showing the Contoso Motors with simulated data](./img/adx_contoso_motors_with_simulated_data.png)

- Contoso Motors dashboard report is configured to display data from the _"Last 1 hour"_ by default. To view all the simulated manufacturing data, change report time range to _"Last 7 days"_ as shown in the picture below. Dashboard report will refresh data and display reports for the selected time range.

  ![Screenshot showing the Contoso Motors select time range](./img/adx_contoso_motors_report_select_timerange.png)

  ![Screenshot showing the Contoso Motors with simulated data for selected time range](./img/adx_contoso_motors_with_simulated_data_selected_timerange.png)

  ![Screenshot showing the Contoso Motors with simulated data for production metrics](./img/adx_contoso_motors_production_metrics.png)

## Next steps

Now that you have completed the first data pipeline scenario, it's time to continue to the next scenario, [Web UI and AI Inference flow](../ai_inferencing/).
