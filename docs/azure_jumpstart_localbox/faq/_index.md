---
type: docs
linkTitle: "LocalBox FAQ"
weight: 7
---

# Jumpstart LocalBox Frequently Asked Questions (FAQ)

## What is Jumpstart LocalBox?

Jumpstart LocalBox is a turnkey solution that provides a complete sandbox for exploring Azure Local capabilities and hybrid cloud integration in a virtual environment. LocalBox is designed to be completely self-contained within a single Azure subscription and resource group, which makes it easy for users to get hands-on with Azure Local and Azure Arc technology without the need for physical hardware.

> **Note:** For general questions about Arc Jumpstart please see the [Jumpstart FAQ](../../faq/).

## What is required to deploy LocalBox?

LocalBox deployment requires a user with Owner role-based access control (RBAC) on an Azure subscription and can be deployed using Azure Bicep. A Managed Identity is provisioned by the Bicep template to authenticate to Azure in the automation scripts that deploy and configure LocalBox features. You can view how the Managed Identity is used by exploring the LocalBox code on our [public GitHub repository](https://github.com/microsoft/azure_arc).

## What Azure regions can LocalBox be deployed to?

LocalBox can be deployed in any region with sufficient compute capacity (vCPU quotas) for the chosen VM SKU (Standard E32s v5 or v6).

LocalBox has been tested in the following Azure regions:

- East US
- Australia East
- Canada Central
- Norway East
- Sweden Central
- North Europe
- West Europe

Some LocalBox resources are deployed in [specific regions](https://learn.microsoft.com/en-us/azure/azure-local/concepts/system-requirements-23h2?view=azloc-2505&tabs=azure-public#azure-requirements) where required services are available:

- East US
- West Europe
- Australia East
- Southeast Asia
- India Central
- Canada Central
- Japan East
- South Central US

This can be controlled by specifying the `azureLocalInstanceLocation` deployment parameter.

## How much will it cost to use LocalBox?

LocalBox incurs normal Azure consumption charges for various Azure resources such as virtual machines and storage.

Consider using [Azure Spot VMs](https://learn.microsoft.com/azure/virtual-machines/spot-vms) to reduce compute costs, though this may result in eviction when Azure needs capacity. This can be enabled by specifying the value `true` for the `enableAzureSpotPricing` deployment parameter.

You can view example estimates of LocalBox costs in the links below.

- [LocalBox cost estimate](https://aka.ms/LocalBoxCost)

## Which versions of Azure Local does LocalBox support?

LocalBox uses the 24H2 build of the [Azure Local OS](https://learn.microsoft.com/azure/azure-local/deploy/operating-system?view=azloc-2505).

## Where can I go if I have trouble deploying or using LocalBox?

If you're stuck, please [submit an issue](https://github.com/microsoft/azure_arc/issues/new/choose) on the Jumpstart GitHub repository and the Jumpstart team will try to assist you.
