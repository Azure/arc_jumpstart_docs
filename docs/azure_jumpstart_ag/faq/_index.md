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
| Contoso Hypermarket | eastus, eastus2, westus2, westus3, westeurope |
| Contoso Motors | eastus, eastus2, westus2, westus3, northeurope |
| Contoso Supermarket | eastus, eastus2, westus, westus2, northeurope, west europe |

## How much does it cost to use Agora?

Agora incurs normal Azure consumption charges for various Azure resources such as virtual machines and storage. Each industry scenario in Agora may use a different combination of Azure resources and therefore costs vary depending on the industry scenario used. You can view example estimates of Agora costs in the link below.

- Contoso Hypermarket cost estimate has multiple deployment options:
  - [Contoso Hypermarket standard deployment cost estimate](https://aka.ms/AgoraContosoHypermarketCostEstimate)
    - [Contoso Hypermarket with GPU-enabled SKUs option 1 cost estimate](https://aka.ms/AgoraContosoHypermarketCostEstimateGPU1)
    - [Contoso Hypermarket with GPU-enabled SKUs option 2 cost estimate](https://aka.ms/AgoraContosoHypermarketCostEstimateGPU2)
- [Contoso Motors cost estimate](https://aka.ms/AgoraContosoMotorsCostEstimate)
- [Contoso Supermarket cost estimate](https://aka.ms/AgoraContosoSupermarketCostEstimate)

## Where can I go if I have trouble deploying or using Agora?

Agora has a dedicated pages for troubleshooting that you can review for common issues.

- [Troubleshoot Contoso Hypermarket](/azure_jumpstart_ag/retail/contoso_hypermarket/troubleshooting)
- [Troubleshoot Contoso Motors](/azure_jumpstart_ag/manufacturing/contoso_motors/troubleshooting)
- [Troubleshoot Contoso Supermarket](/azure_jumpstart_ag/retail/contoso_supermarket/troubleshooting)

## What AI models are used in Jumpstart Agora?

Jumpstart Agora uses a combination of the following AI models:

- **Azure OpenAI** for general AI tasks.
- **Microsoft _Phi-3-Mini-4K-Instruct_ model**, a specialized language model for advanced natural language processing.
- **Intel OpenVINO models**, which are designed for optimized deployment of AI models on Intel hardware.

## What is the license for the Microsoft Phi-3-Mini-4K-Instruct model?**

The **_Phi-3-Mini-4K-Instruct_** model by Microsoft is licensed under the [MIT License](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/LICENSE). You can review the full details of the license in the `LICENSE` file located in the Jumpstart Agora repository.

## What license applies to Intel OpenVINO models?

The **Intel OpenVINO** models are distributed under the **Apache License 2.0**. You can view the full terms of the license in the [Intel OpenVINO License file](https://github.com/openvinotoolkit/openvino/blob/master/LICENSE).

## Can I use these models in my own projects?

Yes, as long as you comply with the respective licenses. For the Microsoft _Phi-3-Mini-4K-Instruct_ model, you must adhere to the terms of the MIT License. For Intel OpenVINO, the Apache License 2.0 governs the usage. Make sure to review each model’s license to understand the permissions and restrictions.

## Can I modify and distribute the models used in Jumpstart Agora?

- **Microsoft _Phi-3-Mini-4K-Instruct_ model**: You are permitted to modify and distribute the model under the MIT License, as long as you include the appropriate copyright notice and disclaimers.
- **Intel OpenVINO models**: You are allowed to modify and distribute Intel OpenVINO models under the terms of the Apache License 2.0, with the conditions outlined in the license.

## Is there any support or documentation available for using these models?

- For **Azure OpenAI** and **_Phi-3-Mini-4K-Instruct_** model, refer to the [Azure OpenAI documentation](https://learn.microsoft.com/azure/cognitive-services/openai/) and the official [Hugging Face repository for the _Phi-3-Mini-4K-Instruct_ model](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct).
- For **Intel OpenVINO**, you can access detailed documentation and support from the [OpenVINO GitHub repository](https://github.com/openvinotoolkit/openvino) and the official Intel documentation.

## What if I am still required assistance?

If you're still stuck, please [submit an issue](https://aka.ms/JumpstartIssue) on our GitHub repository and the Jumpstart team will try to assist as soon as we can.
