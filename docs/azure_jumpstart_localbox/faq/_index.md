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

LocalBox deployment requires an Azure service principal with Owner role-based access control (RBAC) on an Azure subscription and resource group and can be deployed using Azure Bicep. A service principal is required to run the automation scripts that deploy and configure LocalBox features. You can view how the service principal is used by exploring the LocalBox code on our [public GitHub repository](https://github.com/microsoft/azure_arc).

## What Azure regions can LocalBox be deployed to?

LocalBox has been tested in the following Azure regions. Some LocalBox resources are deployed in specific regions where required services are available.

- East US
- Australia East
- Canada Central
- West Europe

## How much will it cost to use LocalBox?

LocalBox incurs normal Azure consumption charges for various Azure resources such as virtual machines and storage. You can view example estimates of LocalBox costs in the links below.

- [LocalBox cost estimate](https://aka.ms/LocalBoxCost)

## Which versions of Azure Local does LocalBox support?

LocalBox uses the 23H2 build of the Azure Stack HCI OS.

## Where can I go if I have trouble deploying or using LocalBox?

If you're stuck, please [submit an issue](https://github.com/microsoft/azure_arc/issues/new/choose) on the Jumpstart GitHub repository and the Jumpstart team will try to assist you.
