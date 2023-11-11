---
type: docs
linkTitle: "HCIBox FAQ"
weight: 6
---

## Jumpstart HCIBox Frequently Asked Questions (FAQ)

## What is Jumpstart HCIBox?

Jumpstart HCIBox is a turnkey solution that provides a complete sandbox for exploring Azure Stack HCI capabilities and hybrid cloud integration in a virtual environment. HCIBox is designed to be completely self-contained within a single Azure subscription and resource group, which makes it easy for users to get hands-on with Azure Stack HCI and Azure Arc technology without the need for physical hardware.

> **Note:** For general questions about Azure Arc Jumpstart please see the [Jumpstart FAQ](../../faq/).

## What is required to deploy HCIBox?

HCIBox deployment requires an Azure service principal with Owner role-based access control (RBAC) on an Azure subscription and resource group. You can deploy HCIBox using Azure Bicep or the [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview). A service principal is required to run the automation scripts that deploy and configure HCIBox features. You can view how the service principal is used by exploring the HCIBox code on our [public GitHub repository](https://github.com/microsoft/azure_arc).

## What Azure regions can HCIBox be deployed to?

HCIBox can be deployed to the following regions:

- East US
- East US 2
- West US 2
- North Europe

## How much will it cost to use HCIBox?

HCIBox incurs normal Azure consumption charges for various Azure resources such as virtual machines and storage. You can view example estimates of HCIBox costs in the links below.

- [HCIBox cost estimate](https://aka.ms/HCIBoxCost)

## Where can I go if I have trouble deploying or using HCIBox?

If you're stuck, please [submit an issue](https://github.com/microsoft/azure_arc/issues/new/choose) on our GitHub repository and the Jumpstart team will try to assist you as soon as we can.
