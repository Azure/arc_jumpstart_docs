---
type: docs
linkTitle: "Getting Started"
isGettingStarted: false
weight: 2
---
# Evaluating Azure Local with HCIBox
## Getting started

HCIBox is a turnkey solution that provides a complete sandbox for exploring [Azure Local](https://learn.microsoft.com/azure-stack/hci/whats-new) capabilities and hybrid cloud integration in a virtualized environment. HCIBox is designed to be completely self-contained within a single Azure subscription and resource group, which will make it easy for a user to get hands-on with Azure Local and [Azure Arc](https://learn.microsoft.com/azure/azure-arc/overview) technology without the need for physical hardware.

  > **Note:** [Azure Stack HCI 23H2](https://learn.microsoft.com/azure-stack/hci/whats-new) is now generally available. 23H2 simplifies configuration and deployment of Azure Local instances and related workloads like [VM management](https://learn.microsoft.com/azure-stack/hci/manage/azure-arc-vm-management-overview) for VM self-service management in Azure portal. HCIBox has also been updated and now offers instances built on the new 23H2 OS, and prior Azure Local releases are no longer part of HCIBox or supported by the Jumpstart team. If you have used earlier versions of HCIBox you should read this guide thoroughly to understand the new HCIBox deployment process.

<img src="/img/logo/hcibox.png" alt="Jumpstart HCIBox logo" width="250">

## Use cases

- Sandbox environment for getting hands-on with Azure Local and Azure Arc technologies
- Accelerator for Proof-of-concepts or pilots
- Training tool for skills development
- Demo environment for customer presentations or events
- Rapid integration testing platform

![Screenshot showing HCIBox architecture diagram](./arch.png)

## Azure Local capabilities available in HCIBox

### 2-node Azure Local instance

HCIBox automatically creates and configures a two-node Azure Local instance using nested virtualization with Hyper-V running on an Azure Virtual Machine. This Hyper-V host creates three guest virtual machines: two Azure Local machines (_AzSHost1_, _AzSHost2_), and one nested Hyper-V host (_AzSMGMT_). _AzSMGMT_ itself hosts two guest VMs: an [Active Directory domain controller](https://learn.microsoft.com/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview), and a [Routing and Remote Access Server](https://learn.microsoft.com/windows-server/remote/remote-access/remote-access) acting as a virtual router.

![Screenshot showing HCIBox nested virtualization](./nested_virtualization.png)

### Virtual machine management

HCIBox comes with [guest VM management in Azure portal](https://learn.microsoft.com/azure-stack/hci/manage/azure-arc-vm-management-overview). The HCIBox documentation will walk you through how to use this feature, including configuring VM images from Azure marketplace and creating VMs on your instance.

### Azure Kubernetes Service on Azure Stack HCI

Azure Stack HCI includes [Azure Kubernetes Services on Azure Local (AKS hybrid)](https://learn.microsoft.com/azure/aks/hybrid/) as part of the default configuration. A user script is provided that can be used to create a workload instance.

## HCIBox Azure Consumption Costs

HCIBox resources generate Azure Consumption charges from the underlying Azure resources including core compute, storage, networking and auxiliary services. Note that Azure consumption costs may vary depending the region where HCIBox is deployed. Be mindful of your HCIBox deployments and ensure that you disable or delete HCIBox resources when not in use to avoid unwanted charges. Please see the [Jumpstart HCIBox FAQ](../faq/) for more information on consumption costs.

## Deployment Options and Flow

HCIBox supports [Bicep](https://learn.microsoft.com/azure/azure-resource-manager/bicep/overview?tabs=bicep) templates for both Azure CLI and [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview) to deploy and configure necessary Azure resources.

Deploying HCIBox is a multi-step process that includes:

  1) Deploy Azure infrastructure
  2) Automation scripts configure virtual Azure Local instance and generate ARM template
  3) User or automation deploys ARM template (Azure Local instance validate phase)
  4) User or automation re-deploys ARM template (Azure Local instance deploy phase)

![Screenshot showing deployment flow diagram for Bicep-based deployments](./deployment_flow.png)

## Deploy HCIBox
-	[Deploy HCIBox with Azure Developer CLI](/azure_jumpstart_hcibox/deployment_azd) : Best for those with access to Microsoft Entra ID
-	[Deploy HCIBox with Azure CLI](/azure_jumpstart_hcibox/deployment_az) : Alternative to Microsoft Entra ID, requires pre-configured service principle.

Looking for something else related to HCIBox?

- [Connect to HCIBox](/azure_jumpstart_hcibox/cloud_deployment)

- [HCIBox FAQ](/azure_jumpstart_hcibox/faq)