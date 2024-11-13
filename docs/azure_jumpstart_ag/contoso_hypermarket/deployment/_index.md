---
type: docs
weight: 1
title: Deployment guide
linkTitle: Deployment guide
---

## Overview

Jumpstart Agora provides a simple deployment process using Azure Bicep and PowerShell that minimizes user interaction. This automation automatically configures the Contoso Hypermarket scenario environment, including the infrastructure, the Contoso Hypermarket AI applications, CI/CD artifacts, observability components, and cloud architecture. The diagram below details the high-level architecture that's deployed and configured as part of the automation.

![Architecture diagram](./img/architecture_diagram.png)

Deploying the "Contoso Hypermarket" scenario consists of the following steps (once prerequisites are met).

  1. Deploy infrastructure - The user deploys a Bicep file that creates the infrastructure in an Azure resource group.
  2. Bicep template deploys multiple Azure resources including the Client virtual machine.
  3. Client VM uses a custom script extension to run the Bootstrap PowerShell script which initializes the environment.
  4. Bootstrap script injects the Logon script to the Client VM.
  5. User logs in to the _Agora-VM-Client_ Azure virtual machine.
  6. After login the _Agora-VM-Client_ PowerShell scripts automatically run that configure the infrastructure, applications and CI/CD. These scripts will take some time to run.

Once automation is complete, users can immediately start enjoying the Contoso Hypermarket experience.

![Deployment flow architecture diagram](./img/deployment_workflow.png)

## Prerequisites

