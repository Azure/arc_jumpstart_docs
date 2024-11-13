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

The Shopper Insights System is an advanced computer vision solution that provides real-time analytics about shopper behavior using video feeds. The system leverages OpenVINO™ for efficient AI model inference and provides detailed metrics about customer movements, demographics, and interactions within defined areas.
Key Features

### Real-time Person Detection

- Tracks multiple people simultaneously
- Maintains unique IDs for each detected person
- Processes video feeds at optimized FPS rates

### Person Re-identification (ReID) Technology
Person re-identification is a critical computer vision task that involves recognizing and tracking the same individual across different camera views or time periods. In our system, we use the following approach:
How ReID Works

### Feature Extraction

When a person is detected, the system extracts a unique feature vector (embedding)
These features capture distinctive characteristics like:

- Clothing patterns and colors
- Body shape and proportions
- Appearance attributes

### Feature Matching

New detections are compared with existing tracks using cosine distance
Distance threshold: 0.3 (configured in max_distance_threshold)
Lower distance indicates higher similarity

### Track Management

Each person gets a unique hash ID (8 characters)
Tracks are maintained for up to 60 frames (max_frames_to_track)
System handles track creation, updates, and termination

### Models Used
1. Person Detection Model
Model: person-detection-retail-0013

Purpose: Detects people in video frames
Architecture: MobileNetV2-like backbone with FPN and SSD head
Input: Images of 320×320 pixels
Output: Bounding boxes with confidence scores
Performance:

- High accuracy for retail environments
- Minimum confidence threshold: 0.6 (min_detection_confidence)

2. Person Re-identification Model
Model: person-reidentification-retail-0287

Purpose: Generates unique feature vectors for tracked individuals
Architecture: ResNet50 backbone optimized for ReID
Input: Cropped person images
Output: 256-dimensional feature vector
Features:

- Optimized for retail scenarios
- Robust to viewpoint changes
- Handles partial occlusions

3. Age Recognition Model
Model: age-gender-recognition-retail-0013

Purpose: Estimates age of detected persons
Architecture: Based on VGG-16 architecture
Input: Face/person crops
Output: Age estimation (0-100 years)
Features:

- Groups ages into decades for statistics
- Provides real-time demographic insights

### Area Analytics

- Supports multiple detection areas
- Tracks entry/exit times for each area
- Maintains current and total visitor counts

### Demographics Analysis

- Age detection for each detected person
- Age group statistics and trends
- Historical data aggregation

- Data pipeline to MQ

### Jump to other Contoso Hypermarket guides

[Deployment](../deployment/_index.md)
[Commercial gen-AI](../cerebral/_index.md)
[Observability](../observability/_index.md)
[Predictive Analytics](../predictive_analytics/_index.md)
[Speech-to-Text](../speech_to_text/_index.md)
[Cleanup](../cleanup/_index.md)
[Troubleshooting](../troubleshooting/_index.md)
