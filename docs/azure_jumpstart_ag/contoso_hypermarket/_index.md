---
type: docs
weight: 1
linkTitle: Contoso HyperMarket
description: >-
  Learn how Contoso HyperMarket, an international consumer goods distributor and retailer, implements an AI-enhanced cloud-to-edge strategy with computer vision, next-gen language models, data pipelines, Microsoft Fabric, and Azure Arc.
---

# Contoso HyperMarket overview

Contoso HyperMarket, an international consumer goods distributor and retailer, is at the forefront of the retail industry's digital transformation. Leveraging next-generation AI-powered shopper analytics solutions, Contoso HyperMarket utilizes advanced computer vision technologies to enhance customer experiences and optimize store operations.

By integrating advanced computer vision into their retail facilities, Contoso HyperMarket can analyze shopper behavior in real-time, providing valuable insights into customer preferences and shopping patterns. These insights enable them to tailor marketing strategies, optimize product placements, and improve inventory management, ensuring that customers find what they need quickly and efficiently.

The AI-powered solutions also enhance maintenance and operational efficiency. With real-time monitoring and analytics, Contoso HyperMarket can detect errors or anomalies with automated checkout activities, manage equipment and detect malfunctions. This innovative approach drives operational excellence, positioning Contoso HyperMarket as a leader in the retail sector.

## Architecture and technology stack

Contoso HyperMarket uses an AI technology stack, services, and processes to support their digital transformation. A set of reference use-cases is included with the Jumpstart Agora Contoso HyperMarket scenario.

- **Natural language querying with small language models** - Using SLMs at the edge for natural language query (NLQ) interaction with Contoso operations and connected systems and data to support frontline workers and corporate personnel.
- **Computer vision for shopper insights** - Computer vision using tuned inferencing models provides advanced shopper insights like foot traffic patterns, dwell time, product interaction, and demographic analysis.
- **Speech to text** - Converts spoken language into written text to facilitate customer service interactions, transcribe meetings, and support voice-activated commands for in-store assistance.
- **IoT at the Edge** - Manages IoT devices and sensors at the edge to collect and process data in real-time, enabling predictive maintenance, inventory tracking, and enhanced operational efficiency.
- **Predictive inventory and operations analytics with Microsoft Copilot** - Analyzes sales and inventory trends and provides forecasting insights for optimizing inventory and sales.
- **Edge-to-cloud data pipeline** - Seamless data integration between IoT devices at the edge, customer and business data, and Microsoft Fabric, aggregating real-time shopper insights, centralized data management, predictive maintenance, and enhanced decision-making capabilities and enabling advanced data insights.

## Virtual sandbox edge environment

Jumpstart Agora provides virtual sandbox environments that simulate edge infrastructure deployments for industry solutions. The automation in the Contoso HyperMarket scenario deploys an Azure Virtual machine to support this "virtual" factory's AI technology. Additional features are included to further enhance the "virtual industry" experience in a lab setting, including simulated Real-Time Streaming Protocol (RTSP) feeds, data emulators, MQTT, industrial assets, and data. Review the diagram and dedicated guides below to learn more about the virtual environment.

![Applications and technology stack architecture diagram](./img/simulation_stack.png)

## Getting started

To get started with the "Contoso HyperMarket" Jumpstart Agora scenario, we provided you with a dedicated guide for each step of the way. The guides are designed to be as simple as possible but also keep the detailed-oriented spirit of the Jumpstart.

| **Guide**  | **Contoso HyperMarket service or platform** | **Technology stack** |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [Deployment guide](../contoso_hypermarket/deployment/) | Not applicable | Not applicable |
| [Jumpstart Cerebral](../contoso_hypermarket/cerebral/) | Natural Language Query | Azure OpenAI, phi3, gpt35turbo, Rancher K3s, InfluxDB, Microsoft SQL Server on Linux |
| [Data pipeline and reporting across cloud and edge](../contoso_hypermarket/data_pipeline/) | Operational technology (OT) | Azure IoT Operations, Microsoft Fabric, MQTT, Event Hub, Rancher K3s, InfluxDB, PostgreSQL, MQTT simulators |
| [Web UI and Computer vision](../contoso_hypermarket/ai_inferencing/) | Computer vision | Yolo8, RTSP, OpenCV, Rancher K3s, PostgreSQL, Azure Arc  |
| [Speech-to-text](../contoso_hypermarket/speech_to_text/) | Customer service  | Azure AI Speech, Rancher K3s, Azure Arc |
| [Predictive analytics with Microsoft Copilot](../contoso_hypermarket/predictive_analytics/) | Predictive inventory | Microsoft Copilot |
| [Infrastructure observability for Kubernetes and Arc-enabled Kubernetes](../contoso_hypermarket/observability/) | Infrastructure | Arc-enabled Kubernetes, Rancher K3s, Prometheus, Grafana  |
| [Cleanup deployment](../contoso_hypermarket/cleanup/) | Not applicable | Not applicable |
| [Troubleshooting](../contoso_hypermarket/troubleshooting/) | Not applicable  | Not applicable |
| [Frequently asked questions (FAQ)](../../faq/) | Not applicable  | Not applicable |
