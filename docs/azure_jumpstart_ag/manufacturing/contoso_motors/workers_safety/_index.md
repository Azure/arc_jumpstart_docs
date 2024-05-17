---
type: docs
weight: 5
title: Enabling AI at the Edge to enhance workers safety
linkTitle: Enabling AI at the Edge to enhance workers safety
summary: |
    The enabling AI at the Edge to enhance workers safety page provides an overview of how Contoso Motors leverages AI to ensure workers' safety by detecting workers with no helmets on the factory floor. It describes the architecture and flow of information for detecting and classifying helmet adherence using AI. The page also explains the steps involved in the inference process, including UI selection, RTSP video simulation, frame capturing, image pre-processing/inferencing, and post-processing/rendering.
serviceOrPlatform: Manufacturing
technologyStack:
  - AKS
  - OPENVINO
  - AI
  - AKS EDGE ESSENTIALS
  - RTSP
---

# Enabling AI at the Edge to enhance workers safety

## Overview

Contoso Motors uses AI-enhanced computer vision to improve workers' safety by detecting workers with no helmets on the factory floor. Workers safety is one of the four computer vision use cases that Contoso Motors uses, which also include object detection, and human pose estimation. While each use case has its own unique characteristics, they all follow the same inferencing architecture pattern and data flow.

## Architecture

![Welding defect archietcture](./img/flow.png)

### Model

#### Inputs

#### Outputs

## Operation technology (OT) Manager Experience

Contoso leverages their AI-enhanced computer vision to monitor the safety helmet adherence for workers on the factory floor to help OT managers ensure workers safety through the "Control Center" interface.

- To access the "Control Center" interface, select the Control center [_env_] option from the _Control center_ Bookmarks folder. Each environment will have it's own "Control Center" instance with a different IP. Select one of the sites and click on the factory image to start navigating the different factory control centers.

![Screenshot showing the Control center Bookmark](./img/control-center-menu.png)

- Click on the "Site" control center.

  ![Screenshot showing the two Control centers](./img/control-center-site.png)

- Click on the "Workers safety" control center image.

  ![Screenshot showing the workers safety control center](./img/control-center-workers-safety.png)

- You can now see the AI-enhanced computer vision in action analyzing the video feed to detect if workers are adhering to Contoso's safety helmet policies in the factory floor.

  ![Screenshot showing the helmet detection monitoring feed](./img/control-center-helmet-detection.png)

## Next steps

Now that you have completed the workers safety scenario, it's time to continue to the next scenario, [Infrastructure observability for Kubernetes and Arc-enabled Kubernetes](../k8s_infra_observability/).
