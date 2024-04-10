---
type: docs
title: "Discover Edge Storage Accelerator on AKS Edge Essentials single node deployment"
linkTitle: "Discover Edge Storage Accelerator on AKS Edge Essentials single node deployment"
weight: 8
description: >
---

## Discover Edge Storage Accelerator on AKS Edge Essentials single node deployment 

The following Jumpstart scenario showcases Edge Storage Accelerator (ESA), which is a storage system designed for Arc-enabled Kubernetes clusters to provide reliable, fault tolerant storage in a *ReadWriteMany* persistent volume. The Edge Storage Accelerator provides a constantly connected conduit for edge data to be replicated to blob storage in the cloud while maintaining a local copy, as space permits, for low-latency local access.

> ⚠️ **Disclaimer:** The Edge Storage Accelerator is currently in private preview and not generally available. Access to the feature may be limited and subject to specific terms and conditions. For further details and updates on availability, please refer to the [Edge Storage Accelerator Documentation](https://review.learn.microsoft.com/en-us/azure/azure-arc/edge-storage-accelerator/overview?branch=pr-en-us-268178).

> **Note:** 🧪 For access to the preview, please complete this [questionnaire](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR19S7i8RsvNAg8hqZuHbEyxUNTEzN1lDT0s3SElLTDc5NlEzQTE2VVdKNi4u) about your environment and use-case. We want to be sure that our customers will be successful in their testing! Once you have submitted your responses, one of the ESA PMs will get back to you with an update on your request! 
🪲 If you found a bug or have an issue, please complete the [Edge Storage Accelerator Request Support Form](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR19S7i8RsvNAg8hqZuHbEyxUOVlRSjJNOFgxNkRPN1IzQUZENFE4SjlSNy4u).


In this scenario, a computer vision AI model detects defects in bolts by analyzing video from a supply line video feed streamed over RTSP. The identified defects are then stored in a container within a storage account using ESA.

The automation in this scenario deploys Edge Storage Accelerator on an AKS Edge Essentials single-node deployment running in an Azure virtual machine. The provided ARM template creates the Azure resources and configures the LogonScript.ps1 custom script extension which handles AKS Edge Essentials cluster creation, Azure Arc onboarding for the Azure VM and AKS Edge Essentials cluster, and Edge Storage Accelerator deployment. Once AKS Edge Essentials is deployed [Edge Storage Accelerator](https://learn.microsoft.com/azure/azure-arc/edge-storage-accelerator/overview) is installed as a Kubernetes service that exposes a CSI driven storage class for use by applications in the Edge Essentials Kubernetes cluster.

![Screenshot ARM template output](./01.png)

## Prerequisites

- [Install or update Azure CLI to version 2.53.0 and above](https://learn.microsoft.com/cli/azure/install-azure-cli?view=azure-cli-latest). Use the below command to check your current installed version.

  ```shell
  az --version
  ```

- In case you don't already have one, you can [Create a free Azure account](https://azure.microsoft.com/free/).

- Create Azure service principal (SP)

    To complete the scenario and its related automation, an Azure service principal with the “Contributor” role assigned is required. To create it, login to your Azure account and run the below command (this can also be done in [Azure Cloud Shell](https://shell.azure.com/).

    ```shell
    az login
    subscriptionId=$(az account show --query id --output tsv)
    az ad sp create-for-rbac -n "<Unique SP Name>" --role "Contributor" --scopes /subscriptions/$subscriptionId
    ```

    For example:

    ```shell
    az login
    subscriptionId=$(az account show --query id --output tsv)
    az ad sp create-for-rbac -n "JumpstartArc" --role "Contributor" --scopes /subscriptions/$subscriptionId
    ```

    Output should look like this:

    ```json
    {
    "appId": "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "displayName": "JumpstartArc",
    "password": "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "tenant": "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    }
    ```

    > **Note:** If you create multiple subsequent role assignments on the same service principal, your client secret (password) will be destroyed and recreated each time. Therefore, make sure you grab the correct password.

    > **Note:** The Jumpstart scenarios are designed with ease of use in-mind and adhere to security-related best practices whenever possible. It is optional but highly recommended to scope the service principal to a specific [Azure subscription and resource group](https://learn.microsoft.com/cli/azure/ad/sp?view=azure-cli-latest) as well as considering use of a [less privileged service principal account](https://learn.microsoft.com/azure/role-based-access-control/best-practices).


## Automation Flow

The automation and deployment flow of the scenario proceeds as follows:

- User edits the ARM template parameters file (1-time edit). These parameter values are used throughout the deployment.

- Main [_azuredeploy_ ARM template](https://github.com/microsoft/azure_arc/blob/main/azure_edge_iot_ops_jumpstart/esa_fault_detection/azuredeploy.json) will initiate the deployment of the following resources:

  - _Virtual Network_ - Virtual Network for Azure Windows Server VM.
  - _Network Interface_ - Network Interface for Azure Windows Server VM.
  - _Network Security Group_ - Network Security Group to allow RDP in Azure Windows Server VM.
  - _Virtual Machine_ - Azure Windows Server VM.
  - _Custom script and Azure Desired State Configuration extensions_ - Configure the Azure Windows Server VM to host AKS Edge Essentials.

- User remotes into client Windows VM, which automatically kicks off the [_LogonScript_](https://github.com/microsoft/azure_arc/blob/main/azure_edge_iot_ops_jumpstart/esa_fault_detection/artifacts/LogonScript.ps1) PowerShell script to:
  - Create the AKS Edge Essentials cluster in the Windows Server VM
  - Onboard the Azure VM and AKS Edge Essentials cluster to Azure Arc
  - Deploy ESA and Fault Detection Model

## Deployment

As mentioned, this deployment will leverage ARM templates. You will deploy a single template, responsible for creating all the Azure resources in a single resource group as well onboarding the created VM to Azure Arc.

- Clone the Azure Arc Jumpstart repository

    ```shell
    git clone https://github.com/microsoft/azure_arc.git
    ```

- Before deploying the ARM template, login to Azure using Azure CLI with the *`az login`* command.

- The deployment uses the ARM template parameters file. Before initiating the deployment, edit the [_azuredeploy.parameters.json_](https://github.com/microsoft/azure_arc/blob/main/azure_edge_iot_ops_jumpstart/esa_fault_detection/azuredeploy.parameters.json) file located in your local cloned repository folder.

  - _`vmSize`_ - Client Windows VM size.
  - _`vmName`_ - Client Windows VM name.
  - _`kubernetesDistribution`_ - Choice (k8s | k3s) kubernetes distribution.
  - _`windowsNode`_ - Choice (true | false) to deploy AKS Windows Node.
  - _`adminUsername`_ - Client Windows VM Administrator username.
  - _`adminPassword`_ - Client Windows VM Password. Password must have 3 of the following: 1 lower case character, 1 upper case character, 1 number, and 1 special character. The value must be between 12 and 123 characters long.
  - _`appId`_ - Your Azure service principal id.
  - _`password`_ - Your Azure service principal secret.
  - _`tenantId`_ - Your Azure tenant id.
  - _`subscriptionId`_ - Your Subscription ID.
  - _`location`_ - Azure location.
  - _`deployBastion`_ - Choice (true | false) to deploy [Azure Bastion](https://learn.microsoft.com/azure/bastion/bastion-overview) or not to connect to the client VM.
  - _`bastionHostName`_ - Azure Bastion name.
  - _`storageAccountName`_ - Azure Storage Account Name
  - _`storageContainer`_ - Container in Storage Account (Leave this unmodified for a quick deployment)

- To deploy the ARM template, navigate to the local cloned [deployment folder](https://github.com/microsoft/azure_arc/blob/main/azure_edge_iot_ops_jumpstart/esa_fault_detection/) and run the below command:

    ```shell
    az group create --name <Name of the Azure resource group> --location <Azure Region>
    az deployment group create \
    --resource-group <Name of the Azure resource group> \
    --name <The name of this deployment> \
    --template-uri https://raw.githubusercontent.com/microsoft/azure_arc/main/azure_edge_iot_ops_jumpstart/esa_fault_detection/azuredeploy.json \
    --parameters <The _azuredeploy.parameters.json_ parameters file location>
    ```

    > **Note:** Make sure that you are using the same Azure resource group name as the one you've just used in the _azuredeploy.parameters.json_ file.

    For example:

    ```shell
    az group create --name AKS-EE-ESA-Demo --location "East US 2"
    az deployment group create \
    --resource-group AKS-EE-ESA-Demo \
    --name akseedemo \
    --template-uri https://raw.githubusercontent.com/microsoft/azure_arc/main/azure_edge_iot_ops_jumpstart/esa_fault_detection/azuredeploy.json \
    --parameters azuredeploy.parameters.json
    ```

    > **Note:** If you receive an error message stating that the requested VM size is not available in the desired location (as an example: '*Standard_D8s_v3*'), it means that there is currently a capacity restriction for that specific VM size in that particular region. Capacity restrictions can occur due to various reasons, such as high demand or maintenance activities. Microsoft Azure periodically adjusts the available capacity in each region based on usage patterns and resource availability. To continue deploying this scenario, please try to re-run the deployment using another region.

- Once Azure resources have been provisioned, you will be able to see them in Azure portal.

    ![Screenshot ARM template output](./02.png)

    ![Screenshot resources in resource group](./03.png)

## Windows Login & Post Deployment

Various options are available to connect to _ESA-Win-Demo_ Azure VM, depending on the parameters you supplied during deployment.

- [RDP](#connecting-directly-with-rdp) - available after configuring access to port 3389 on the _Arc-App-Client-NSG_, or by enabling [Just-in-Time access (JIT)](#connect-using-just-in-time-access-jit).
- [Azure Bastion](#connect-using-azure-bastion) - available if *`true`* was the value of your _`deployBastion`_ parameter during deployment.

### Connecting directly with RDP

By design, port 3389 is not allowed on the network security group. Therefore, you must create an NSG rule to allow inbound 3389.

- Open the _ESA-Win-Demo-NSG_ resource in Azure portal and click "Add" to add a new rule.

  ![Screenshot showing AKS-EE-Demo-NSG NSG with blocked RDP](./04.png)

  ![Screenshot showing adding a new inbound security rule](./05.png)

- Specify the IP address that you will be connecting from and select RDP as the service with "Allow" set as the action. You can retrieve your public IP address by accessing [https://icanhazip.com](https://icanhazip.com) or [https://whatismyip.com](https://whatismyip.com).

  ![Screenshot showing all inbound security rule](./06.png)

  ![Screenshot showing all NSG rules after opening RDP](./07.png)

  ![Screenshot showing connecting to the VM using RDP](./08.png)

### Connect using just-in-time access (JIT)

If you already have [Microsoft Defender for Cloud](https://learn.microsoft.com/azure/defender-for-cloud/just-in-time-access-usage?tabs=jit-config-asc%2Cjit-request-asc) enabled on your subscription and would like to use JIT to access the Azure Client VM, use the following steps:

- In the Client VM configuration pane, enable just-in-time. This will enable the default settings.

  ![Screenshot showing the Microsoft Defender for cloud portal, allowing RDP on the client VM](./10.png)

  ![Screenshot showing connecting to the VM using JIT](./11.png)

### Connect using Azure Bastion

- If you have chosen to deploy Azure Bastion in your deployment, use it to connect to the Azure VM.

  ![Screenshot showing connecting to the VM using Bastion](./09.png)

  > **Note:** When using Azure Bastion, the desktop background image is not visible. Therefore some screenshots in this guide may not exactly match your experience if you are connecting with Azure Bastion.

### Post Deployment

- At first login, as mentioned in the "Automation Flow" section, a logon script will get executed. This script was created as part of the automated deployment process.

- Let the script to run its course and **do not close** the Powershell session, this will be done for you once completed.

    > **Note:** The script run time is ~13min long.

    ![Screenshot script output](./12.png)

    ![Screenshot script output](./13.png)

    ![Screenshot script output](./14.png)

    ![Screenshot script output](./15.png)

    ![Screenshot script output](./16.png)

    ![Screenshot script output](./17.png)

    ![Screenshot script output](./18.png)

    ![Screenshot script output](./19.png)

    ![Screenshot script output](./38.png)

- Upon successful run, a new Azure Arc-enabled server and Azure Arc-enabled Kubernetes cluster will be added to the resource group.

![Screenshot Azure Arc-enabled server on resource group](./22.png)

- You can also run _kubectl get nodes -o wide_ to check the cluster node status and _kubectl get pod -A_ to see that the cluster is running and all the needed pods (system and [the Arc-enabled Kubernetes extension pods](https://learn.microsoft.com/azure/azure-arc/kubernetes/extensions)) are in a running state.

![Screenshot kubectl get nodes -o wide](./36.png)

![Screenshot kubectl get pod -A](./37.png)

## Edge Storage Accelerator: Real-Time Defect Detection in Manufacturing

Once installed, you will need to open a PowerShell on the *ESA-Win-Demo* server and obtain the IP and service port for the demonstration application. 

![Screenshot kubectl get svc](./32.png)

Use the *esa-webserver-svc* EXTERNAL-IP and PORT to reach the application web frontend.

![Screenshot of web application](./33.png)

Before the application runs, the *Logon.ps1* script will create a container in the *StorageAccountName* the user configured in *azuredeploy.parameters.json*.

![Screenshot of Azure Portal Storage Account](./39.png)

After the application runs, you can validate that the detected objects have been saved to your blob storage account container.

![Screenshot of Azure Portal Storage Account](./34.png)

### Exploring logs from the Client VM

Occasionally, you may need to review log output from scripts that run on the _ESA-Win-Demo_ VM in case of deployment failures. To make troubleshooting easier, the scenario deployment scripts collect all relevant logs in the _C:\Temp_ folder on _ESA-Win-Demo_ Azure VM. A short description of the logs and their purpose can be seen in the list below:

| Log file | Description |
| ------- | ----------- |
| _C:\Temp\Bootstrap.log_ | Output from the initial _bootstrapping.ps1_ script that runs on _ESA-Win-Demo_ Azure VM. |
| _C:\Temp\LogonScript.log_ | Output of _LogonScript.ps1_ which creates the AKS Edge Essentials cluster, onboard it with Azure Arc creating the needed extensions for Edge Storage Accelerator, storage account, storage container, and the kubernetes deployment for running the fault detection scenario |

![Screenshot showing the Temp folder with deployment logs](./30.png)

## Cleanup

- If you want to delete the entire environment, simply delete the deployment resource group from the Azure portal.

    ![Screenshot showing Azure resource group deletion](./31.png)