- [Install or update Azure CLI to version 2.65.0 or above](https://learn.microsoft.com/cli/azure/install-azure-cli?view=azure-cli-latest). Use the following command to check your current installed version.

    ```shell
    az --version
    ```

- Login to Azure CLI using the *`az login`* command.

- Ensure that you have selected the correct subscription you want to deploy Agora to by using the *`az account list --query "[?isDefault]"`* command. If you need to adjust the active subscription used by az CLI, follow [this guidance](https://learn.microsoft.com/cli/azure/manage-azure-subscriptions-azure-cli#change-the-active-subscription).

- Register necessary Azure resource providers by running the following commands.

### Option 1: PowerShell

  ```powershell
    $providers = @(
        "Microsoft.Kubernetes",
        "Microsoft.KubernetesConfiguration",
        "Microsoft.ExtendedLocation",
        "Microsoft.HybridCompute",
        "Microsoft.OperationsManagement",
        "Microsoft.DeviceRegistry",
        "Microsoft.EventGrid",
        "Microsoft.IoTOperationsOrchestrator",
        "Microsoft.IoTOperations",
        "Microsoft.Fabric",
        "Microsoft.SecretSyncController"
    )

    foreach ($provider in $providers) {
        az provider register --namespace $provider --wait
    }
  ```

### Option 2: Shell

```shell
    providers=(
        "Microsoft.Kubernetes"
        "Microsoft.KubernetesConfiguration"
        "Microsoft.ExtendedLocation"
        "Microsoft.HybridCompute"
        "Microsoft.OperationsManagement"
        "Microsoft.DeviceRegistry"
        "Microsoft.EventGrid"
        "Microsoft.IoTOperationsOrchestrator"
        "Microsoft.IoTOperations"
        "Microsoft.Fabric"
        "Microsoft.SecretSyncController"
    )

    for provider in "${providers[@]}"; do
        az provider register --namespace "$provider" --wait
    done
  ```

> **Note:** The Jumpstart scenarios are designed with as much ease of use in mind and adhering to security-related best practices whenever possible. It's optional but highly recommended to scope the service principal to a specific [Azure subscription and resource group](https://learn.microsoft.com/cli/azure/ad/sp?view=azure-cli-latest) as well as considering using a [less privileged service principal account](https://learn.microsoft.com/azure/role-based-access-control/best-practices).

- Clone the Azure Arc Jumpstart repository

  ```shell
  git clone https://github.com/microsoft/azure_arc.git
  ```

### Regions and capacity

- Agora deploys multiple Azure services that are available in specific regions across the globe like Azure OpenAI and Azure IoT Operations. The list of supported regions per service is always expanding as Azure grows. At the moment, Agora must be deployed to one of the following regions to make sure you have a successful deployment. **Deploying Agora outside of these regions may result in unexpected results, deployment errors as some of the services deployed might not support that region.**

  - East US
  - East US 2
  - West US 2
  - West US 3
  - West Europe

> **Note:** Every subscription has different capacity restrictions and quotas so it's very critical to ensure you have sufficient vCPU quota available in your selected Azure subscription and the region where you plan to deploy Agora. If you encounter any capacity constraints error , please try another region from the list above.

- **Agora requires 32 Ds-series vCPUs and 8 Bs-series vCPUs**. You can use the below az CLI command to check your vCPU utilization.

  ```shell
  az vm list-usage --location <your location> --output table
  ```

  ![Screenshot showing az vm list-usage](./img/az_vm_list_usage.png)

- Contoso Hypermarket allows an option to deploy GPU-enabled worker nodes for the K3s Kubernetes clusters. If you select that option in the parameters file, then you can select one of a pre-defined list of GPU-enabled Virtual machines based on your subscription's available quotas. You can use the below az CLI command to check your vCPU utilization. **Depending on your Azure Subscription, you might be restricted to deploy GPU-enabled SKUs. Please check your utilization and quota availability before using the GPU option.**

  ```shell
  az vm list-usage --location <your location> --output table
  ```

- Contoso Hypermarket deploys Azure AI services (OpenAI and speech-to-text models). **Depending on your Azure Subscription, you might be restricted to deploy Cognitive Services accounts and/or Azure OpenAI models. Please check your utilization and quota availability before proceeding with the deployment.**

  ```shell
  az cognitiveservices usage list -l <your location> -o table --query "[].{Name:name.value, currentValue:currentValue, limit:limit}"
  ```

  ![Screenshot showing cognitive services usage](./img/check_ai_usage.png)

## Deployment: Bicep deployment via Azure CLI

- Upgrade to latest Bicep version

  ```shell
  az bicep upgrade
  ```

- Edit the [main.parameters.json](https://github.com/microsoft/azure_arc/blob/main/azure_jumpstart_ag/contoso_hypermarket/bicep/main.parameters.json) template parameters file and supply some values for your environment.
  - _`tenantId`_ - Your Azure tenant id
  - _`windowsAdminUsername`_ - Client Windows VM Administrator username
  - _`windowsAdminPassword`_ - Client Windows VM Password. Password must have 3 of the following: 1 lower case character, 1 upper case character, 1 number, and 1 special character. The value must be between 12 and 123 characters long.
  - _`deployBastion`_ - Option to deploy using Azure Bastion instead of traditional RDP. Set to *`true`* or *`false`*.
  - _`fabricCapacityAdmin`_ - Microsoft Fabric capacity admin (admin user ins the same Entra ID tenant).
  - _`deployGPUNodes`_ - Option to deploy GPU-enabled worker nodes for the K3s clusters.
  - _`k8sWorkerNodesSku`_ The K3s worker nodes VM SKU. If _`deployGPUNodes`_ is set to true, a GPU-enabled VM SKU needs to be provided in this parameter (Example: _`Standard_NV6ads_A10_v5`_).

  ![Screenshot showing example parameters](./img/parameters_bicep.png)

- You will need to get the Azure Custom Location Resource Provider (RP) Object ID (OID) and export it as an environment variable. This is required to enable [Custom Location](https://learn.microsoft.com/azure/azure-arc/platform/conceptual-custom-locations) on your cluster.

> **Note:** You need permissions to list all the service principals.

### Option 1: Bash

  ```shell
  customLocationRPOID=$(az ad sp list --filter "displayname eq 'Custom Locations RP'" --query "[?appDisplayName=='Custom Locations RP'].id" -o tsv)
  ```

### Option 2: PowerShell

  ```powershell
  $customLocationRPOID=(az ad sp list --filter "displayname eq 'Custom Locations RP'" --query "[?appDisplayName=='Custom Locations RP'].id" -o tsv)
  ```

- Now you will deploy the Bicep file. Navigate to the local cloned [deployment folder](https://github.com/microsoft/azure_arc/tree/main/azure_jumpstart_ag/contoso_hypermarket/bicep) and run the below command:

  ```shell
  az login
  az group create --name "<resource-group-name>"  --location "<preferred-location>"
  az deployment group create -g "<resource-group-name>" -f "main.bicep" -p "main.parameters.json" -p customLocationRPOID="$customLocationRPOID"
  ```

    > **Note:** If you see any failure in the deployment, please check the [troubleshooting guide](../troubleshooting/).

## Start post-deployment automation

Once your deployment is complete, you can open the Azure portal and see the Agora scenario resources inside your resource group. You will be using the _Agora-Client-VM_ Azure virtual machine to explore various capabilities of Agora. You will need to remotely access _Agora-Client-VM_.

  ![Screenshot showing all deployed resources in the resource group](./img/deployed_resources.png)

   > **Note:** For enhanced Agora security posture, RDP (3389) and SSH (22) ports aren't open by default in Agora deployments. You will need to create a network security group (NSG) rule to allow network access to port 3389, or use [Azure Bastion](https://learn.microsoft.com/azure/bastion/bastion-overview) or [Just-in-Time (JIT)](https://learn.microsoft.com/azure/defender-for-cloud/just-in-time-access-usage?tabs=jit-config-asc%2Cjit-request-asc) access to connect to the VM.

### Connecting to the Agora Client virtual machine

Various options are available to connect to _Agora-Client-VM_, depending on the parameters you supplied during deployment.

- [RDP](../deployment/#connecting-directly-with-rdp) - available after configuring access to port 3389 on the _Agora-NSG-Prod_, or by enabling [Just-in-Time access (JIT)](../deployment/#connect-using-just-in-time-access-jit).
- [Azure Bastion](../deployment/#connect-using-azure-bastion) - available if *`true`* was the value of your _`deployBastion`_ parameter during deployment.

#### Connecting directly with RDP

By design, Agora doesn't open port 3389 on the network security group. Therefore, you must create an NSG rule to allow inbound 3389.

- Open the _Agora-NSG-Prod_ resource in Azure portal and click "Add" to add a new rule.

  ![Screenshot showing adding a new inbound security rule](./img/nsg_add_rule.png)

- Select My IP address from the dropdown.

  <img src="./img/nsg_add_rdp_rule.png" alt="Screenshot showing adding a new allow RDP inbound security rule" width="400">

  <br/>

  ![Screenshot showing all inbound security rule](./img/nsg_rdp_all_rules.png)

  ![Screenshot showing connecting to the VM using RDP](./img/rdp_connect.png)

#### Connect using Azure Bastion

- If you have chosen to deploy Azure Bastion in your deployment, use it to connect to the VM.

  ![Screenshot showing connecting to the VM using Bastion](./img/bastion_connect.png)

  > **Note:** When using Azure Bastion, the desktop background image isn't visible. Therefore some screenshots in this guide may not exactly match your experience if you are connecting to _Agora-Client-VM_ with Azure Bastion.

#### Connect using just-in-time access (JIT)

If you already have [Microsoft Defender for Cloud](https://learn.microsoft.com/azure/defender-for-cloud/just-in-time-access-usage?tabs=jit-config-asc%2Cjit-request-asc) enabled on your subscription and would like to use JIT to access the Client VM, use the following steps:

- In the Client VM configuration pane, enable just-in-time. This will enable the default settings.

  ![Screenshot showing how to enable JIT](./img/enable_jit.png)

  ![Screenshot showing connecting to the VM using RDP](./img/connect_jit.png)

### The Logon scripts

- Once you log into the _Agora-Client-VM_, multiple automated scripts will open and start running. These scripts usually take around thirty minutes to finish, and once completed, the script windows will close automatically. At this point, the deployment is complete.

  ![Screenshot showing Agora-Client-VM](./img/automation.png)

- Deployment is complete! Let's begin exploring the features of Contoso Hypermarket!

  ![Screenshot showing complete deployment](./img/contoso_hypermarket_complete.png)

  ![Screenshot showing Agora resources in Azure portal](./img/rg_complete.png)

### Setup Microsoft Fabric workspace

Due to some limitations of automating Microsoft Fabric items in the Fabric workspace using a managed identity, users deploying Contoso Hypermarket have to run a setup script manually using the end user credentials that are used to access Microsoft Fabric workspace.

In order to create the Microsoft Fabric workspace, the tenant in which the workspace is created must have one of the following settings enabled. Users can verify these settings in [Microsoft Fabric Admin Portal](https://app.powerbi.com/admin-portal/tenantSettings?experience=power-bi). If you do not have permissions to access Microsoft Fabric Admin Portal, please contact your Entra ID tenant to confirm these settings.

1. Enabled for the entire organization.
1. User must be a member of the security group allowed to create workspace.
1. Not a member of the excluded security groups.

> **Note**: Microsoft Fabric do not support access as a guest user. Users will be redirected to their home tenant upon log into Microsoft Fabric.

  ![Screenshot showing Fabric tenant settings for workspace](./img/fabric-tenant-settings.png)

Once you log into _Agora-Client-VM_ using any of the method described above follow the steps below to run the script

- Open Windows Explorer and navigate to _C:\Ag\Fabric_ folder and make sure there are two files located in the folder.

  ![Screenshot showing Fabric workspace setup files](./img/fabric-script-files.png)

- Open Windows PowerShell command-line tool from Start menu

  ![Screenshot showing PowerShell command-line tool launch](./img/ag-client-launch-powershell.png)

- Change directory to _C:\Ag\Fabric_

- Run the script file as shown below and follow the onscreen instructions to login to the Entra ID tenant.

  ![Screenshot showing location of fabric setup PowerShell script](./img/fabric-run-script.png)

- Users are prompted to complete authentication using a device code to log into the Entra ID tenant to create fabric workspace. Copy 1) device authentication URL and 2) Code from the command-line as shown below.

  ![Screenshot showing device authentication URL and code](./img/fabric-device-authentication.png)

- Open Edge browser and access the URL copied above and enter the code to complete authentication.

  ![Screenshot showing device code prompt in the browser](./img/fabric-enter-device-code.png)

- Select subscription when prompted to select as shown below and press enter

  ![Screenshot showing subscription selection](./img/fabric-select-subsription.png)

- Once the script executed successfully without any issues, output of the script looks like below. If there are any errors open the script log file to review any issues and follow troubleshooting instructions below in this document.

  ![Screenshot showing results of successful script execution](./img/fabric-script-output.png)

- Access Contoso Hypermarket workspace by log into [Microsoft Fabric](https://app.fabric.microsoft.com/) and complete authentication. Fabric home page will look like below

  ![Screenshot showing Microsoft Fabric home page](./img/fabric-home-page.png)

- Click on Power BI to view workspaces and access Contoso Hypermarket workspace

  ![Screenshot showing choosing Power BI](./img/fabric-home-page.png)

- Click on Workspaces to view all available workspaces. Contoso Hypermarket workspaces have created with the naming standard _contoso-hypermarket-<naming_guid>_, where _naming_guid_ can be found in the Azure Portal resource group.

  ![Screenshot showing view workspaces](./img/fabric-view-workspaces.png)

- Open the workspace created to view Fabric items

  ![Screenshot showing open workspace](./img/fabric-open-workspace.png)

- Screenshot below shows all the items created for the Contoso Hypermarket
  
  ![Screenshot showing workspace items](./img/fabric-workspace-items.png)

## Next steps

Once deployment is complete its time to start experimenting with the various scenarios under the “Contoso Hypermarket” experience, starting with the [“Data pipeline and reporting across cloud and edge for Contoso Hypermarket”](../data_pipeline/).
