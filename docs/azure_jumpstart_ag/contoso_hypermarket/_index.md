---
type: docs
weight: 2
linkTitle: Contoso Hypermarket
description: >-
  Learn how Contoso Hypermarket, an international consumer goods distributor and retailer, implements an AI-enhanced cloud-to-edge strategy with computer vision, next-gen language models, data pipelines, Microsoft Fabric, and Azure Arc.
---

# Overview

Contoso Hypermarket, a leading international consumer goods distributor and retailer, is leading the digital transformation in the retail industry. By leveraging next-generation AI-powered shopper analytics solutions, Contoso Hypermarket employs advanced computer vision technologies to enhance customer experiences and optimize store operations.

By integrating advanced computer vision into their retail facilities, Contoso Hypermarket can analyze shopper behavior in real-time, providing valuable insights into customer preferences and shopping patterns. These insights enable them to tailor marketing strategies, optimize product placements, and improve inventory management, ensuring that customers find what they need quickly and efficiently.

The AI-powered solutions also enhance maintenance and operational efficiency. With real-time monitoring and analytics, Contoso Hypermarket can detect errors or anomalies with automated checkout activities, manage equipment and detect malfunctions. This innovative approach drives operational excellence, positioning Contoso Hypermarket as a leader in the retail sector.

> **Disclaimer:** This Jumpstart Agora scenario utilizes both Azure OpenAI and the _Phi-3-Mini-4K-Instruct_ model from Microsoft to enhance its capabilities in natural language processing and instruction-based interactions. The _Phi-3-Mini-4K-Instruct_ model is licensed under the MIT License, and users are encouraged to review the full license terms. For details, please refer to Arc Jumpstart [MIT License](https://github.com/Azure/arc_jumpstart_docs/blob/main/LICENSE) included in this repository.
> Additionally, this project uses Intel OpenVINO models, which are distributed under the Apache License 2.0. Please refer to the [Intel OpenVINO License](https://github.com/openvinotoolkit/openvino/blob/master/LICENSE) for the applicable terms and conditions governing its usage.

## Architecture and technology stack

Contoso Hypermarket uses an AI technology stack, services, and processes to support their digital transformation. A set of reference use-cases is included with the Jumpstart Agora Contoso Hypermarket scenario.

- **Retrieval-augmented generation** - Use natural language query (NLQ) to work with Contoso industrial assets, infrastructure and data to support frontline workers and corporate personnel.
- **Computer vision for shopper insights** - Computer vision using tuned inference models provides advanced shopper insights like foot traffic patterns, dwell time, product interaction, and demographic analysis.
- **Speech-to-Text** - Converts spoken language into written text to facilitate customer service interactions, transcribe meetings, and support voice-activated commands for in-store assistance.
- **IoT at the Edge** - Manages IoT devices and sensors at the edge with [Azure IoT Operations](https://learn.microsoft.com/azure/iot-operations/overview-iot-operations) to collect and process data in real-time, enabling predictive maintenance, inventory tracking, and enhanced operational efficiency.
- **Predictive inventory and operations analytics with Microsoft 365 Copilot** - Analyzes sales and inventory trends and provides forecasting insights for optimizing inventory and sales.
- **Edge-to-cloud data pipeline** - Seamless data integration between IoT devices at the edge, customer and business data, and [Microsoft Fabric](https://www.microsoft.com/microsoft-fabric), aggregating real-time shopper insights, centralized data management, predictive maintenance, and enhanced decision-making capabilities and enabling advanced data insights.

## Virtual sandbox edge environment

Jumpstart Agora provides virtual sandbox environments that simulate edge infrastructure deployments for industry solutions. The automation in the Contoso Hypermarket scenario deploys an Azure Virtual machine to support this "virtual" factory's AI technology. We have incorporated additional features to enhance the 'virtual industry' experience in a lab setting. These enhancements include simulated Real-Time Streaming Protocol (RTSP) feeds, data emulators, MQTT, industrial assets, and data. For more details about the virtual environment, please review the diagram and dedicated guides below.

![Screenshot of Contoso Hypermarket technology stack and operations architecture diagram](./deployment/img/architecture_diagram.png)

## Getting started

To get started with the "Contoso Hypermarket" Jumpstart Agora scenario, we provided you with a dedicated guide for each step of the way. The guides are designed to be as simple as possible but also keep the detailed-oriented spirit of the Jumpstart.

| **Guide**  | **Contoso Hypermarket service or platform** | **Technology stack** |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [Deployment guide](../contoso_hypermarket/deployment/) | Not applicable | Not applicable |
| [Shopper insights using computer vision](../contoso_hypermarket/shopper_insights/) | Real-time footfall inferences and shopper insights | Yolo8, RTSP, OpenCV, Rancher K3s, PostgreSQL, Azure Arc  |
| [Jumpstart Cerebral - Commercial and Operations assistance with Gen AI](../contoso_hypermarket/cerebral/) | Natural language query with Jumpstart Cerebral | Azure OpenAI, phi3, gpt35turbo, Rancher K3s, InfluxDB, Microsoft SQL Server on Linux |
| [Commercial and operations assistance with Speech-to-Text](../contoso_hypermarket/speech_to_text/) | Speech-to-Text  | Azure AI Speech, Rancher K3s, Azure Arc |
| [Industrial assets observability](../contoso_hypermarket/observability/assets/) | Observability | Prometheus, Grafana |
| [Shopper insights observability](../contoso_hypermarket/observability/shopper_insights/) | Observability | Prometheus, Grafana |
| [Kubernetes infrastructure observability](../contoso_hypermarket/observability/infrastructure/) | Observability | Arc-enabled Kubernetes, Rancher K3s, Prometheus, Grafana  |
| [Data pipeline and reporting for operational technology (OT)](../contoso_hypermarket/data_pipeline/operational/) | Operational technology (OT) | Azure IoT Operations, Microsoft Fabric, MQTT, Event Hub, Rancher K3s, InfluxDB, PostgreSQL, MQTT simulators |
| [Data pipeline and reporting for commercial sales](../contoso_hypermarket/data_pipeline/commercial/) | Operational technology (OT) | Azure IoT Operations, Microsoft Fabric, MQTT, Event Hub, Rancher K3s, InfluxDB, PostgreSQL, MQTT simulators |
| [Predictive analytics using Microsoft 365 Copilot](../contoso_hypermarket/predictive_analytics/) | Predictive inventory | Microsoft 365 Copilot |
| [Cleanup](../contoso_hypermarket/cleanup/) | Not applicable | Not applicable |
| [Troubleshooting](../contoso_hypermarket/troubleshooting/) | Not applicable  | Not applicable |
| [Frequently asked questions (FAQ)](../../faq/) | Not applicable  | Not applicable |
