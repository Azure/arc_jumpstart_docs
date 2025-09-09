---
type: docs
title: "Jumpstart Release Notes"
linkTitle: "Jumpstart Release Notes"
weight: 6
---

# Arc Jumpstart release notes

## August 2025

### Release highlights

- Resolved ArcBox DataOps deployment issue related to NAT gateway and virtual network configuration
- Introduced Windows SSH posture control to ArcBox for enhanced security and compliance
- Optimized ITPro flavor deployments by excluding NAT gateway when Bastion is not deployed
- Upgraded ArcBox Linux machines to Ubuntu 24.04 for improved performance and support
- Updated Arc SQL container image versions for stability and feature alignment

### Jumpstart ArcBox

- [Bug / Issue: NatGatewayCannotBeUsedBySubnetsBelongingToDifferentVirtualNetworks Error for ArcBox DataOps Flavor #3288](https://github.com/microsoft/azure_arc/issues/3288)
- [Feature Request: Add Windows SSH Posture Control to ArcBox #3292](https://github.com/microsoft/azure_arc/issues/3292)
- [Feature Request: Exclude NAT gateway deployment in ITPro if Bastion is not deployed #3294](https://github.com/microsoft/azure_arc/issues/3294)
- [Feature Request: Update Linux machines in ArcBox to Ubuntu 2404 #3296](https://github.com/microsoft/azure_arc/issues/3296)
- [Feature Request: Update image version of Arc SQL contaimer images #3302](https://github.com/microsoft/azure_arc/issues/3302)

### Jumpstart Drops

- No new drops for this release

### Jumpstart SDK

- No updates for this release

## July 2025

### Release highlights

- Enhanced network security across all Jumpstart solutions with explicit defaultOutboundAccess property implementation
- LocalBox updated to Azure Local 2507 solution version with improved reliability
- 2 new Jumpstart Drops focusing on Azure Arc integration capabilities
- Documentation improvements for LocalBox RBAC permission requirements
- Critical bug fixes for LocalBox

### Jumpstart ArcBox

- [Feature Request: ArcBox - Add an explicit defaultOutboundAccess property to subnets in all templates avoid breaking scenarios #3266](https://github.com/microsoft/azure_arc/issues/3266)

### Jumpstart LocalBox

- [Bug / Issue: Type 'InitializeEceLite' of Role 'DeploymentService' raised an exception: Failed to initialize Ece Lite with Exception: #3273](https://github.com/microsoft/azure_arc/issues/3273)
- [Feature Request: LocalBox - Add an explicit defaultOutboundAccess property to subnets in all templates avoid breaking scenarios #3268](https://github.com/microsoft/azure_arc/issues/3268)
- [Feature Request: Update LocalBox to the 2506 solution version of Azure Local #3272](https://github.com/microsoft/azure_arc/issues/3272)
- [Feature Request: Update LocalBox to the 2507 solution version of Azure Local #3289](https://github.com/microsoft/azure_arc/issues/3289)
- [Docs Feature: LocalBox - Clarify the requirement for unconstrained Owner role RBAC permissions #774](https://github.com/Azure/arc_jumpstart_docs/issues/774)

### Jumpstart Agora

- [Feature Request: Agora- Add an explicit defaultOutboundAccess property to subnets in all templates avoid breaking scenarios #3267](https://github.com/microsoft/azure_arc/issues/3267)

### Jumpstart Drops

- [New: Azure Arc Video Indexer Example](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Azure%20Arc%20Video%20Indexer%20Example)
- [New: Azure Arc with AMPLS & Private Link](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Azure%20Arc%20with%20AMPLS%20&%20Private%20Link)

### Jumpstart SDK

- No updates for this release

## June 2025

### Release highlights

- Code cleanup for ArcBox DataOps flavor removing unused DHCP and AD DS components
- K3s version updates for Contoso Motors and Hypermarket scenarios
- 4 new Jumpstart Drops
- 2 new Jumpstart Lightning videos

### Jumpstart ArcBox

- [Feature Request: Add pipelines for integration tests #3252](https://github.com/microsoft/azure_arc/issues/3252)
- [Enhancement: Removed unused code related to DHCP service installation and AD DS roles for the DataOps flavor #3251](https://github.com/microsoft/azure_arc/pull/3251)

### Jumpstart LocalBox

- [Feature Request: Add pipelines for integration tests #3252](https://github.com/microsoft/azure_arc/issues/3252)

### Jumpstart Agora

- [Bug / Issue: Contoso Motors and Contoso Hypermarket use out-dated K3s version #3245](https://github.com/microsoft/azure_arc/issues/3245)
- [Feature Request: Remove longhorn.yaml and references to it since unneeded for Agora #3262](https://github.com/microsoft/azure_arc/issues/3262)

### Jumpstart Scenarios

- [Feature Request: Azure Arc-enabled data services - May release #3244](https://github.com/microsoft/azure_arc/issues/3244)

### Jumpstart Drops

- [Bug / Issue: Link to template file in Jumpstart drops not working #747](https://github.com/Azure/arc_jumpstart_docs/issues/747)
- [New: Azure Arc with Private Link (Terraform)](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Azure%20Arc%20with%20Private%20Link%20(Terraform)&fs=true)
- [New: Oauth2.0 multi-cluster API security using Traefik](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Oauth2.0%20multi-cluster%20API%20security%20using%20Traefik&fs=true)
- [New: OpenAPISpec with Traefik Developer Portal](https://jumpstart.azure.com/azure_jumpstart_drops?drop=OpenAPISpec%20with%20Traefik%20Developer%20Portal&fs=true)
- [New: Multi-cluster API Management using Traefik](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Multi-cluster%20API%20Management%20using%20Traefik&fs=true)

### Jumpstart SDK

- No updates for this release

### Jumpstart Lightning

- [Jumpstart LocalBox 25H2 Release](https://youtu.be/LdRALDLRMKU)
- [You NEED these Arc ESU Jumpstart dashboards!](https://youtu.be/zK-vW5aCR70)

## May 2025

### Release highlights

- [Jumpstart LocalBox 25H2](https://aka.ms/LocalBox25H2Blog)
- [Jumpstart LocalBox Rebranding](https://aka.ms/JumpstartLocalBoxBlog)
- [15 new Jumpstart Drops](http://aka.ms/JumpstartDrops)
- [Jumpstart Gems May release](https://aka.ms/JumpstartGemsReleaseLD525)

### Jumpstart ArcBox

- [Docs Feature: Add resource provider Microsoft.HybridConnectivity to prerequisites #720](https://github.com/Azure/arc_jumpstart_docs/issues/720)

### Jumpstart LocalBox

- [Bug / Issue: Automation Account Failed Error #3201](https://github.com/microsoft/azure_arc/issues/3201)
- [Bug / Issue: Azure Local validation is failing due to AzureEdgeLifecycleManager latest version not supported #3219](https://github.com/microsoft/azure_arc/issues/3219)
- [Bug / Issue: 1 Test Failed Jumpstart LocalBox #3220](https://github.com/microsoft/azure_arc/issues/3220)
- [Feature Request: Update LocalBox to solution update 2504 #3221](https://github.com/microsoft/azure_arc/issues/3221)
- [Feature Request: Remove Service Principal dependency for LocalBox #3223](https://github.com/microsoft/azure_arc/issues/3223)
- [Feature Request: LocalBox - add support for Spot VMs #3239](https://github.com/microsoft/azure_arc/issues/3239)
- [Feature Request: LocalBox - add support for Azure Local 2505 #3240](https://github.com/microsoft/azure_arc/issues/3240)
- [Feature Request: Add support for deploying the LocalBox Client VM and Azure Local instance in separate regions #3241](https://github.com/microsoft/azure_arc/issues/3241)
- [Feature Request: LocalBox - add dedicated PowerShell module #3242](https://github.com/microsoft/azure_arc/issues/3242)
- [Bug / Issue: LocalBox deployment error #686](https://github.com/Azure/arc_jumpstart_docs/issues/686)
- [Docs Feature: Add resource provider Microsoft.HybridConnectivity to prerequisites #720](https://github.com/Azure/arc_jumpstart_docs/issues/720)
- [Bug / Issue: Azure Local validation is failing due to AzureEdgeLifecycleManager latest version not supported #727](https://github.com/Azure/arc_jumpstart_docs/issues/727)
- [Docs Feature: Add deployment time note to LocalBox documentation #728](https://github.com/Azure/arc_jumpstart_docs/issues/728)
- [Docs Feature: Add required Azure resource providers to LocalBox documentation #729](https://github.com/Azure/arc_jumpstart_docs/issues/729)
- [Docs Feature: Improvements to LocalBox documentation #730](https://github.com/Azure/arc_jumpstart_docs/issues/730)

### Jumpstart Agora

- [Bug / Issue: Contoso Motors - Incorporate v2 changes #3218](https://github.com/microsoft/azure_arc/issues/3218)
- [Bug / Issue: 2 tests fail on Contoso Motors #3224](https://github.com/microsoft/azure_arc/issues/3224)
- [Bug / Issue: Prometheus.monitoring.coreos.com "prometheus-kube-prometheus-prometheus" is invalid #3226](https://github.com/microsoft/azure_arc/issues/3226)
- [Bug / Issue: Contoso Motors - Azure IoT Operation - release azure-arc-containerstorage failed #3236](https://github.com/microsoft/azure_arc/issues/3236)
- [Docs Feature: Add resource provider Microsoft.HybridConnectivity to prerequisites #720](https://github.com/Azure/arc_jumpstart_docs/issues/720)

### Jumpstart Scenarios

- No updates for this release

### Jumpstart Drops

- [Microsoft Entra Workload ID with AKS](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Microsoft%20Entra%20Workload%20ID%20with%20AKS)
- [External Secrets Operator with Azure Key Vault](https://jumpstart.azure.com/azure_jumpstart_drops?drop=External%20Secrets%20Operator%20with%20Azure%20Key%20Vault)
- [Dapr Secret Store for Key Vault](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Dapr%20Secret%20Store%20for%20Key%20Vault)
- [Secrets Store CSI Driver for Key Vault in AKS](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Secrets%20Store%20CSI%20Driver%20for%20Key%20Vault%20in%20AKS)
- [Azure Arc gateway with Terraform](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Azure%20Arc%20gateway%20with%20Terraform)
- [Azure Arc Agent Toolkit](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Azure%20Arc%20Agent%20Toolkit)
- [3D USD Import and Export For Digital Twin Builder](https://jumpstart.azure.com/azure_jumpstart_drops?drop=3D%20USD%20Import%20and%20Export%20For%20Digital%20Twin%20Builder)
- [Use Azure Monitor dashboards with Grafana for K8s](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Use%20Azure%20Monitor%20dashboards%20with%20Grafana%20for%20K8s)
- [Azure Container Storage enabled by Azure Arc SFTP](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Azure%20Container%20Storage%20enabled%20by%20Azure%20Arc%20SFTP)
- [Monitor Arc Agent Logs](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Monitor%20Arc%20Agent%20Logs)
- [Kubernetes AI Toolchain Operator (KAITO) & AKS Arc](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Kubernetes%20AI%20Toolchain%20Operator%20(KAITO)%20&%20AKS%20Arc)
- [Traefik Deployment on Arc-enabled Kubernetes](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Traefik%20Deployment%20on%20Arc-enabled%20Kubernetes)
- [Multi-cluster TLS cert management using Traefik](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Multi-cluster%20TLS%20cert%20management%20using%20Traefik)
- [Service auto-discovery and routing with Traefik](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Service%20auto-discovery%20and%20routing%20with%20Traefik)
- [Deploy multiple Arc k8s clusters with Terraform](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Deploy%20multiple%20Arc%20k8s%20clusters%20with%20Terraform)

### Jumpstart SDK

- [Feature Request: Added Azure Arc Jumpstart LocalBox PowerShell module #329](https://github.com/Azure/jumpstart-sdk/pull/329)

### Jumpstart Lightning

- [Enable secret encryption on AKS EE | EASY PEASY!](https://youtu.be/3pXDA7BFKCE)

## April 2025

### Release highlights

- Jumpstart and the new *Azure.Arc.Jumpstart.Common* PowerShell module is now part the [PowerShell Gallery](https://www.powershellgallery.com/profiles/jumpstart). See [announcement](https://www.linkedin.com/posts/janegilring_azurearc-powershell-devops-activity-7321568402370641920-07JR?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAGRRdoBb4Olf2HriygmIqHP4lnX1xJe_hc) from the team
- New Jumpstart Drop: [Arc Insights PBI Dashboards Powered by Jumpstart](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Arc%20Insights%20PBI%20Dashboards%20Powered%20by%20Jumpstart&fs=true)
- Total of 4 new Jumpstart Drops in the release
- All ArcBox OS images updated with latest patch level
- ArcBox bug fixes and documents update
- HCIBox improvements for VM lifecycle
- Telemetry enhancements
- [New Arc Jumpstart video training series](https://www.youtube.com/playlist?list=PLZuSmETs0xIZybQBZo1x8PP_dbD9FD0BE)

### Jumpstart ArcBox

- [Bug / Issue: Unable to start ArcBox-Client HyperV servers - ARC Jumpstart ITPro install #3143](https://github.com/microsoft/azure_arc/issues/3143)
- [Bug / Issue: SQLQueryStress broken URL #3145](https://github.com/microsoft/azure_arc/issues/3145)
- [Feature Request: Add GUIDs for JS Telemetry #3136](https://github.com/microsoft/azure_arc/issues/3136)
- [Docs Feature: Move ArcBox parameters into table #679](https://github.com/Azure/arc_jumpstart_docs/issues/679)

### Jumpstart LocalBox

- [Feature Request: Missing provider requirement #3138](https://github.com/microsoft/azure_arc/issues/3138)
- [Feature Request: Support Standard_E32s_v6 in HCIBox #3140](https://github.com/microsoft/azure_arc/issues/3140)
- [Feature Request: Add GUIDs for JS Telemetry #3136](https://github.com/microsoft/azure_arc/issues/3136)

### Jumpstart Agora

- [Bug / Issue: Contoso Supermarket Scenario Uses Unsupported Kubernetes Version #3174](https://github.com/microsoft/azure_arc/issues/3174)
- [Feature Request: Add GUIDs for JS Telemetry #3136](https://github.com/microsoft/azure_arc/issues/3136)
- [Bug / Issue: Contoso Motors - define InfluxDB Admin password & comment deployGPUNodes #3180](https://github.com/microsoft/azure_arc/pull/3180)
- [Bug / Issue: Agora base image credentials not aligned to the JS OS images baseline #3191](https://github.com/microsoft/azure_arc/issues/3191)

### Jumpstart Scenarios

- [Bug / Issue: StorageProfile is not accepted value for agentPoolProfiles in AKS under Jumpstart ML Scenario #3170](https://github.com/microsoft/azure_arc/issues/3170)
- [Feature Request: Azure Arc-enabled data services - April release #3181](https://github.com/microsoft/azure_arc/issues/3181)
- [Docs Feature: Update PowerShell version and PowerShell module versions in the Automanage Machine Configuration custom configuration scenarios #678](https://github.com/Azure/arc_jumpstart_docs/issues/678)

### Jumpstart Drops

- [New: Arc Insights PBI Dashboards Powered by Jumpstart](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Arc%20Insights%20PBI%20Dashboards%20Powered%20by%20Jumpstart&fs=true)
- [New: Azure Arc Connectivity Check](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Azure%20Arc%20Connectivity%20Check)
- [New: Azure Arc SQL Tags Inheritance](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Azure%20Arc%20SQL%20Tags%20Inheritance)
- [New: Graph User Photo Sync Automation](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Graph%20User%20Photo%20Sync%20Automation)

### Jumpstart SDK

- [Feature Request: Add Azure.Arc.Jumpstart.Common module #66](https://github.com/Azure/jumpstart-sdk/issues/66)

### Jumpstart Lightning

- [Arc Jumpstart video training series](https://www.youtube.com/playlist?list=PLZuSmETs0xIZybQBZo1x8PP_dbD9FD0BE)
- [Arc SQL Best Practices Assessment | SHOULD YOU?](https://youtu.be/yPlzP0XVLz0)

## March 2025

### Release highlights

- [Jumpstart Agora - Contoso Motors v2 release](https://techcommunity.microsoft.com/blog/azurearcblog/jumpstart-agora---contoso-motors-v2/4397985)
- [Jumpstart Gems March release](https://www.linkedin.com/posts/liorkamrat_azure-msftadvocate-mvpbuzz-activity-7310788209955721219-kHmm?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAGRRdoBb4Olf2HriygmIqHP4lnX1xJe_hc)
- HCIBox Client VM Windows Server 2025 support
- ArcBox ARM APIs vBump
- [Refactored "Deploy Azure Container Apps on AKS using an ARM Template" scenario](https://jumpstart.azure.com/azure_arc_jumpstart/azure_arc_app_svc/aks/aks_container_apps_arm_template)
- Numerous bug fixes for ArcBox, HCIBox, and Agora
- 3 new Jumpstart Drops
- 6 new Jumpstart Lightning videos
- Several deprecated scenarios to streamline offerings
  - All of Arc-enabled data services data controller vanilla scenarios 
  - Arc-enabled SQL Managed Instance with Kubeadm using ARM Template
  - Arc-enabled SQL Managed Instance with MicroK8s using ARM Template

### Jumpstart ArcBox

- [Feature Request: Migrate container images to MCR](https://github.com/microsoft/azure_arc/issues/2997)
- [Bug / Issue: Remote Desktop hang when logging in to ArcBox and HCIBox Client VMs #3035](https://github.com/microsoft/azure_arc/issues/3035)
- [Feature Request: Update NSG priorities #3048](https://github.com/microsoft/azure_arc/issues/3048)
- [Feature Request: ArcBox - Update ARM API versions for ARM template and Bicep #3111](https://github.com/microsoft/azure_arc/issues/3111)

### Jumpstart LocalBox

- [Enhancement: HCIBox - Update Windows Server 2022 vhdx image to Windows Server 2025 #2709](https://github.com/microsoft/azure_arc/issues/2709)
- [Feature Request: Internal governance automation potentially breaking HCIBox #2998](https://github.com/microsoft/azure_arc/issues/2998)
- [Bug / Issue: Cant deploy Logical Network - error while running script #3002](https://github.com/microsoft/azure_arc/issues/3002)
- [Bug / Issue: Remote Desktop hang when logging in to ArcBox and HCIBox Client VMs #3035](https://github.com/microsoft/azure_arc/issues/3035)
- [Docs Feature: Make the regional and quote HCIBox disclaimer more visable #625](https://github.com/Azure/arc_jumpstart_docs/issues/625)
- [Feature Request: Missing provider requirement #3138](https://github.com/microsoft/azure_arc/issues/3138)
- [Docs Feature: Missing provider requirement #638](https://github.com/Azure/arc_jumpstart_docs/issues/638)

### Jumpstart Agora

- [Bug / Issue: Version '0.5.1b1' not found for extension 'azure-iot-ops' #2908](https://github.com/microsoft/azure_arc/issues/2908)
- [Bug / Issue: Hypermarket Deployment Mistakenly Uses Motors Configuration #3001](https://github.com/microsoft/azure_arc/issues/3001)
- [Feature Request: Update NSG priorities #3048](https://github.com/microsoft/azure_arc/issues/3048)

### Jumpstart Scenarios

- [Bug / Issue: Deploy container apps on AKS using an ARM Template #2906](https://github.com/microsoft/azure_arc/issues/2906)
- [Bug / Issue: The system cannot find the file specified - Deploy a vanilla Azure Arc Data Controller in a directly connected mode on AKS using an ARM Template #2923](https://github.com/microsoft/azure_arc/issues/2923)
- [Feature Request: Azure Arc-enabled data services - March Release #3125](https://github.com/microsoft/azure_arc/issues/3125)
- [Docs Feature: Deprecate Arc-enabled data services Data Controller scenarios #595](https://github.com/Azure/arc_jumpstart_docs/issues/595)

### Jumpstart Drops

- [New: Azure Local Releases Tool](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Azure%20Local%20Releases%20Tool)
- [New: Azure Quick Review Tutorial](https://jumpstart.azure.com/azure_jumpstart_drops?drop=%20Azure%20Quick%20Review%20Tutorial)
- [New: Azure Local Endpoints Codified](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Azure%20Local%20Endpoints%20Codified)

### Jumpstart Lightning

- [Azure Device Registry and Storage | But can it HA?](https://youtu.be/NceN83tjaL4)
- [Arc-enabled servers | Is it secured?](https://youtu.be/wqN57-_i1yY)
- [I didn't know CloudCasa can do that](https://youtu.be/rsbmXajcmd0)
- [Arc and Azure Benefits | Old servers?! DO IT!](https://youtu.be/L49XxTwutNw)
- [SSH Posture Control | Not JUST Port 22](https://youtu.be/ddiHeWVo7kA)
- [Litmus Edge with Azure IoT Operations | IT'S THE DATA!](https://youtu.be/RdS9GUPrZj0)

## February 2025

### Release highlights

- [5 years of Arc Jumpstart with a refreshed website](https://techcommunity.microsoft.com/blog/azurearcblog/5-years-of-arc-jumpstart-with-a-refreshed-website/4384823)
- [Jumpstart Gems release for the month of January/February](https://www.linkedin.com/posts/liorkamrat_azure-msftadvocate-mvpbuzz-activity-7292239125657632768-cAsU?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAGRRdoBb4Olf2HriygmIqHP4lnX1xJe_hc)
- Five new Jumpstart Drops added
- Three new Jumpstart Lightning videos
- Multiple bug fixes for ArcBox deployment and logon scripts
- Enhanced HCIBox with additional location support
- Migration of Contoso Supermarket to Jumpstart-apps repository
- Several deprecated scenarios to streamline offerings
  - Edge IoT with AKS
  - Platform 9 with Arc-enabled Kubernetes
  - Arc-enabled app services (Azure Web App) with AKS
  - Arc-enabled app services (Azure API Management) with AKS
  - Arc-enabled app services (Azure Functions) with AKS
  - Arc-enabled app services (Azure Logic Apps) with AKS
  - Arc-enabled SQL Managed Instance with Azure DevOps
  - Arc-enabled PostgreSQL Instance with Azure DevOps

### Jumpstart ArcBox

- [Bug / Issue: Azure Policy deployment error in ArcBox for ITPro #2934](https://github.com/microsoft/azure_arc/issues/2934)
- [Bug / Issue: Deployment error with complex password generator #2904](https://github.com/microsoft/azure_arc/issues/2904)
- [Bug / Issue: Logon script failing on ArcBox-client multiple times #2992](https://github.com/microsoft/azure_arc/issues/2992)

### Jumpstart LocalBox

- [Enhancement: HCIBox - Add more location #2903](https://github.com/microsoft/azure_arc/issues/2903)
- [Enhancement: Add resource provider registration prerequisite for HCIBox #480](https://github.com/Azure/arc_jumpstart_docs/issues/480)
- [Bug / Issue: HCI autoDeployClusterResource validate fails with LcmController latest version #3133](https://github.com/microsoft/azure_arc/issues/3133)

### Jumpstart Agora

- [Enhancement: Contoso Supermarket - Migrate to Jumpstart-apps repository #2913](https://github.com/microsoft/azure_arc/issues/2913)

### Jumpstart Scenarios

- [Feature Request: Azure Arc-enabled data services - Feb Release #3003](https://github.com/microsoft/azure_arc/issues/3003)
- [Feature Request: Azure Arc-enabled data services - Nov/Jan Release #2915](https://github.com/microsoft/azure_arc/issues/2915)
- [Depreciation: Remove majority of Arc-enabled app services scenarios #507](https://github.com/Azure/arc_jumpstart_docs/issues/507)

### Jumpstart Drops

- [New: Integrating Litmus Edge with Azure IoT Operations](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Integrating%20Litmus%20Edge%20with%20Azure%20IoT%20Operations&fs=true)
- [New: Azure Arc Windows Server Management License Activation](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Azure%20Arc%20Windows%20Server%20Management%20License%20Activation&fs=true)
- [New: Connecting IIoT Gateway to Azure IoT Operations](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Connecting%20IIoT%20Gateway%20to%20Azure%20IoT%20Operations&fs=true)
- [New: Using Secret Store extension to fetch secrets in Azure Arc-enabled Kubernetes cluster](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Using%20Secret%20Store%20extension%20to%20fetch%20secrets%20in%20Azure%20Arc-enabled%20Kubernetes%20cluster&fs=true)
- [New: Connecting PLC using Modbus and Dapr to Azure IoT Operations](https://jumpstart.azure.com/azure_jumpstart_drops?drop=Connecting%20PLC%20using%20Modbus%20and%20Dapr%20to%20Azure%20IoT%20Operations&fs=true)

### Jumpstart Lightning

- [Azure Device Registry and Storage | But can it HA?](https://youtu.be/NceN83tjaL4)
- [Arc-enabled servers | Is it secured?](https://youtu.be/wqN57-_i1yY)
- [I didn't know CloudCasa can do that](https://youtu.be/rsbmXajcmd0)

## January 2025

### Release highlights

- [Announcing Jumpstart ArcBox 25Q1](https://aka.ms/ArcBox2025Blog)
- Azure Developer CLI (azd) support depreciation from HCIBox
- Deprecating "Contoso Bakeries" scenario
- Critical Jumpstart LocalBox bug fixes
- Other issue fixes

### Jumpstart ArcBox

- [Release: Jumpstart ArcBox 25Q1](https://github.com/microsoft/azure_arc/issues/2868)
- [Bug: Logon scripts on ARCBoxClient machine fail! #2845](https://github.com/microsoft/azure_arc/issues/2845)
- [Docs: Azure ArcBox for ITPros deployment #448](https://github.com/Azure/arc_jumpstart_docs/issues/448)

### Jumpstart LocalBox

- [Bug: Type 'ValidateAzureStackNetworkATCSettings' of Role 'HostNetwork' raised an exception: #2861](https://github.com/microsoft/azure_arc/issues/2861)
- [Bug: main.azd.bicep contains unsupported region #2873](https://github.com/microsoft/azure_arc/issues/2873)
- [Bug: PowerShell Scripts on HCIBox AKS and VM scenarios use hard coded locations #2885](https://github.com/microsoft/azure_arc/issues/2885)
- [Bug: Pre-deployment script fails on Hyper-V attaching wrong vhdx file #2886](https://github.com/microsoft/azure_arc/issues/2886)
- [Docs: HCIBox Doc issues #427](https://github.com/Azure/arc_jumpstart_docs/issues/427)
- [Depreciation: An error occurred creating the service principal (AZD support removed) #2895](https://github.com/microsoft/azure_arc/issues/2895)

### Jumpstart Agora

- [Bug: Contoso Motors - The Logon scripts show errors while installing Azure IoT Operations. #2875](https://github.com/microsoft/azure_arc/issues/2875)

### Jumpstart Scenarios

- [Bug: AKS ARM template fails deployment due to unsupported parameter inclusion #2847](https://github.com/microsoft/azure_arc/issues/2847)
- [Bug: Deployment of azure_arc_jumpstart/azure_edge_iot_ops/aks_edge_essentials_single fails #2872](https://github.com/microsoft/azure_arc/issues/2872)
- [Depreciation: Deprecating "Contoso Bakeries" scenario #2883](https://github.com/microsoft/azure_arc/issues/2883)

### Jumpstart Lightning

- [Unified Namespace for IIoT with Vincent](https://youtu.be/XE6_OeBJv94)
- [Jumpstart ArcBox | PAY LESS, DO MORE!](https://youtu.be/6zRk5I7c3k0)
