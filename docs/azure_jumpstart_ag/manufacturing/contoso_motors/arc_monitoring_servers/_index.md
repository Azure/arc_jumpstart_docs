---
type: docs
weight: 7
title: Infrastructure observability for Arc-enabled servers using Azure Monitor
linkTitle: Infrastructure observability for Arc-enabled servers using Azure Monitor
summary: |
    Infrastructure observability is key for Contoso Motors to understand the performance and the health of their Arc-enabled servers. This is where Azure Monitor steps in, playing a crucial role in providing visibility into every aspect of their Arc-enabled servers ecosystem.
serviceOrPlatform: INFRASTRUCTURE
technologyStack:
  - AZURE ARC
  - AZURE MONITOR
---

# Infrastructure observability for Arc-enabled servers using Azure Monitor

## Overview

Infrastructure observability is crucial for Contoso Motors to understand the performance and health of their Arc-enabled servers. This is where [Azure Monitor](https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/hybrid/arc-enabled-servers/eslz-management-and-monitoring-arc-server) steps in, playing a vital role in offering visibility into every facet of their Arc-enabled servers ecosystem.

Azure Monitor empowers Contoso with the capability to monitor and gather telemetry data from their Arc-enabled servers. It serves as a central hub, providing near real-time insights into server performance, health, and resource utilization. Azure Monitor offers a comprehensive view of the entire infrastructure, ensuring proactive identification and resolution of potential issues.

## Enable and configure Azure Monitor

Azure Monitor can collect data directly from your Arc-enabled servers into a Log Analytics workspace for detailed analysis and correlation. It requires installing the Azure Monitor Agent (AMA) VM extension on your Arc-enabled servers, enabling VM insights to collect data from your machines.

As part of the automated deployment, an Azure Policy monitoring initiative and a Data Collection Rule (DCR) are deployed. They allow collecting monitoring data from your Arc-enabled servers.

Follow these steps to verify that these required Azure Monitor artifacts have been successfully deployed:

- In the top bar of the Azure portal, search for **policy** and click on **Policy**:

    ![Screenshot of searching Azure Policy](./img/search_policy.png)

- Click on **Assignments**. You will see the Azure Policy initiative **(Ag) Enable Azure Monitor for Hybrid VMs with AMA**. This initiative enables Azure Monitor for the hybrid virtual machines with AMA. It takes a Log Analytics workspace as and a Data Collection Rule (DCR) as parameters.

    ![Screenshot of Azure Monitor initiative assignment Azure Policy](./img/azure_monitor_initiative.png)

- The DCR is in charge of collecting monitoring data from the Arc-enabled servers. In the top bar, search for **Data collection rules**:

    ![Screenshot of searching Data Collection Rules](./img/search_dcr.png)

- You will find the DCR that has been created to collect insights from the Arc-enabled servers:

    ![Screenshot of the Data Collection Rules](./img/dcr_vmi.png)

- Click on the DCR. You will see the data sources collected, in this case, performance counters:

    ![Screenshot of the DCR - Data sources](./img/dcr_datasources.png)

## Arc-enabled servers and Azure Monitor VM insights Integration

Now that we have checked that the required monitoring artifacts have been successfully enabled, it's time to leverage VM insights. It monitors the performance of your Arc-enabled servers by collecting the required data with AMA.

- Search for **Azure Arc**, go to **Machines** and click in one of your **Arc-enabled servers**:

    ![Screenshot of searching for an Arc-enabled server](./img/search_arc_server.png)

- Click on **Insights** and then on **Performance**. You will find a set of performance charts that target several key performance indicators to help you determine how well your Arc-enabled server is performing. The charts show resource utilization over a period of time:

    ![Screenshot of VM insights - Performance](./img/vminsights_performance.png)

## Operating System (OS) Performance Workbook

An Azure Workbook for Operating System (OS) Performance is also available as part of the deployment. It complements the views provided by VM insights.

- Search for **workbooks** and click on **Azure workbooks**:

  ![Screenshot of searching for Azure Monitor workbooks](./img/search_workbooks.png)

- Click on the workbook whose name contains **Arc-enabled servers OS Performance** and then click on **Open workbook**:

  ![Screenshot of searching for clicking on OS Performance Workbook](./img/click_osworkbook.png)

  ![Screenshot of opening OS Performance workbook](./img/open_osworkbook.png)

- You will find a table that summarizes the OS performance status for your servers (CPU, Memory and Disk):
  
  ![Screenshot of summary OS Performance table](./img/summarize_osworkbook.png)

- If you scroll down, you can use the charts and tables available per each key performance counter:

  ![Screenshot of summary OS Performance table](./img/cpuusage_osworkbook.png)

## Arc-enabled resources inventory Workbook

The second Azure Workbook functions as an inventory report detailing the various Arc-enabled resources that have been deployed.

- Search for **workbooks** and click on **Azure workbooks**:

  ![Screenshot of searching for Azure Monitor workbooks](./img/search_workbooks.png)

- Click on the workbook whose name contains **Arc-enabled resources inventory** and then click on **Open workbook**:

  ![Screenshot of searching for clicking on Inventory Workbook](./img/click_inventoryworkbook.png)

  ![Screenshot of opening Inventory workbook](./img/open_inventoryworkbook.png)

- You will find the first inventory for **Machines overall status and configurations**, which counts the number of machines by type and by their status:

  ![Screenshot of inventory workbook machines overall status and configurations](./img/machinesoverall_inventoryworkbook.png)

- The second and third inventories list your **Arc-enabled servers** and your **Arc-enabled Kubernetes clusters**. It provides information about the status, Arc agent version, the operating system, location, and the number of compliant and non-compliant policies.

  ![Screenshot of inventory workbook arc servers and kubernetes clusters](./img/arcserverskubernetesclusters_inventoryworkbook.png)

- There is also an inventory for checking the **Updates Data** of the servers:

  ![Screenshot of inventory workbook updates data](./img/updatesdata_inventoryworkbook.png)

- The last inventory will list any **Defender for Cloud active alerts**:

  ![Screenshot of inventory workbook arc servers and kubernetes clusters](./img/defenderalerts_inventoryworkbook.png)

## Next steps

Now that you have successfully completed all of the Contoso Motors scenarios, continue to the next step to learn how to [cleanup the deployment](../cleanup/).
