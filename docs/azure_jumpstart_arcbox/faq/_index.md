---
type: docs
linkTitle: "ArcBox FAQ"
weight: 5
---

# Jumpstart ArcBox Frequently Asked Questions (FAQ)

## What are the use cases for ArcBox?

ArcBox is a sandbox that can be used to explore Azure Arc capabilities, build quick demo environments, support proof-of-concept projects, and even provide a testing platform for specific scenarios. Customers, partners, and community members use ArcBox to quickly get hands-on with Azure Arc technology because it's quick to deploy and has minimal requirements.

## What is required to deploy ArcBox?

ArcBox deployment requires an Azure service principal with a **Contributor** or **Owner** role-based access control (RBAC) on an Azure subscription and resource group. You can deploy ArcBox using the Azure portal, Azure CLI, Bicep, or Terraform. A service principal is required to run the automation scripts that deploy and configure ArcBox features. You can view how the service principal is used by exploring the ArcBox code on our [public GitHub repository](https://aka.ms/JumpstartGitHubCode).

## What are the different "flavors" of ArcBox?

ArcBox offers four different “flavors” (configurations) that let users choose their own experience.

- [ArcBox Full](/azure_jumpstart_arcbox/Full) - The core ArcBox experience with Azure Arc-enabled servers, Kubernetes, and data services capabilities.
- [ArcBox for IT Pros](/azure_jumpstart_arcbox/ITPro/) - This essential Azure Arc-enabled servers sandbox includes a mix of Microsoft Windows and Linux servers managed using the included capabilities such as Azure Monitor, Microsoft Defender for Cloud, Azure Policy, Update Management, and more.
- [ArcBox for DevOps](/azure_jumpstart_arcbox/DevOps) - This essential Azure Arc-enabled Kubernetes sandbox includes capabilities such as GitOps, Open Service Mesh (OSM), secretes management, monitoring, and more.
- [ArcBox for DataOps](/azure_jumpstart_arcbox/DataOps) - This essential Azure Arc-enabled SQL Managed Instance sandbox includes capabilities such as Microsoft Active Directory authentication, disaster recovery, point-in-time restore, migration, and more.

## What Azure regions can ArcBox be deployed to?

ArcBox can be deployed to the following regions:

- East US
- East US 2
- Central US
- West US 2
- North Europe
- West Europe
- France Central
- UK South
- Australia East
- Japan East
- Korea Central
- Southeast Asia

## How much does it cost to use ArcBox?

ArcBox incurs normal Azure consumption charges for various Azure resources such as virtual machines and storage. Each flavor of ArcBox uses a different combination of Azure resources and therefore costs vary depending on the flavor used. You can view example estimates of ArcBox costs per flavor by clicking in the links below.

- [ArcBox Full cost estimate](https://aka.ms/ArcBoxFullCost)
- [ArcBox for IT Pros cost estimate](https://aka.ms/ArcBoxITProCost)
- [ArcBox for DevOps cost estimate](https://aka.ms/ArcBoxDevOpsCost)
- [ArcBox for DataOps cost estimate](https://aka.ms/ArcBoxDataOpsCost)

## Where can I go if I have trouble deploying or using ArcBox?

Each ArcBox flavor deployment guide has it's own troubleshooting section you can review for common issues.

- [Troubleshooting ArcBox Full](/azure_jumpstart_arcbox/Full/#basic-troubleshooting)
- [Troubleshooting ArcBox for IT Pros](/azure_jumpstart_arcbox/ITPro/#basic-troubleshooting)
- [Troubleshooting ArcBox for DevOps](/azure_jumpstart_arcbox/DevOps/#basic-troubleshooting)
- [Troubleshooting ArcBox for DataOps](/azure_jumpstart_arcbox/DataOps/#basic-troubleshooting)
