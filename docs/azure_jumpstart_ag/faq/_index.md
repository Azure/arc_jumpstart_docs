---
type: docs
linkTitle: "Agora FAQ"
weight: 5
---

# Jumpstart Agora Frequently Asked Questions (FAQ)

## What is Jumpstart Agora?

Jumpstart Agora is a marketplace of various “cloud-to-edge” industry scenarios, designed to provide an end-to-end user experience. The word "agora" comes from the ancient Greek term for a public gathering place or assembly, and it has come to be used more broadly to refer to any place or forum where people come together for discussion or exchange. Our mission is to create a rich marketplace of applications that can leverage Hybrid Cloud, Internet of Things (IoT), and artificial intelligence (AI) technologies and make those accessible for enablement and educational purposes via the Jumpstart automation mechanisms.

> **Note:** For general questions about Azure Arc Jumpstart please see the [Jumpstart FAQ](../../faq/).

## What industry scenarios are available in Jumpstart Agora?

Agora offers three industry scenarios, [Contoso Motors](/azure_jumpstart_ag/manufacturing/contoso_motors), [Contoso Supermarket](/azure_jumpstart_ag/retail/contoso_supermarket) and [Contoso Hypermarket](/azure_jumpstart_ag/manufacturing/contoso_hypermarket). Each industry scenario includes everything needed to deploy, configure, and use a real-world including CI/CD, observability, security, and more.

## What is required to deploy Agora?

Agora deployment requires an Azure service principal with **Contributor** or **Owner** role-based access control (RBAC) on an Azure subscription and resource group. You can deploy Agora using Azure Bicep. A service principal is required to run the automation scripts that deploy and configure Agora features. You can view how the service principal is used by exploring the Agora code on our [public GitHub repository](https://aka.ms/JumpstartGitHubCode).

## What Azure regions can Agora be deployed to?

Agora can be deployed to the following regions:

| Agora scenario | Region support |
| ------- | ----------- |
| Contoso Motors | eastus, eastus2, westus2, westus3, northeurope |
| Contoso Supermarket | eastus, eastus2, westus, westus2, northeurope, west europe |
| Contoso Hypermarket | eastus, eastus2, westus, westus2, westus3 |

## How much does it cost to use Agora?

Agora incurs normal Azure consumption charges for various Azure resources such as virtual machines and storage. Each industry scenario in Agora may use a different combination of Azure resources and therefore costs vary depending on the industry scenario used. You can view example estimates of Agora costs in the link below.

- [Contoso Motors cost estimate](https://aka.ms/AgoraContosoMotorsCostEstimate)
- [Contoso Supermarket cost estimate](https://aka.ms/AgoraContosoSupermarketCostEstimate)
- [Contoso Hypermarket cost estimate](https://aka.ms/AgoraContosoHypermarketCostEstimate)

## Where can I go if I have trouble deploying or using Agora?

Agora has a dedicated pages for troubleshooting that you can review for common issues.

- [Troubleshoot Contoso Motors](/azure_jumpstart_ag/manufacturing/contoso_motors/troubleshooting)
- [Troubleshoot Contoso Supermarket](/azure_jumpstart_ag/retail/contoso_supermarket/troubleshooting)
- [Troubleshoot Contoso Hypermarket](/azure_jumpstart_ag/retail/contoso_hypermarket/troubleshooting)

If you're still stuck, please [submit an issue](https://aka.ms/JumpstartIssue) on our GitHub repository and the Jumpstart team will try to assist as soon as we can..
