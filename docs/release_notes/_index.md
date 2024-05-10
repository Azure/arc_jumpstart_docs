---
type: docs
title: "Jumpstart Release Notes"
linkTitle: "Jumpstart Release Notes"
weight: 6
---

# Arc Jumpstart release notes

> **Note:** Release notes will be released around the first week of each month and will cover the previous month.

## April 2024

### Release highlights

- New "Arc, Edge, and IoT Operations" scenario for Edge Storage Accelerator
- Multiple HCIBox features
- Various critical bugs fixes
- Jumpstart Assets - Arc Architecture Posters and Diagrams (APD) [April release](https://www.linkedin.com/feed/update/urn:li:activity:7188194418762420227/)

### Jumpstart HCIBox

- [Bug: HCIBox setup script failed due to incorrect parameter name "autoUpdateClusterResource" #2498](https://github.com/microsoft/azure_arc/issues/2498)
- [Feature: HCIBox - add automatic validation and deployment of cluster #2488](https://github.com/microsoft/azure_arc/issues/2488)
- [Feature: HCIBox - add automatic upgrade of cluster #2493](https://github.com/microsoft/azure_arc/issues/2493)
- [Feature: Update HCIBox VHDX images for April release #2524](https://github.com/microsoft/azure_arc/issues/2524)
- [Documentation: Jumpstart HCIBox 23H2 Deployment - Where or how to get Windows Admin Center #2490](https://github.com/microsoft/azure_arc/issues/2490)

### Arc-enabled data services

- [Feature: Azure Arc-enabled data services - April release #2495](https://github.com/microsoft/azure_arc/issues/2495)

### Arc, Edge, and IoT Operations

- [New scenario: Fault Detection with Edge Storage Accelerator on AKS Edge Essentials single node deployment](https://azurearcjumpstart.com/azure_arc_jumpstart/azure_edge_iot_ops/aks_edge_essentials_single_esa)
- [Bug: Deployment of Azure IoT Operations (AIO) fails with AKS-EE due to lack of logs space #2515](https://github.com/microsoft/azure_arc/pull/2514)
- [Bug: AIO scenario preview repository #2517](https://github.com/microsoft/azure_arc/issues/2517)

### Jumpstart Agora

- [Bug: Video feed not working in Agora retail #2522](https://github.com/microsoft/azure_arc/issues/2522)

## March 2024

### Release highlights

- New Arc-enabled servers scenario
- Arc-enabled data service monthly release
- AKS version bump
- Jumpstart Assets - Arc Architecture Posters and Diagrams (APD) [March release](https://www.linkedin.com/feed/update/urn:li:activity:7172952002442776576/)

### Cross Jumpstart

- [Bug: Unsupported default version of Kubernetes in multiple scenarios #2452](https://github.com/microsoft/azure_arc/issues/2452)

### Jumpstart ArcBox

- [Bug: ArcBox DataOps deployment fails with AKS Version not available #2451](https://github.com/microsoft/azure_arc/issues/2451)
- [Bug: Failed to connect AKS cluster with Azure Arc and failed to create custom location #2461](https://github.com/microsoft/azure_arc/issues/2461)

### Jumpstart HCIBox

- [Bug: HCIBox AZD use the current PowerShell context different to azd auth context #2443](https://github.com/microsoft/azure_arc/issues/2443)
- [Bug: HCIBox: Cloud Deployment ARM Validation Failing #2444](https://github.com/microsoft/azure_arc/issues/2444)
- [Bug: HCIBox - Windows Server 2022 latest Az marketplace image possibly causing slowness in nested virtualization network performance #2462](https://github.com/microsoft/azure_arc/issues/2462)
- [Bug: PowerShell error when running the configure-AKSWorkloadCluser.ps1 #2469](https://github.com/microsoft/azure_arc/issues/2469)
- [Bug: HCIBox AKS Kubernetes workload cluster deployment issues #2474](https://github.com/microsoft/azure_arc/issues/2474)

### Jumpstart Agora

- [Bug: AZD change - Have to provide default values for parameters #2459](https://github.com/microsoft/azure_arc/issues/2459)

### Arc-enabled servers

- [New scenario: Run PowerShell and Shell scripts on Azure Arc-enabled servers using the Run command](https://azurearcjumpstart.com/azure_arc_jumpstart/azure_arc_servers/day2/arc_run_command)

### Arc-enabled data services

- [Feature: Azure Arc-enabled data services - March release #2442](https://github.com/microsoft/azure_arc/issues/2442)

## February 2024

### Release highlights

- HCIBox support for 2402 OS version
- HCIBox Azure region support - Australia East, West Europe
- Jumpstart Assets - Arc Architecture Posters and Diagrams (APD) [initial release](https://www.linkedin.com/posts/liorkamrat_arcjumpstart-mvpbuzz-msftadvocate-activity-7160667718273118212-iYrJ?utm_source=share&utm_medium=member_desktop)
- Jumpstart Assets - Arc Architecture Posters and Diagrams (APD) [February release](https://www.linkedin.com/posts/liorkamrat_mvpbuzz-msftadvocate-azure-activity-7166081672575225857-AHV9?utm_source=share&utm_medium=member_desktop)

### Jumpstart ArcBox

- [Bug: Deployment fails if Service Principal can access multiple subscriptions #2393](https://github.com/microsoft/azure_arc/issues/2393)

### Jumpstart HCIBox

- [Bug: HCIBox: azd preprovisioning can error out due to older Az.Accounts module. #2394](https://github.com/microsoft/azure_arc/issues/2394)
- [Bug: Answer files generated by New-HCIBoxCluster.ps1 should use base64 encoding #2396](https://github.com/microsoft/azure_arc/issues/2396)
- [Bug: azd update changes when user is prompted for variables, thus requiring changes to the azd preprovision script #2427](https://github.com/microsoft/azure_arc/issues/2427)
- [Bug: Azure HCIBox - After logon script runs on HCIBox-Client I don't see the hosts in ARC Machines #2434](https://github.com/microsoft/azure_arc/issues/2434)
- [Enhancement: HCIBox should deploy with 2402 as the base #2435](https://github.com/microsoft/azure_arc/issues/2435)
- [Feature: HCIBox -> upstream change introduces az aksarc -> update Configure-AKSWorkloadCluster.ps1 to use new method #2401](https://github.com/microsoft/azure_arc/issues/2401)
- [Feature: Upgrade HCIBox to use 2311.2 as default OS image #2413](https://github.com/microsoft/azure_arc/issues/2413)
- [Documentation: Typo in Documentation - AKS on Azure Stack HCI #2415](https://github.com/microsoft/azure_arc/issues/2415)
- [Documentation: HCIBox diagram updates #258](https://github.com/Azure/arc_jumpstart_docs/pull/258)

### Jumpstart Agora

- [Bug: Agora Retail deployment fails due to unsupported AKS version #2433](https://github.com/microsoft/azure_arc/issues/2433)

### Arc-enabled servers

- [Bug: Arc AWS Scaled Deployment out of date #2424](https://github.com/microsoft/azure_arc/issues/2424)
- [Documentation: Update module versions in scenario "Automanage Machine Configuration custom configurations for Windows" #254](https://github.com/Azure/arc_jumpstart_docs/issues/254)

### Arc, Edge, and IoT Operations

- [Bug: AIO scenario - error in AIO initializtion #2392](https://github.com/microsoft/azure_arc/issues/2392)
- [Bug: Arc-enabled Video Indexer: update extension parameters to support release builds #2402](https://github.com/microsoft/azure_arc/issues/2402)

### Arc-enabled data services

- [Feature: Azure Arc-enabled data services - February release #2397](https://github.com/microsoft/azure_arc/issues/2397)

## Janurary 2024

### Release highlights

- [Jumpstart HCIBox 23H2 release](https://aka.ms/HCIBox23h2Blog)
- Secuirty posture improvements

### Cross Jumpstart

- [Enhancement: Passing of sensitive parameters #2205](https://github.com/microsoft/azure_arc/issues/2205)
- [Bug: Jumpstart to deploy an Arc-enabled k3s cluster on an Azure VM fails if the password of the service principal starts with "-" #2331](https://github.com/microsoft/azure_arc/issues/2331)

### Jumpstart HCIBox

- [Enhancement: HCIBox: 23H2 not supported #2304](https://github.com/microsoft/azure_arc/issues/2304)

### Jumpstart Agora

- [Bug: DockerDesktop popup #2351](https://github.com/microsoft/azure_arc/issues/2351)

### Arc-enabled SQL Server

- [Bug: Jumpstart Arc-enabled SQL Server - change server edition to allow use of performance metrics #2305](https://github.com/microsoft/azure_arc/issues/2305)

### Arc-enabled Kubernetes

- [Bug: Calico Remove image pull secret #2345](https://github.com/microsoft/azure_arc/issues/2345)

### Arc, Edge, and IoT Operations

- [Documentation: Missing images in jumpstart "Deploy AKS cluster on Azure IoT Edge and connect it to Azure Arc using Terraform" #2390](https://github.com/microsoft/azure_arc/issues/2390)
- [Bug: AIO - Service Principal Does Not Have Secrets List Permission on Key Vault #2353](https://github.com/microsoft/azure_arc/issues/2353)
