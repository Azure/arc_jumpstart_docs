---
type: docs
title: "Jumpstart Release Notes"
linkTitle: "Jumpstart Release Notes"
weight: 6
---

# Arc Jumpstart release notes

> **Note:** Release notes will be released around the first week of each month and will cover the previous month.

## November 2024

### Release highlights
* Critical Jumpstart ArcBox/HCIBox bug fixes
* [Announcing Jumpstart Agora "Contoso Hypermarket" scenario](https://techcommunity.microsoft.com/blog/azurearcblog/announcing-jumpstart-agora-contoso-hypermarket-scenario/4289504)
* [Jumpstart Drops Hits General Availability](https://techcommunity.microsoft.com/blog/azurearcblog/jumpstart-drops-hits-general-availability/4288629)
* Other minor fixes 

### Jumpstart HCIBox

- [HCIBox - autoDeployClusterResource set to true / Enable Storage Auto IP #2780](https://github.com/microsoft/azure_arc/issues/2780)
- [Remove WinGet pindown for ArcBox and HCIBox #2793](https://github.com/microsoft/azure_arc/issues/2793)
- [Type 'ValidateAzureStackNetworkATCSettings' of Role 'HostNetwork' raised an exception #2861](https://github.com/microsoft/azure_arc/issues/2861)
- [main.azd.bicep contains unsupported region #2873](https://github.com/microsoft/azure_arc/issues/2873)
- [azd down: error deleting Azure resources: no resources found for deployment · Issue #2876](https://github.com/microsoft/azure_arc/issues/2876)

### Jumpstart ArcBox

- [Can't see SQL Databases using ARC box for it Pros #2782](https://github.com/microsoft/azure_arc/issues/2782)
- [Remove WinGet pindown for ArcBox and HCIBox #2793](https://github.com/microsoft/azure_arc/issues/2793)

### Jumpstart Agora

- [Agora-HyperMarket Deployment Issue #2863](https://github.com/microsoft/azure_arc/issues/2863)

### Arc-enabled Kubernetes
- [AKS ARM template fails deployment due to unsupported parameter inclusion #2847](https://github.com/microsoft/azure_arc/issues/2847)

## October 2024

### Release highlights

- Critical Jumpstart ArcBox bug fixes
- Critical Jumpstart Agora bug fixes
- Critical Azure IoT Operations related bug fixes

### Jumpstart HCIBox

- [Bug: Jumpstart HCI Box: Exception encountered while adding node to cluster #2732](https://github.com/microsoft/azure_arc/issues/2732)
- [Bug: HCIBox Step 10/11 [Build Cluster validate cluster deployment] is failing #2737](https://github.com/microsoft/azure_arc/issues/2737)
- [Feature: HCIBox-Client VM - Infrastructure deployment #2730](https://github.com/microsoft/azure_arc/issues/2730)

### Jumpstart Agora

- [Bug: Manufacturing - cannot import name 'AccessTokenInfo' from 'azure.core.credentials' when deploying AIO on the cluster #2731](https://github.com/microsoft/azure_arc/issues/2731)
- [Bug: Deploying Agora Manufacturing Scenario fails to connect AKS EE clusters to Azure Arc #2761](https://github.com/microsoft/azure_arc/issues/2761)
- [Bug: Az cli connectedk8s regression causes failures in k3s onboarding #2763](https://github.com/microsoft/azure_arc/issues/2763)

### Arc-enabled Kubernetes

- [Bug: main.py in esa_fault_detection scenario has hardcoded paths causing issues with Edge Volumes #2735](https://github.com/microsoft/azure_arc/issues/2735)

### Arc, Edge, and Azure IoT Operations

- [Bug: no matches for kind "MqttBridgeConnector" in version "mq.iotoperations.azure.com/v1beta1" #2738](https://github.com/microsoft/azure_arc/issues/2738)

## September 2024

### Release highlights

- Deprecation of Cluster API (CAPI) from the Arc Jumpstart
- Critical Jumpstart ArcBox bug fixes
- Critical Jumpstart Agora bug fixes
- Various documentation updates
- Miscellaneous bug fixes and enhancements

### Cross Jumpstart

- [Deprecation: Deprecate CAPI from Jumpstart Scenarios #2707](https://github.com/microsoft/azure_arc/issues/2707)
- [Enhancement: Update AKSEE schema version to 1.14 #2722](https://github.com/microsoft/azure_arc/issues/2722)

### Jumpstart ArcBox

- [Bug: ArcBox deployment fails due to WinGet bootstrapping issue #2724](https://github.com/microsoft/azure_arc/issues/2724)
- [Bug: Deployment failure if no email recipient given for autoshutdown #404](https://github.com/Azure/arc_jumpstart_docs/issues/404)
- [Feature: Support Arc-enabled SQL Server least privilege, automated backups, and performance dashboards #2733](https://github.com/microsoft/azure_arc/issues/2733)
- [Enhancement: Update AKS templates autoupgrade channels #2699](https://github.com/microsoft/azure_arc/issues/2699)

### Jumpstart HCIBox

- [Documentation: Syntax within the guide for HCI #2715](https://github.com/microsoft/azure_arc/issues/2715)

### Jumpstart Agora

- [Bug: Bug with new version in Azure IoT Operations #2695](https://github.com/microsoft/azure_arc/issues/2695)
- [Bug: Contoso Motors - reporting dashboard not working #2702](https://github.com/microsoft/azure_arc/issues/2702)
- [Bug: Contoso Motors - InfluxDB login not working #2703](https://github.com/microsoft/azure_arc/issues/2703)
- [Documentation: Update Screenshots to use newer branding for Agora #408](https://github.com/Azure/arc_jumpstart_docs/issues/408)

### Arc-enabled Kubernetes

- [Bug: Logon script error in AKS Edge Essentials single node deployment with Azure Arc using ARM Template #2688](https://github.com/microsoft/azure_arc/issues/2688)

### Arc-enabled data services

- [Feature: Azure Arc-enabled data services - Sept release #2711](https://github.com/microsoft/azure_arc/issues/2711)

### Arc, Edge, and IoT Operations

- [Bug: Simulator not Transmitting Data in Edge IoT Ops Manufacturing Jumpstart #406](https://github.com/Azure/arc_jumpstart_docs/issues/406)

## August 2024

### Release highlights

- [Jumpstart ArcBox v3.0 release](https://aka.ms/arcboxblog)
- Critical HCIBox upstream-related bug fixes

### Jumpstart ArcBox

- [Jumpstart ArcBox v3.0 release](https://aka.ms/arcboxblog)
- [Bug: C:\ArcBox\SqlQueryStress.zip is missing #354](https://github.com/Azure/arc_jumpstart_docs/issues/354)
- [Bug: Microsoft SQL Server Management Studio Desktop Link is broken #353](https://github.com/Azure/arc_jumpstart_docs/issues/353)
- [Bug: Provisioning of VM extension installscript_CAPI has timed out #352](https://github.com/Azure/arc_jumpstart_docs/issues/352)

### Jumpstart HCIBox

- [Bug: cannot provision k8s on the HCIBox cluster #2628](https://github.com/microsoft/azure_arc/issues/2628)
- [Bug: HCI deployment failing with permission error. #2631](https://github.com/microsoft/azure_arc/issues/2631)
- [Bug: [Regression]Unable to install a new jumpstart HCIBox #2658](https://github.com/microsoft/azure_arc/issues/2658)
- [Bug: HCIBox-Client post deployment automation issues #2671](https://github.com/microsoft/azure_arc/issues/2671)

### Jumpstart Agora

- [Bug: IOT_OPS_Jumpstart failing for AIO_Manufacturing with error: mq_service_type not found #2648](https://github.com/microsoft/azure_arc/issues/2648)
- [Bug: Azure_jumpstart_ag -> Manufacturing: Aglogon script doesn't run successfully. #2655](https://github.com/microsoft/azure_arc/issues/2655)

### Arc, Edge, and IoT Operations

- [Bug: IOT_OPS_Jumpstart failing for AIO_Manufacturing with error: mq_service_type not found #2648](https://github.com/microsoft/azure_arc/issues/2648)

### Arc-enabled data services

- [Feature: Azure Arc-enabled data services - Aug release #2678](https://github.com/microsoft/azure_arc/issues/2678)

## July 2024

### Release highlights

- Maintenance release
- Jumpstart Assets - Arc Architecture Posters and Diagrams (APD) [July release](https://www.linkedin.com/posts/liorkamrat_msftadvocate-mvpbuzz-azure-activity-7224056401747136512-w6KF?utm_source=combined_share_message&utm_medium=member_desktop)

### Cross Jumpstart

- [Feature: Add ability to pin AKS Edge essentials to a specific schema version #2624](https://github.com/microsoft/azure_arc/issues/2624)

### Jumpstart ArcBox

- [Feature: Upcoming breaking change in Get-AzAccessToken #2611](https://github.com/microsoft/azure_arc/issues/2611)

### Jumpstart HCIBox

- [Bug: Unable to deploy Arcmanaged VM from Azure Portal](https://github.com/microsoft/azure_arc/issues/2599)
- [Bug: AzSHOST1 : Extension AzureEdgeDeviceManagement and Extension AzureEdgeLifecycleManager are missing #2614](https://github.com/microsoft/azure_arc/issues/2614)
- [Bug: A parameter cannot be found that matches parameter name 'AsPlainText'. #2620](https://github.com/microsoft/azure_arc/issues/2620)
- [Feature: Upcoming breaking change in Get-AzAccessToken #2611](https://github.com/microsoft/azure_arc/issues/2611)

### Arc-enabled data services

- [Feature: Azure Arc-enabled data services - July release #2608](https://github.com/microsoft/azure_arc/issues/2608)

## June 2024

### Release highlights

- Various critical bugs fixes and features
- Jumpstart Assets - Arc Architecture Posters and Diagrams (APD) [June release](https://www.linkedin.com/feed/update/urn:li:activity:7211732533040799744/)

### Jumpstart HCIBox

- [Bug: High MTU (9014) causes network congestion on nested VMs when using Windows Server 20348.2340.240303 or later #2579](https://github.com/microsoft/azure_arc/issues/2579)
- [Feature: HCI box unable to create RG - Unable to acquire a token error. #2571](https://github.com/microsoft/azure_arc/issues/2571)

### Arc-enabled data services

- [Feature: Azure Arc-enabled data services - June release #2582](https://github.com/microsoft/azure_arc/issues/2582)

## May 2024

### Release highlights

- Maintenance release

### Cross Jumpstart

- [Feature: Remove use of SAS tokens for VHD downloads #2551](https://github.com/microsoft/azure_arc/issues/2551)

### Jumpstart ArcBox

- [Feature: Leverage Managed Identity for authentication #2550](https://github.com/microsoft/azure_arc/issues/2550)

### Jumpstart HCIBox

- [Bug: Failed to deploy HCIBox: failure when processing extension 'Bootstrap' Missing an argument for parameter 'spnProviderId' #2541](https://github.com/microsoft/azure_arc/issues/2541)
- [Bug: Syntax error line 169 - preprovision.ps1 #2546](https://github.com/microsoft/azure_arc/issues/2546)

### Arc-enabled servers

- [Bug: Failed to deploy Azure Arc-enabled servers connectivity behind a proxy server #303](https://github.com/Azure/arc_jumpstart_docs/issues/303)

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

### Arc-enabled servers

- [Documentation: Code snippet to create service principal for Microsoft Azure: Windows Server Virtual Machine has error, causing it to fail #285](https://github.com/Azure/arc_jumpstart_docs/issues/285)

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

- [Bug: AIO scenario - error in AIO initialization #2392](https://github.com/microsoft/azure_arc/issues/2392)
- [Bug: Arc-enabled Video Indexer: update extension parameters to support release builds #2402](https://github.com/microsoft/azure_arc/issues/2402)

### Arc-enabled data services

- [Feature: Azure Arc-enabled data services - February release #2397](https://github.com/microsoft/azure_arc/issues/2397)

## January 2024

### Release highlights

- [Jumpstart HCIBox 23H2 release](https://aka.ms/HCIBox23h2Blog)
- Security posture improvements

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