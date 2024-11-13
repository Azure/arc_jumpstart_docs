---
type: docs
weight: 2
title: Shopper Insights using computer vision
linkTitle: Shopper Insights using computer vision
---

## Enhance store operations and boost sales with AI-enhanced shopper insights

Contoso Hypermarket uses computer vision to enhance the customer in-store experience and to provide advanced business insights that can make store operations more efficient, increase sales, and streamline operations. In-store cameras detect shopper behavior such as foot traffic, time spent in certain zones of the store, and shopper-specific identifiers that personalize the shopping experience.

### Shopper insights for store managers

Store managers can view foot traffic for a store using the Store Manager dashboard. his includes identifying high traffic areas within the store, which helps in optimizing store layout and product placement. In-store cameras can be mapped to specific "zones" which are then used to sort foot traffic into specific groups of shopper foot traffic.

![A screenshot showing the store manager dashboard](./img/placeholder.png)

#### Configure floor plan and zones

 and patterns using the store manager interface of the Contoso Hypermarket web application. T The manager can also configure cameras and zones for computer vision, ensuring that the system accurately captures and analyzes shopper movements. This setup allows the store manager to make data-driven decisions to enhance the shopping experience and improve store operations.

#### Configure cameras and regions

The specific region of the camera field-of-view that will be sent for inferencing can be controlled on a per-camera basis.

### Regional Manager / Data Analyst

The regional manager will leverage the footfall and shopper insights data from various stores through aggregated dashboards in Fabric. These dashboards provide a comprehensive view of shopper behaviors and patterns across multiple locations, enabling the regional manager to identify trends and make informed decisions. By analyzing high traffic areas, peak shopping times, and customer preferences, the regional manager can optimize store layouts, improve product placement, and tailor marketing strategies to enhance the overall shopping experience. Additionally, the insights gathered from the dashboards help in identifying operational inefficiencies and areas for improvement, ensuring that each store operates at its best.

Further reading:

- [Observability](../observability/_index.md) - Visualize shopper foot traffic and behavior patterns in Grafana dashboards
- [Contoso Hypermarket edge-to-cloud data pipeline](../data_pipeline/_index.md) - Understand how individual store data is sent from edge-to-cloud and analyzed using Microsoft Fabric.

### Architecture

![A diagram depicting the shopper insights system architecture](./img/footfall_diagram.png)

#### Video inference pipeline

- Footfall API
- Shopper Insights API
- Data pipeline to MQ

### Jump to other Contoso Hypermarket guides

[Deployment](../deployment/_index.md)
[Commercial gen-AI](../cerebral/_index.md)
[Observability](../observability/_index.md)
[Predictive Analytics](../predictive_analytics/_index.md)
[Speech-to-Text](../speech_to_text/_index.md)
[Cleanup](../cleanup/_index.md)
[Troubleshooting](../troubleshooting/_index.md)
