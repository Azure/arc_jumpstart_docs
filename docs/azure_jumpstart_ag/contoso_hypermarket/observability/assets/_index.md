---
type: docs
weight: 5
title: Industrial assets observability
linkTitle: Industrial assets observability
---

# Industrial assets observability

## Overview

Maintenance workers, equipment managers, and production engineers at Contoso Hypermarket use real-time interactive dashboards to operate, monitor, maintain, and service all aspects of industrial assets such as refrigerators, HVAC. Real-time data and insights are available through dashboards they can proactively address potential issues, perform predictive maintenance, and ensure the optimal performance of industrial assets. This lowers downtime and extends the lifespan of the equipment.

Industrial assets data is collected and managed using [Azure IoT Operations](https://learn.microsoft.com/azure/iot-operations/overview-iot-operations) and sent through an [edge-to-cloud data pipeline](../../data_pipeline/) where it can then be visualized using [Grafana](https://grafana.com/) or other tools..

## View industrial assets health in the Contoso Hypermarket application

Maintenance workers and equipment managers can view the status and health of Contoso Hypermarket's critical production assets such as refrigerators, ovens, and [HVAC](https://en.wikipedia.org/wiki/Heating,_ventilation,_and_air_conditioning) units. Follow the instructions below to see this experience in action.

- Open Microsoft Edge on the _Ag-Client_VM_ desktop and then click on the bookmarks toolbar and find the bookmark folder for Main UI.

    ![A screenshot showing Microsoft edge and the bookmarks folder with the bookmarks for Main UI](./img/bookmarks.png)

- Click on the link for Maintenance Workers

    ![A screenshot showing the Contoso Hypermarket homepage](./img/homepage.png)

- In this screen, maintenance workers can view the health of ovens, refrigerators, and point-of-sale assets such as automated checkouts or smart shelves.

    ![A screenshot showing the maintenance worker dashboard](./img/maintenance_dashboard.png)

>**Note:** The suggested prompts user interface widgets at the top of the screen are cosmetic only and aren't implemented in this release of Contoso Hypermarket.

- Users can also interact with Contoso Hypermarket using natural language. Click on the [Jumpstart Cerebral](../../cerebral/) icon in the upper right to ask a question about the status of industrial assets.

    ![A screenshot showing Jumpstart Cerebral location in the app](./img/cerebral_icon.png)

## View industrial assets health in a Grafana dashboard

Users also have the ability to use [Grafana](https://grafana.com/) to build, view and customize dashboards for industrial assets telemetry.

- Open Microsoft Edge and click on the Grafana bookmark.

    ![A screenshot showing Microsoft Edge and the Grafana bookmark](./img/grafana_bookmark.png)

- Navigate to the Industrial Assets Health dashboard.

    ![A screenshot showing the Industrial Assets Health menu of dashboards](./img/grafana_menu.png)

- From this view, users can view real-time telemetry from industrial assets and filter by store and time dimension.

    ![A screenshot showing the industrial assets Grafana dashboard](./img/grafana_dashboard.png)

## Observability architecture components

The Contoso Hypermarket observability architecture uses [Azure IoT Operations](https://learn.microsoft.com/azure/iot-operations/overview-iot-operations) to collect and send industrial assets telemetry using MQTT, an industry standard protocol. Assets including refrigerators, ovens, HVACs, and retail smart shelves send telemetry through the [MQTT Broker](https://learn.microsoft.com/azure/iot-operations/manage-mqtt-broker/overview-iot-mq) using an [edge-to-cloud data pipeline](../../data_pipeline/operational/).

- [**Azure IoT Operations**](https://learn.microsoft.com/azure/iot-operations/overview-iot-operations): Facilitates the connection and management of IoT devices, enabling real-time monitoring and control of industrial assets.
- [**MQTT**](https://learn.microsoft.com/azure/iot-operations/manage-mqtt-broker/overview-iot-mq): A lightweight messaging protocol used for efficient communication between IoT devices and the cloud.
- [**Prometheus**](https://prometheus.io/docs/introduction/overview/): An open-source monitoring and alerting toolkit used to collect and store metrics from industrial assets.
- [**Grafana**](https://grafana.com/): A multi-platform open-source analytics and interactive visualization web application used to create dashboards and graphs from the metrics collected by Prometheus.
- [**Azure Arc-enabled Kubernetes**](https://learn.microsoft.com/azure/azure-arc/kubernetes/overview): Manage and configure Kubernetes clusters running anywhere using Azure.

![Screenshot of the architecture diagram for observability](./img/arch_diagram.png)

## Next steps

Now that you have completed the _Industrial assets_ scenario, it's time to continue to the next one, [Shopper insights observability](../shopper_insights/).
