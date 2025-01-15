---
type: docs
linkTitle: "ArcBox for DataOps"
weight: 5
---

# Jumpstart ArcBox for DataOps

## Overview

ArcBox for DataOps is a special "flavor" of ArcBox that's intended for users who want to experience Azure Arc-enabled SQL Managed Instance capabilities in a sandbox environment.

![Screenshot showing ArcBox architecture diagram](./arch_dataops.png)

### Use cases

- Sandbox environment for getting hands-on with Azure Arc technologies and [Azure Arc-enabled SQL Managed Instance landing zone accelerator](https://aka.ms/ArcLZAcceleratorReady)
- Accelerator for Proof-of-concepts or pilots
- Training solution for Azure Arc skills development
- Demo environment for customer presentations or events
- Rapid integration testing platform
- Infrastructure-as-code and automation template library for building hybrid cloud management solutions

## Azure Arc capabilities available in ArcBox for DataOps

### Azure Arc-enabled Kubernetes

ArcBox for DataOps deploys three Kubernetes clusters to give you multiple options for exploring Azure Arc-enabled Kubernetes capabilities and potential integrations.

- _**ArcBox-K3s-Data-xxxx**_ - A single-node Rancher K3s cluster running on an Azure virtual machine. The cluster is onboarded as an Azure Arc-enabled Kubernetes resource. ArcBox automatically deploys an Azure Arc Data Controller, an Active Directory connector and an Azure Arc-enabled SQL Managed Instance on top of the connected cluster.
- _**ArcBox-AKS-Data-xxxx**_ - An AKS cluster that's connected to Azure as an Azure Arc-enabled Kubernetes resource. ArcBox automatically deploys an Azure Arc Data Controller, an Active Directory connector and an Azure Arc-enabled SQL Managed Instance on top of the connected cluster.
- _**ArcBox-AKS-DR-Data-xxxx**_ - An AKS cluster that's deployed in a separate virtual network, designating a disaster recovery site. This cluster is then connected to Azure as an Azure Arc-enabled Kubernetes resource. ArcBox automatically deploys an Azure Arc Data Controller, an Active Directory connector and an Azure Arc-enabled SQL Managed Instance on top of the connected cluster. This cluster is then configured with _ArcBox-K3s-Data-xxxx_ to be part of a distributed availability group for disaster recovery.

### Sample applications

ArcBox for DataOps deploys two sample applications on the _ArcBox-K3s-Data-xxxx_ and the _ArcBox-AKS-DR-Data-xxxx_ clusters.

The sample applications included in ArcBox are:

- **The Bookstore Application** - An MVC web application. ArcBox will deploy **one Kubernetes pod replica** of the _Bookstore_ application in the _arc_ namespace onto the _ArcBox-K3s-Data-xxxx_ and the _ArcBox-AKS-DR-Data-xxxx_ clusters.

- **DB Connection Application** - An MVC application. ArcBox will deploy **one Kubernetes pod replica** as part of the DB connection app and an Ingress controller to demonstrate the active connections to the different Azure Arc-enabled SQL Managed Instances replicas.

### Azure Monitor integration

ArcBox deploys metrics and logs upload to Azure Monitor for the deployed data services, in addition to the out-of-the-box Grafana and Kibana dashboards that get deployed as part of Arc-enabled Data services.

### Unified Operations

ArcBox allows you to experience various Azure Arc-enabled SQL Managed Instance unified operations like Point-in-Time restore, disaster recovery, high availability, monitoring and migration. Once deployed, you will be able to connect to the SQL instances deployed on the three clusters and test different operations with the aid of a bookstore application.

## ArcBox Azure Costs

ArcBox resources generate Azure consumption charges from the underlying Azure resources including core compute, storage, networking, and auxiliary services. Note that Azure consumption costs vary depending on the region where ArcBox is deployed. Be mindful of your ArcBox deployments and ensure that you disable or delete ArcBox resources when not in use to avoid unwanted charges.  In an effort to reduce the costs, by default the client VM will auto-shutdown at 1800 UTC.  This can be changed either during the deployment by altering the parameters for autoShutdownEnabled, autoShutdownTime, and autoShutdownTimezone within the Bicep template or after deployment by changing the [auto-shutdown](https://learn.microsoft.com/azure/virtual-machines/auto-shutdown-vm?tabs=portal) parameters from the Azure Portal.  When the ArcBox-Client VM is stopped, there will be no compute charges; however, there will still be charges for the storage components.  In addition, [Azure Spot VMs](https://learn.microsoft.com/azure/virtual-machines/spot-vms) can be used to reduce the compute costs of ArcBox.  Using this option may result in the _ArcBox-Client_ being evicted when Azure needs the capacity and the VM will no longer be available.

![screenshot showing the auto-shutdown parameters in the Azure Portal](./arcbox-client-auto-shutdown.png)

Please see the [Jumpstart FAQ](../../faq/) for more information on consumption costs.

## Deployment Options and Automation Flow

ArcBox provides multiple paths for deploying and configuring ArcBox resources. Deployment options include:

- Azure portal
- Azure Bicep

![Deployment flow diagram for ARM-based deployments](./deployment_flow.png)

ArcBox uses an advanced automation flow to deploy and configure all necessary resources with minimal user interaction. The previous diagrams provide an overview of the deployment flow. A high-level summary of the deployment is:

- User deploys the Bicep template (_main.bicep_). These objects contain several nested objects that will run simultaneously.
  - Client virtual machine ARM template/plan - deploys a domain-joined Client Windows VM. This is a Windows Server VM that comes preconfigured with kubeconfig files to work with the three Kubernetes clusters, as well multiple tools such as Visual Studio Code, Azure Data Studio and SQL Server Management Studio to make working with ArcBox simple and easy.
  - Storage account template/plan - used for staging files in automation scripts.
  - Management artifacts template/plan - deploys Azure Log Analytics workspace, its required Solutions, a domain controller and two virtual networks.
- User remotes into the Client Windows VM using domain credentials, which automatically kicks off multiple scripts that:
  - Onboards the AKS clusters to Azure Arc as Arc-enabled Kubernetes clusters.
  - Deploys a data controller, AD connector and an Azure Arc-enabled SQL Managed Instance on each cluster.
  - Creates the necessary DNS records for the Azure Arc-enabled SQL Managed Instance's endpoints.
  - Configures a distributed availability group between the Azure Arc-enabled SQL Managed Instances deployed on the _ArcBox-K3s-Data-xxxx_ and the _ArcBox-AKS-DR-Data-xxxx_ clusters.
  - Deploys the _Bookstore_ application on the _ArcBox-K3s-Data-xxxx_ and the _ArcBox-AKS-DR-Data-xxxx_ clusters.
  - Deploy an Azure Monitor workbook that provides example reports and metrics for monitoring and visualizing ArcBox's various components.

## Prerequisites

- [Install or update Azure CLI to version 2.65.0 and above](https://learn.microsoft.com/cli/azure/install-azure-cli?view=azure-cli-latest). Use the below command to check your current installed version.

  ```shell
  az --version
  ```

- Login to Azure CLI using the _`az login`_ command.

- Ensure that you have selected the correct subscription you want to deploy ArcBox to by using the _`az account list --query "[?isDefault]"`_ command. If you need to adjust the active subscription used by Azure CLI, follow [this guidance](https://learn.microsoft.com/cli/azure/manage-azure-subscriptions-azure-cli#change-the-active-subscription).

- ArcBox must be deployed to one of the following regions. **Deploying ArcBox outside of these regions may result in unexpected behavior or deployment errors.**

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

- **ArcBox DataOps requires 42 B-series vCPUs and 56 DSv5 vCPUs** when deploying with default parameters such as VM series/size. Ensure you have sufficient vCPU quota available in your Azure subscription and the region where you plan to deploy ArcBox. You can use the below Azure CLI command to check your vCPU utilization.

  ```shell
  az vm list-usage --location <your location> --output table
  ```

  ![Screenshot showing command: vm list-usage](./az_vm_list_usage.png)

- Some Azure subscriptions may also have SKU restrictions that prevent deployment of specific Azure VM sizes. You can check for SKU restrictions used by ArcBox by using the below command:

  ```shell
  az vm list-skus --location <your location> --size Standard_D2s --all --output table
  az vm list-skus --location <your location> --size Standard_D4s --all --output table
  ```

  In the screenshots below, the first screenshot shows a subscription with no SKU restrictions in West US 2. The second shows a subscription with SKU restrictions on D4s_v4 in the East US 2 region. In this case, ArcBox won't be able to deploy due to the restriction.

  ![Screenshot showing command: vm list-skus with no restrictions](./list_skus_unrestricted.png)

  ![Screenshot showing command: vm list-skus with restrictions](./list_skus.png)

- Register necessary Azure resource providers by running the following commands.

  ```shell
  az provider register --namespace Microsoft.Kubernetes --wait
  az provider register --namespace Microsoft.KubernetesConfiguration --wait
  az provider register --namespace Microsoft.ExtendedLocation --wait
  az provider register --namespace Microsoft.AzureArcData --wait
  az provider register --namespace Microsoft.OperationsManagement --wait
  ```

- [Generate a new SSH key pair](https://learn.microsoft.com/azure/virtual-machines/linux/create-ssh-keys-detailed) or use an existing one (Windows 10 and above now comes with a built-in ssh client). The SSH key is used to configure secure access to the Linux virtual machines that are used to run the Kubernetes clusters.

  ```shell
  ssh-keygen -t rsa -b 4096
  ```

  To retrieve the SSH public key after it's been created, depending on your environment, use one of the below methods:
  - In Linux, use the `cat ~/.ssh/id_rsa.pub` command.
  - In Windows (CMD/PowerShell), use the SSH public key file that by default, is located in the _`C:\Users\WINUSER/.ssh/id_rsa.pub`_ folder.

  SSH public key example output:

  ```shell
  ssh-rsa o1djFhyNe5NXyYk7XVF7wOBAAABgQDO/QPJ6IZHujkGRhiI+6s1ngK8V4OK+iBAa15GRQqd7scWgQ1RUSFAAKUxHn2TJPx/Z/IU60aUVmAq/OV9w0RMrZhQkGQz8CHRXc28S156VMPxjk/gRtrVZXfoXMr86W1nRnyZdVwojy2++sqZeP/2c5GoeRbv06NfmHTHYKyXdn0lPALC6i3OLilFEnm46Wo+azmxDuxwi66RNr9iBi6WdIn/zv7tdeE34VAutmsgPMpynt1+vCgChbdZR7uxwi66RNr9iPdMR7gjx3W7dikQEo1djFhyNe5rrejrgjerggjkXyYk7XVF7wOk0t8KYdXvLlIyYyUCk1cOD2P48ArqgfRxPIwepgW78znYuwiEDss6g0qrFKBcl8vtiJE5Vog/EIZP04XpmaVKmAWNCCGFJereRKNFIl7QfSj3ZLT2ZXkXaoLoaMhA71ko6bKBuSq0G5YaMq3stCfyVVSlHs7nzhYsX6aDU6LwM/BTO1c= user@pc
  ```

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

## Deployment Option 1: Azure portal

- Click below link to deploy using Azure portal and enter values for the ARM template parameters.

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fmicrosoft%2Fazure_arc%2Fmain%2Fazure_jumpstart_arcbox%2FARM%2Fazuredeploy.json)

  ![Screenshot showing Azure portal deployment of ArcBox](./portal_deploy01.png)

  ![Screenshot showing Azure portal deployment of ArcBox](./portal_deploy02.png)

  ![Screenshot showing Azure portal deployment of ArcBox](./portal_deploy03.png)

  > **Note:** The deployment can take up to 45 minutes. If it keeps running for more than that, please check the [troubleshooting guide](#basic-troubleshooting).

## Deployment Option 2: Azure Bicep deployment via Azure CLI

- Clone the Azure Arc Jumpstart repository

  ```shell
  git clone https://github.com/microsoft/azure_arc.git
  ```

- Upgrade to latest Bicep version

  ```shell
  az bicep upgrade
  ```

- Edit the [main.bicepparam](https://github.com/microsoft/azure_arc/blob/main/azure_jumpstart_arcbox/bicep/main.bicepparam) template parameters file and supply values for your environment.
  - _`sshRSAPublicKey`_ - Your SSH public key
  - _`tenantId`_ - Your Azure tenant id
  - _`windowsAdminUsername`_ - Client Windows VM Administrator username
  - _`windowsAdminPassword`_ - Client Windows VM Password. Password must have 3 of the following: 1 lower case character, 1 upper case character, 1 number, and 1 special character. The value must be between 12 and 123 characters long
  - _`logAnalyticsWorkspaceName`_ - Name for the ArcBox Log Analytics workspace that will be created
  - _`flavor`_ - Use the value "DataOps" to specify that you want to deploy the DataOps flavor of ArcBox
  - _`deployBastion`_ - Set to _`true`_ if you want to use Azure Bastion to connect to _ArcBox-Client_
  - _`resourceTags`_ - Tags to assign for all ArcBox resources
  - _`namingPrefix`_ - The naming prefix for the nested virtual machines and all Azure resources deployed. The maximum length for the naming prefix is 7 characters,example if the value is _Contoso_: `Contoso-Win2k19`
  - _`sqlServerEdition`_ - SQL Server edition to deploy on the Hyper-V guest VM. Supported values are Developer, Standard, and Enterprise. Default is Developer edition. Azure Arc-enabled SQL Server features such as performance metrics requires Standard or Enterprise edition. Use this parameter to experience SQL Server performance metrics enabled by Azure Arc.

  ![Screenshot showing example parameters](./parameters_dataops_bicep.png)

- (optional) to use Spot VM instance for the _ArcBox Client VM_, add a parameter called _`enableAzureSpotPricing`_ set to true.

- Now you will deploy the Bicep file. Navigate to the local cloned [deployment folder](https://github.com/microsoft/azure_arc/tree/main/azure_jumpstart_arcbox/bicep) and run the below command:

```shell
az login
az group create --name "<resource-group-name>"  --location "<preferred-location>"
az deployment group create -g "<resource-group-name>" -f "main.bicep" -p "main.parameters.json" -p  customLocationRPOID="$customLocationRPOID"
```

To use a Spot instance, replace the last command with `az deployment group create -g "<resource-group-name>" -f "main.bicep" -p "main.bicepparam" -p enableAzureSpotPricing=true`

> **Note:** The deployment can take up to 45 minutes. If it keeps running for more than that, please check the [troubleshooting guide](#basic-troubleshooting).

## Start post-deployment automation

Once your deployment is complete, you can open the Azure portal and see the ArcBox resources inside your resource group. You will be using the _ArcBox-Client_ Azure virtual machine to explore various capabilities of ArcBox such as GitOps configurations and Key Vault integration. You will need to remotely access _ArcBox-Client_.

  ![Screenshot showing all deployed resources in the resource group](./deployed_resources.png)

   > **Note:** For enhanced ArcBox security posture, RDP (3389) and SSH (22) ports aren't open by default in ArcBox deployments. You will need to create a network security group (NSG) rule to allow network access to port 3389, or use [Azure Bastion](https://learn.microsoft.com/azure/bastion/bastion-overview) or [Just-in-Time (JIT)](https://learn.microsoft.com/azure/defender-for-cloud/just-in-time-access-usage?tabs=jit-config-asc%2Cjit-request-asc) access to connect to the VM.

### Connecting to the ArcBox Client virtual machine

Various options are available to connect to _ArcBox-Client_ VM, depending on the parameters you supplied during deployment.

- [RDP](#connecting-directly-with-rdp) - available after configuring access to port 3389 on the _ArcBox-NSG_, or by enabling [Just-in-Time access (JIT)](#connect-using-just-in-time-access-jit).
- [Azure Bastion](#connect-using-azure-bastion) - available if _`true`_ was the value of your _`deployBastion`_ parameter during deployment.

#### Connecting directly with RDP

By design, ArcBox doesn't open port 3389 on the network security group. Therefore, you must create an NSG rule to allow inbound 3389.

- Open the _ArcBox-NSG_ resource in Azure portal and click "Add" to add a new rule.

  ![Screenshot showing ArcBox-Client NSG with blocked RDP](./rdp_nsg_blocked.png)

  ![Screenshot showing adding a new inbound security rule](./nsg_add_rule.png)

- Specify the IP address that you will be connecting from and select RDP as the service with "Allow" set as the action. You can retrieve your public IP address by accessing [https://icanhazip.com](https://icanhazip.com) or [https://whatismyip.com](https://whatismyip.com).

  ![Screenshot showing adding a new allow RDP inbound security rule](./nsg_add_rdp_rule.png)

  ![Screenshot showing all inbound security rule](./rdp_nsg_all_rules.png)

  ![Screenshot showing connecting to the VM using RDP](./rdp_connect.png)

#### Connect using Azure Bastion

- If you have chosen to deploy Azure Bastion in your deployment, use it to connect to the VM.

  ![Screenshot showing connecting to the VM using Bastion](./bastion_connect.png)

  > **Note:** When using Azure Bastion, the desktop background image isn't visible. Therefore some screenshots in this guide may not exactly match your experience if you are connecting to _ArcBox-Client_ with Azure Bastion.

#### Connect using just-in-time access (JIT)

If you already have [Microsoft Defender for Cloud](https://learn.microsoft.com/azure/defender-for-cloud/just-in-time-access-usage?tabs=jit-config-asc%2Cjit-request-asc) enabled on your subscription and would like to use JIT to access the Client VM, use the following steps:

- In the Client VM configuration pane, enable just-in-time. This will enable the default settings.

  ![Screenshot showing the Microsoft Defender for cloud portal, allowing RDP on the client VM](./jit_allowing_rdp.png)

  ![Screenshot showing connecting to the VM using RDP](./rdp_connect.png)

  ![Screenshot showing connecting to the VM using JIT](./jit_connect_rdp.png)

#### Client VM credentials

After configuring access to the Client VM, you have to connect using the UPN format whether you are connecting using RDP or Azure Bastion.
Example:

- Username: arcdemo@jumpstart.local

  ![Screenshot showing connecting to the VM using UPN format](./domain_login.png)

  ![Screenshot showing connecting to the VM using UPN format in Bastion](./domain_login_bastion.png)

> **Note:** Logging into the Client VM without the UPN format _username@jumpstart.local_ will prevent the automation from running automatically.

#### The Logon scripts

- Once you log into the _ArcBox-Client_ VM, multiple automated scripts will open and start running. These scripts usually take up to 60 minutes to finish, and once completed, the script windows will close automatically. At this point, the deployment is complete.

  ![Screenshot showing ArcBox-Client](./automation.png)

- Deployment is complete! Let's begin exploring the features of Azure Arc-enabled data services with ArcBox for DataOps!

  ![Screenshot showing complete deployment](./arcbox_complete.png)

- Before you move on, make sure to verify that the deployment status shown on the desktop background doesn't indicate any failures. If so, inspect the log files in the ArcBox logs-directory by navigating to the desktop shortcut _Logs_. For more information about troubleshooting, please check the [troubleshooting guide](#basic-troubleshooting)

  ![Screenshot showing ArcBox resources in Azure portal](./rg_arc.png)

## Using ArcBox

After deployment is complete, it's time to start exploring ArcBox. Most interactions with ArcBox will take place either from Azure itself (Azure portal, CLI, or similar) or from inside the _ArcBox-Client_ virtual machine using Azure Data Studio or SQL Server Management Studio. When establishing a remote connection into the VM, here are some things to try:

### Azure Arc-enabled SQL Managed Instance stress simulation

Included in ArcBox, is a dedicated SQL stress simulation tool named SqlQueryStress automatically installed for you on the Client VM. SqlQueryStress will allow you to generate load on the Azure Arc-enabled SQL Managed Instance that can be done used to showcase how the SQL database and services are performing as well to highlight operational practices described in the next section.

- To start with, open the SqlQueryStress desktop shortcut and connect to the K3s SQL Managed Instance primary endpoint IP address. This can be found in the _SQLMI Endpoints_ text file desktop shortcut that was created for you. Or you can get the primary endpoint from the Azure portal.

  ![Screenshot showing SQL Stress application](./sql_stress_start.png)

  ![Screenshot showing SQL Managed Instance endpoints file](./sqlmi-endpoint_file.png)

  ![Screenshot showing SQL Managed Instance endpoints in the Azure portal](./sqlmi_connection_portal.png)

- To connect, use "Integrated Authentication" and select the deployed sample AdventureWorks database (you can use the "Test" button to check the connection).

  ![Screenshot showing SQL Managed Instance connection](./sql_stress_connection.png)

- To generate some load, we will be running a simple stored procedure. Copy the below procedure and change the number of iterations you want it to run as well as the number of threads to generate even more load on the database. In addition, change the delay between queries to 1ms for allowing the stored procedure to run for a while. Click on Go to start generating load.

  ```sql
  exec [dbo].[uspGetEmployeeManagers] @BusinessEntityID = 8
  ```

- As you can see from the example below, the configuration settings are 100,000 iterations, five threads per iteration, and a 1ms delay between queries. These configurations should allow you to have the stress test running for a while.

  ![Screenshot showing SQL stress stored procedure](./sql_stress_sp.png)

  ![Screenshot showing SQL stress running](./sql_stress_running.png)

### Azure Arc-enabled SQL Managed Instance monitoring using Grafana

When deploying Azure Arc-enabled SQL Managed Instance, a [Grafana](https://grafana.com/) instance is also automatically deployed on the same Kubernetes cluster and include built-in dashboards for both Kubernetes infrastructure as well SQL Managed Instance monitoring.

- Now that you have the SqlQueryStress stored procedure running and generating load, we can look how this is shown in the built-in Grafana dashboard. As part of the automation, a new URL desktop shortcut simply named "Grafana" was created.

  ![Screenshot showing Grafana desktop shortcut](./grafana_icon.png)

- [Optional] The IP address for this instance represents the Kubernetes LoadBalancer external IP that was provision as part of Azure Arc-enabled data services. Use the _kubectl get svc -n arc_ command to view the _metricsui_ external service IP address.

  ![Screenshot showing Grafana IP address](./grafana_ip_address.png)

- To log in, use the same username and password that's in the SQLMI Endpoints text file desktop shortcut

  ![Screenshot showing Grafana login page](./grafana_login_page.png)

- Navigate to the built-in "SQL Managed Instance Metrics" dashboard.

  ![Screenshot showing Grafana metrics page](./grafana_metrics_dashboard.png)

  ![Screenshot showing Grafana metrics page](./grafana_sql_mi_metrics.png)

- Change the dashboard time range to "Last 5 minutes" and re-run the stress test using SqlQueryStress (in case it was already finished).

  ![Screenshot showing changing time frame to last 5 minutes in Grafana dashboard](./grafana_time_range.png)

- You can now see how the SQL graphs are starting to show increased activity and load on the database instance.

  ![Screenshot showing changing increased CPU and memory activity in Grafana dashboard](./grafana_increased_activity.png)

  ![Screenshot showing changing increased database activity in Grafana dashboard](./grafana_database_activity.png)

### Application

ArcBox deploys bookstore application on the _ArcBox-K3s-Data_ workload cluster.

- Click on the _Bookstore_ icon on the desktop to open _Bookstore_ application.

  ![Screenshot showing bookstore icon](./bookstore01.png)

  ![Screenshot showing bookstore app](./bookstore02.png)

- The App creates a new Database _demo_ and inserts 4 records. Click on the books tab to review the records.

  ![Screenshot showing bookstore app records](./bookstore03.png)

- Open _Azure Data Studio_ and query the _demo_ DB to review the records inserted in the database.

  ![Screenshot showing Azure Data Studio](./bookstore04.png)

  ![Screenshot showing Azure Data Studio records](./bookstore05.png)

  ![Screenshot showing Azure Data Studio records query](./bookstore06.png)

- ArcBox deploys the Bookstore application's service, and creates a DNS record to resolve to K3s cluster Ingress IP. Open PowerShell and run below commands to validate.

  ```shell
  kubectx k3s
  kubectl --namespace arc get svc
  nslookup jumpstartbooks.jumpstart.local
  ```

  ![Screenshot showing bookstore app DNS record](./bookstore07.png)

### High availability

When deploying Azure Arc-enabled SQL Managed Instance in the Business Critical tier, up to three SQL pods replicas will be deployed to assemble an availability group. The availability group includes three Kubernetes replicas with a primary instance and two secondary instances that can be configured to be readable secondaries. This availability groups managed the failover process to achieve high availability.

  ![Screenshot showing SQL Managed Instance pods](./bookstore08.png)

- Right click and run the _DataOpsTestAppScript.ps1_ script placed under _C:\ArcBox\DataOps_. The script will deploy the DB Connection App.

  ![Screenshot showing DB Connection App script](./bookstore09.png)

- DB Connection App connects to the primary SQL Managed Instance and inserts new book every second, and logs information of server it's connected to. Open PowerShell and run the below commands and follow the logs.

  ```shell
  $pod=kubectl --namespace arc get pods --selector=app=dbconnecttest --output="jsonpath={.items..metadata.name}"
  kubectl --namespace arc logs $pod -f
  ```

  ![Screenshot showing DB Connection App logs 01](./bookstore10.png)

  ![Screenshot showing DB Connection App logs 02](./bookstore11.png)

- To test failover between the replicas, we will simulate a "crash" that will trigger an HA event and will force one of the secondary replicas to get promoted to a primary replica. Open two side-by-side PowerShell sessions. On the left side session review the deployed pods. The right-side session will be used to follow the DB Connection App logs. Delete the Primary replica by running below commands.

  ```shell
  kubectl --namespace arc get pods
  kubectl --namespace arc delete pod k3s-sql-0
  ```

- On the right-side session, you can see some failures once the pod is deleted simulating a primary replica crash. In that time one of the secondary replicas is being promoted to secondary to start receiving requests from the application.

  ![Screenshot showing SQL Managed Instance failover 01](./bookstore12.png)

- It might take a few minutes for the availability group to return to an healthy state. The secondary replica and _k3s-sql-1_ was promoted to primary and DB Connection App is able to insert new records in the database.

  ![Screenshot showing SQL Managed Instance failover 02](./bookstore13.png)

- Open _Azure Data Studio_ and query the _demo_ DB to review the records inserted in the database. Also,review the data inserted in App browser.

  ![Screenshot showing bookstore app DB records](./bookstore14.png)

  ![Screenshot showing bookstore app](./bookstore15.png)

### Point-in-time restore

Arc-enabled SQL Managed Instance is deployed as part of ArcBox deployment. By default [automatic backups](https://learn.microsoft.com/azure/azure-arc/data/point-in-time-restore#automatic-backups) of the databases are enabled in Arc-enabled SQL Managed Instances. Full backup is performed when a new database is created or restored and subsequent full backups are performed weekly. Differential backups are taken every 12 hours and transaction log backups every 5 minutes. Default retention period of these backups is 7 days and is [configurable](https://learn.microsoft.com/azure/azure-arc/data/point-in-time-restore#configure-retention-period).

This section provides instructions on how to perform point in time restore from the automatic backups available in Arc-enabled SQL Managed Instance to recover lost or corrupted data.

To view backups of full, differential, and transaction logs wait for more than 12 hours after deploying the ArcBox DataOps flavor. Once these backups are available follow instructions below to perform a point in time restore of database. If you would like to test this feature immediately, you can simply use the latest backup set when restoring.

- Once you login to the _ArcBox-Client_ VM using RDP or bastion host, locate Azure Data Studio icon on the desktop and open.

  ![Open Azure Data Studio](./sqlmi-pitr-azdatastudio.png)

- Click on _ArcBoxDAG_ to connect to the **k3s-sql** Arc-enabled SQL Managed Instance and view databases. Right click and select **Manage** to view databases. Alternatively you can expand _ArcBoxDAG_ connection to view databases.

  ![View Arc-enabled SQL Managed Instance databases](./sqlmi-pitr-databases.png)

- In order to restore database you need to find the last well known backup copy that you would like to restore. You can list all the available backups by running the following SQL query in **msdb** database.

  ```sql
  SELECT TOP (1000) [backup_set_id]
        ,[database_name]
        ,[backup_start_date]
        ,[backup_finish_date]
        ,[type]
        ,[backup_size]
        ,[server_name]
        ,[machine_name]
        ,[last_valid_restore_time]
    FROM [msdb].[dbo].[backupset]
    WHERE database_name = 'AdventureWorks2019'
  ```

- Run this query in Azure Data Studio to display available backups. Right click **msdb**, select New Query and copy paste above query in the query editor and click Run.

  ![View Arc-enabled SQL Managed Instance databases](./sqlmi-pitr-backuplist.png)

- Identify the backup set that you would like to restore and make note of the **backup_finish_date** value to use in the restore step. Modify the date format as **2022-09-20T23:14:13.000000Z**

- Connect to the Arc Data Controller to restore database using Azure Data Studio. Click on the Connect controller button under Azure Arc Controllers to connecting to an existing data controller.

  ![Connect to Azure Arc Data Controller](./sqlmi-pitr-connect-datacontroller.png)

- Specify **arc** as the namespace, leave the default values (leave **Name** as empty) and click on Connect

  ![Connect to Azure Arc Data Controller details](./sqlmi-pitr-connect-datacontroller-details.png)

- Once connection is successful, expand Azure Arc Controllers, expand _arcbox-k3s-data-xxxx-dc_ to view Arc-enabled SQL Managed Instance

   ![Azure Arc Data Controller](./sqlmi-pitr-datacontroller.png)

- Right-click on the _k3s-sql_ Arc-enabled SQL Managed Instance and select Manage.

  ![Azure Arc Data Controller Manage SQL Managed Instance](./sqlmi-pitr-connect-datacontroller-manage.png)

- Click on "Connect to Server" and enter database username and password to connect to the SQL Managed Instance to view the databases. It can take about a minute to start populating the databases.

  ![Azure Arc Data Controller Manage SQL Managed Instance](./sqlmi-pitr-connect-to-sqlmi.png)

- Click on "Backups" to view databases and available backups to restore

  ![Azure Arc-enabled SQL Managed Instance databases](./sqlmi-pitr-database-list.png)

- Click on the "Restore" link as shown below to restore the _AdventureWorks2019_ database.

  ![Azure Arc-enabled SQL Managed InstanceI database restore](./sqlmi-pitr-database-select-restore.png)

- Specify target database name to restore and backup set `datetime` that's noted down in the previous steps and click on Restore.

  ![Azure Arc-enabled SQL Managed Instance target database restore](./sqlmi-pitr-targetdb.png)

- Wait until database restore operation is complete and refresh the _ArcBoxDAG_ connection to refresh and view restored database.

  ![Azure Arc-enabled SQL Managed Instance restored database](./sqlmi-pitr-restored-database.png)

### Disaster Recovery

The _ArcBox-K3s-Data-xxxx_ and the _ArcBox-AKS-DR-Data-xxxx_ clusters are deployed into a distributed availability group to simulate two different sites. Use the `az sql instance-failover-group-arc` command to initiate a failover from the primary SQL instance to the secondary DR instance.

- Open PowerShell and run below commands to initiate the failover.

  ```shell
  kubectx k3s
  az sql instance-failover-group-arc update --name primarycr --role secondary --k8s-namespace arc --use-k8s
  ```

  ![Screenshot showing bookstore app](./aksdr_bookstore01.png)

- Right click and run the _DataOpsAppDRScript.ps1_ script placed under _C:\ArcBox\DataOps_ to deploy the Bookstore application on the DR cluster to simulate application failover.

  ![Screenshot showing bookstore app](./aksdr_bookstore02.png)

- The DR script deploys the Bookstore app service, creates the Ingress and creates a DNS record to resolve to AKS DR cluster Ingress IP. Open PowerShell and run below commands to validate.

  ```shell
  kubectx aks-dr
  kubectl --namespace arc get ingress
  nslookup dataops.jumpstart.local
  ```

  ![Screenshot showing bookstore app records](./aksdr_bookstore03.png)

- Now that we perform a successful failover, we can re-validate and make sure replication still works as expected.

  ![Screenshot showing bookstore app records](./aksdr_bookstore04.png)

### Additional optional scenarios on the _ArcBox-AKS-Data-xxxx_ cluster

#### Migration to Azure Arc-enabled SQL Managed Instance

As part of ArcBox, a SQL Server is deployed in a nested VM on the Client VM to allow you to test migrating a database to Azure Arc-enabled SQL Managed Instance.

- To connect to the nested SQL Server instance, you can find the connection details in the Azure Data Studio.

  ![Screenshot showing the nested SQL Server in Azure Data Studio](./sql_server_azure_data_studio.png)

  ![Screenshot showing the nested SQL Server connection in Azure Data Studio](./sql_server_azure_data_studio_connection.png)

- You can also connect using Microsoft SQL Server Management Studio (SSMS).

  ![Screenshot showing Microsoft SQL Server Management Studio (SSMS)](./ssms_start.png)

- Connect to the AKS primary SQL Managed Instance's endpoint IP address. This can be found in the _SQLMI Endpoints_ text file desktop shortcut and select the authentication to be _Windows Authentication_.

  ![Screenshot showing connection details of the AKS SQL Managed Instance in the endpoints file](./ssms_aks_endpoints_file.png)

  ![Screenshot showing connection to AKS SQL Managed Instance using Microsoft SQL Server Management Studio (SSMS)](./ssms_aks_connection.png)

- Connect also to the nested SQL server using the details you got from Azure Data Studio. Use the password you entered when provisioning ArcBox.

  ![Screenshot showing opening a new connection on the SQL server using Microsoft SQL Server Management Studio (SSMS)](./ssms_connect.png)

  ![Screenshot showing connection to the nested SQL server using Microsoft SQL Server Management Studio (SSMS)](./ssms_nested_sql.png)

- You can see that _AdventureWorks_ database is only available in the nested SQL Server.

  ![Screenshot showing the databases view for both servers in the Microsoft SQL Server Management Studio (SSMS)](./ssms_db_comparison.png)

- Expand the nested SQL Server instance and navigate to the AdventureWorks database and execute the following query, use the same username and password as the previous step.

  ```sql
  BACKUP DATABASE AdventureWorksLT2019
  TO DISK = 'C:\temp\AdventureWorksLT2019.bak'
  WITH FORMAT, MEDIANAME = 'AdventureWorksLT2019' ;
  GO
  ```

  ![Screenshot showing a new in the Microsoft SQL Server Management Studio (SSMS)](./ssms_new_query.png)

  ![Screenshot showing running a backup query in the Microsoft SQL Server Management Studio (SSMS)](./ssms_db_backup_complete.png)

- To migrate the backup created to the Arc-enabled SQL Managed Instance, open a new PowerShell session and use the following PowerShell snippet to:
  - Copy the created backup to the client VM from the nested SQL Server instance
  - Copy the backup to the Azure Arc-enabled SQL Managed Instance pod
Initiate the backup restore process

  ```powershell
  Set-Location -Path c:\temp
  #Connecting to the nested Windows Server VM
  $nestedWindowsUsername = "Administrator"
  $nestedWindowsPassword = "JS123!!"
  $secWindowsPassword = ConvertTo-SecureString $nestedWindowsPassword -AsPlainText -Force
  $winCreds = New-Object System.Management.Automation.PSCredential ($nestedWindowsUsername, $secWindowsPassword)
  $session = New-PSSession -VMName ArcBox-SQL -Credential $winCreds
  #Copying the database backup to the Client VM
  Copy-Item -FromSession $session -Path C:\temp\AdventureWorksLT2019.bak -Destination C:\Temp\AdventureWorksLT2019.bak
  #Copying the database to the AKS SQL Managed Instance
  kubectx aks
  kubectl cp ./AdventureWorksLT2019.bak aks-sql-0:var/opt/mssql/data/AdventureWorksLT2019.bak -n arc -c arc-sqlmi
  #Initiating restore on the AKS SQL Managed Instance
  kubectl exec aks-sql-0 -n arc -c arc-sqlmi -- /opt/mssql-tools/bin/sqlcmd -S localhost -U $Env:AZDATA_USERNAME -P $Env:AZDATA_PASSWORD -Q "RESTORE DATABASE AdventureWorksLT2019 FROM  DISK = N'/var/opt/mssql/data/AdventureWorksLT2019.bak' WITH MOVE 'AdventureWorksLT2012_Data' TO '/var/opt/mssql/data/AdventureWorksLT2012.mdf', MOVE 'AdventureWorksLT2012_Log' TO     '/var/opt/mssql/data/AdventureWorksLT2012_log.ldf'"
  ```

  ![Screenshot showing a PowerShell command to copy and restore the database backup to SQL Managed Instance](./powershell_db_restore.png)

- Navigate to the Azure Arc-enabled SQL Managed Instance in the Microsoft SQL Server Management Studio (SSMS) and you can see that the _AdventureWorks_ database has been restored successfully.

  ![Screenshot showing the restored DB on SQL Managed Instance](./ssms_db_restore_complete.png)

### ArcBox Azure Monitor workbook

Open the [ArcBox Azure Monitor workbook documentation](/azure_jumpstart_arcbox/workbook/flavors/DataOps) and explore the visualizations and reports of hybrid cloud resources.

  ![Screenshot showing Azure Monitor workbook usage](./workbook.png)

### Arc-enabled SQL Server - Best practices assessment

As part of the ArcBox deployment, SQL Server best practices assessment is configured and run. Open _ArcBox-SQL_ Arc-enabled SQL Server resource from the resource group deployed or Azure Arc service blade to view SQL Server best practice assessment results.

- The following screenshot shows the SQL Server best practices assessment page and the scheduled and previously ran assessments. If this page doesn't show assessment results click on the Refresh button to show assessments. Once displayed the assessments and results click on _View assessment_ results to see results.

  ![Screenshot showing SQL Server best practices assessment configuration](./sql-pba-view-results.png)

  ![Screenshot showing SQL Server best practices assessment results part 1](./sql-bpa-results-1.png)

  ![Screenshot showing SQL Server best practices assessment results part 2](./sql-bpa-results-2.png)

### SQL Server migration assessment

Once you connect SQL Server running in on-premises or other cloud environment it's ready to support  running migration assessment to review migration readiness to Microsoft Azure cloud. Arc-enabled [SQL Server migration assessment](https://learn.microsoft.com/sql/sql-server/azure-arc/migration-assessment?view=sql-server-ver16) greatly simplifies migration assessment by eliminating any additional infrastructure to run SQL Server discovery and assessment tools.

As part of the ArcBox DataOps deployment on-demand SQL Server migration assessment is ran show case the SQL Server migration readiness, which includes server level and database level compatibilities to migrate to different target SQL Servers such as Azure SQL Server, SQL Server Managed Instance, and SQL Server on Azure VMs.

Follow the steps below to review migration readiness of the ArcBox-SQL server running on the ArcBox-Client as a guest VM.

- Navigate to the resource group overview page in Azure Portal.

- Locate ArcBox-SQL Arc-enabled SQL Server resources and open resource details view.

  ![Screenshot showing Arc-enabled SQL Server overview](./sql-server-migration-overview.png)

- Click on Migration in left navigation to view migration assessment results.

> **Note:** It may take sometime to complete SQL Server migration assessment and show results. If you don't see SQL Server migration assessment results, please wait and revisit this section later.

  ![Screenshot showing Arc-enabled SQL Server migration assessment](./sql-server-migration-assessment.png)

- Review migration readiness of the SQL server. For detailed information on readiness review refer product documentation [here](https://learn.microsoft.com/sql/sql-server/azure-arc/migration-assessment?view=sql-server-ver16#review-readiness).

  ![Screenshot showing Arc-enabled SQL Server migration readiness](./sql-server-migration-readines.png)

- Review migration readiness to migrate to Azure SQL Managed Instance.

  ![Screenshot showing Arc-enabled SQL Server migration readiness not ready to SQL MI](./sql-server-migration-readines-not-ready.png)

- Review migration readiness to migrate to SQL Server on Virtual Machines.

  ![Screenshot showing Arc-enabled SQL Server migration readiness ready to migrate to SQL Server on VM](./sql-server-migration-readines-ready.png)

### Microsoft Defender for Cloud - SQL server on machines

This section guides you through different settings for enabling Microsoft Defender for Cloud for SQL server on machines. Follow the steps below to use Defender for Cloud - SQL servers on machines.

- Open Microsoft Defender for Cloud, go to environments settings, select subscription where the ArcBox is deployed.

  ![Screenshot showing email notification settings](./sql-defender-environment-settings.png)

- Select options shown below and specify email address to receive notifications and save changes.

  ![Screenshot showing email notification settings](./sql-defender-email-settings.png)

- Locate _ArcBox-SQL_ Arc-enabled SQL Server resource in the resource group deployed.

- Click on the Microsoft Defender for Cloud in the left navigation and review the current status of the Microsoft Defender for SQL server on machines.

  ![Screenshot showing Microsoft Defender for SQL server on machines status](./sql-defender-status.png)

- Click on _Enable_ button shown in the image above to enable Defender for Cloud on the Arc-enabled SQL Server.

> **Note:** Status might differ depending on if the Microsoft Defender for SQL server on machines is already enabled at subscription level.

- The below screenshot shows the test script used to generate SQL threats, detect, and alert using Defender for Cloud for SQL servers. This script is copied on the nested _ArcBox-SQL_ Hyper-V virtual machine and can be used to run additional tests to generate security incidents and alerts.

  ![Screenshot showing Defender for SQL test scripts](./sql-defender-testing-script.png)

- Logon to the _ArcBox-SQL_ Hyper-V virtual machine, open PowerShell window, and change the directory to _C:\ArcBox\agentScript_ folder and run _testDefenderForSQL.ps1_.

- Run the PowerShell script to generate Defender for SQL incidents and alerts.

  ![Screenshot showing manual execution of the test scripts](./manual-brute-force-test.png)

- The below screenshot shows the SQL threats detected by Microsoft Defender for Cloud.

  ![Screenshot showing Defender for SQL security incidents and alerts](./sql-defender-incidents.png)

- Microsoft Defender for Cloud generates an email and sends it to the registered email for alerts. The below screenshot shows an email alert sent by Defender for Cloud when a SQL threat is detected. By default, this email is sent to the registered contact email at the subscription level.
  
  ![Screenshot showing Defender for SQL security incidents and alerts](./sql-defender-brute-force-attack-alert.png)

### Arc-enabled SQL Server - least privilege access

As part of least privilege security best practice principle, [Arc-enabled SQL server supports running agent extension under least privilege access](https://learn.microsoft.com/sql/sql-server/azure-arc/configure-least-privilege?view=sql-server-ver16). By default SQL server agent extension runs under Local System account. After enabling the least privilege access, agent extension runs under _NT Service\SQLServerExtension_. Refer [permissions required and assigned to _NT Service\SQLServerExtension_ service account](https://learn.microsoft.com/sql/sql-server/azure-arc/configure-windows-accounts-agent?view=sql-server-ver16) for more details.

- Screenshot below shows Arc-enabled SQL server extension service running under _NT Service\SQLServerExtension_ service account.

![Screenshot showing Arc-enabled SQL server agent extension running under least privileged access](./sql-server-least-privileged-access.png)

- To view the status of Arc-enabled SQL server agent extension service, logon to the _ArcBox-SQL_ Hyper-V virtual machine, open Windows services from Control Panel -> System and Security -> Administrative Tools.

![Screenshot showing ArcBox-SQL Hyper-V guest VM](./arcbox-sql-hyperv-guest.png)

### Arc-enabled SQL Server - automated backups and restore

#### Automated backups

[Arc-enabled SQL Server supports automated backups](https://learn.microsoft.com/sql/sql-server/azure-arc/backup-local?view=sql-server-ver16&tabs=azure) to recover data during the disaster recovery process or when customers would like to go back to certain restore point. ArcBox deployment is now enabled to perform scheduled backups at instance level to take full database backup every 7 days,  differential backup every 12 hours, and log backup every 5 minutes to support lowest RPO. These schedules are customizable, refer documentation [here](https://learn.microsoft.com/sql/sql-server/azure-arc/backup-local?view=sql-server-ver16&tabs=azure#backup-frequency-and-retention-days) for more details. These backups can be configured at database server instance level or individual database level based on the recovery needs.

- Screenshot below shows automated backup schedule configured in ArcBox-SQL Arc-enabled SQL Server at the instance level.

![Screenshot showing ArcBox-SQL automated backup schedule](./sql-server-automated-backups.png)

- Screenshot below shows automated backup schedule inherited from the instance level backup policy.

![Screenshot showing ArcBox-SQL automated backup schedule inherited from instance](./sql-server-automated-backups-database.png)

#### Restore database

Once the SQL Server backups are enabled and have the backups available to restore from certain restore points, customers can restore database to a new database from the specific restore point that would like to restore data from.

- Screenshot below shows earliest available restore points to restore database from. Click on the _Restore_ link restore _AdventurWorksLT2022_ database from one of the restore point.

![Screenshot showing ArcBox-SQL backup earliest restore points](./sql-server-backups-restore-points.png)

- Screenshot below shows available restore points for _AdventurWorksLT2022_ database. To restore this database 1) Select available restore point, 2) Specify new database name, and 3) Click on Create to restore database to the desired restore points.

![Screenshot showing _AdventurWorksLT2022_ database restore points](./sql-server-backups-restore-db.png)

- Review final details and click Review + Create to start restoring the database.

![Screenshot showing _AdventurWorksLT2022_ database restore confirmation](./sql-server-backups-confirim-restore-db.png)

- Once the database restore request is submitted, review restore status in the Azure Portal as shown in the screenshot below. Notice new database is created on the _ArcBox-SQL_ database server.

![Screenshot showing _AdventurWorksLT2022_ database restore status](./sql-server-backups-restore-db-status.png)

- You can also verify restored database on the ArcBox-SQL guest VM as shown in the screenshot below.

![Screenshot showing restored database on the SQL server guest VM](./sql-server-backups-restore-db-status-guestvm.png)

### Monitor SQL Server enabled by Azure Arc

Arc-enabled SQL Server now supports [monitoring using the performance dashboards](https://learn.microsoft.com/sql/sql-server/azure-arc/sql-monitoring?view=sql-server-ver16) in Azure Portal. Performance dashboard feature is supported only on SQL Server Standard and Enterprise editions. ArcBox deployment now supports deploying SQL Server Standard and Enterprise editions. Choose the correct edition based on the requirement to experience performance dashboards. Refer deployment parameters documented in this document to select desired SQL Server edition using the parameter _sqlServerEdition_.

- To view performance dashboards in Arc-enabled SQL Server, go to the resource group deployed in the Azure Portal, locate ArcBox-SQL Arc-enabled SQL server and open resource details.

- Click on _Performance Dashboard_ under Monitoring section as shown below to view performance dashboard.

![Screenshot showing SQL server performance dashboard](./sql-server-navigate-performance-dashboard.png)

- Screenshot below shows SQL Server performance dashboard enabled by Azure Arc.

![Screenshot showing SQL server performance dashboard](./sql-server-open-performance-dashboard.png)

### Included tools

The following tools are including on the _ArcBox-Client_ VM.

- Azure CLI
- Azure PowerShell
- Git
- PowerShell 7
- Visual Studio Code
- Windows Terminal
- WinGet
- kubectl, kubectx, helm
- Microsoft SQL Server Management Studio
- Azure Data Studio
- SQL StressTest application
- Putty
- ZoomIt

### Next steps

ArcBox is a sandbox that can be used for a large variety of use cases, such as an environment for testing and training or a kickstarter for proof of concept projects. Ultimately, you are free to do whatever you wish with ArcBox. Some suggested next steps for you to try in your ArcBox are:

- Use the included kubectx to switch contexts between the three Kubernetes clusters
- Explore the different visualizations in Grafana
- Scale the SQL Managed Instance's cores and memory up and down
- Test failover and fallback  scenarios to and from the DR instance

## Clean up the deployment

To clean up your deployment, simply delete the resource group using Azure CLI or Azure portal.

```shell
az group delete -n <name of your resource group>
```

![Screenshot showing group delete from Azure portal](./portal_delete.png)

## Basic troubleshooting

Occasionally deployments of ArcBox may fail at various stages. Common reasons for failed deployments include:

- Automation scripts don't start after login - this is usually caused by logging into the client VM with wrong format of the username. Login needs to be done using domain credentials in UPN format _username@jumpstart.local_.
- "User disabled" error message appears when you try to RDP or connect using Bastion to the Client VM - this is caused by logging into the client VM with wrong format of the username. Login needs to be done using domain credentials in UPN format _username@jumpstart.local_.
- Invalid SSH public key provided in _azuredeploy.parameters.json_ file.
  - An example SSH public key is shown here. Note that the public key includes "ssh-rsa" at the beginning. The entire value should be included in your _azuredeploy.parameters.json_ file.

      ![Screenshot showing SSH public key example](./ssh_example.png)

- Not enough vCPU quota available in your target Azure region - check vCPU quota and ensure you have at least 98 available. See the [prerequisites](#prerequisites) section for more details.
- The selected Azure region doesn't support all the necessary services. Ensure you are deploying ArcBox in one of the supported regions listed in the "ArcBox Azure Region Compatibility" section above.

### Exploring logs from the _ArcBox-Client_ virtual machine

Occasionally, you may need to review log output from scripts that run on the _ArcBox-Client_ and the _ArcBox-K3s-Data-xxxx_ virtual machines in case of deployment failures. To make troubleshooting easier, the ArcBox deployment scripts collect all relevant logs in the _C:\ArcBox\Logs_ folder on _ArcBox-Client_. A short description of the logs and their purpose can be seen in the list below:

| Log file | Description |
| ------- | ----------- |
| _C:\ArcBox\Logs\Bootstrap.log_ | Output from the initial bootstrapping script that runs on _ArcBox-Client_. |
| _C:\ArcBox\Logs\DataOpsLogonScript.log_ | Output of _DataOpsLogonScript.ps1_ which configures the Hyper-V host and guests and onboards the guests as Azure Arc-enabled servers. |
| _C:\ArcBox\Logs\installK3s.log_ | Output from the custom script extension which runs on _ArcBox-K3s-MGMT_ and configures the Cluster API for Azure cluster and onboards it as an Azure Arc-enabled Kubernetes cluster. If you encounter ARM deployment issues with _ubuntuK3s.json_ then review this log. |
| _C:\ArcBox\Logs\MonitorWorkbookLogonScript.log_ | Output from _MonitorWorkbookLogonScript.ps1_ which deploys the Azure Monitor workbook. |
|_C:\ArcBox\Logs\DeploySQLMIADAuth.log_ | Output from the _DeploySQLMIADAuth.ps1_ script which deploys the AD connector and the Arc-enabled SQL Managed Instances|
| _C:\ArcBox\Logs\DataOpsAppScript.log_ | Output from the _DataOpsAppScript.ps1_ script which deploys the book store application |
| _C:\ArcBox\Logs\NestedSqlLogonScript.log_ | Output from the ArcServersLogonScript deployment |
| _C:\ArcBox\Logs\DataController-k3s.log_ | Output from the K3s cluster's Data Controller deployment |
| _C:\ArcBox\Logs\DataController-aks.log_ | Output from the AKS cluster's Data Controller deployment |
| _C:\ArcBox\Logs\DataController-aks-dr.log_ | Output from the AKS DR cluster's Data Controller deployment |
| _C:\ArcBox\Logs\DataController-sqlmi-k3s.log_ | Output from the K3s cluster's Arc SQL Managed Instance deployment |
| _C:\ArcBox\Logs\DataController-sqlmi-aks.log_ | Output from the AKS cluster's Arc SQL Managed Instance deployment |
| _C:\ArcBox\Logs\DataController-sqlmi-aks-dr.log_ | Output from the AKS DR cluster's Arc SQL Managed Instance deployment |
| _C:\ArcBox\Logs\WinGet-provisioning-*.log_ | Output from WinGet.ps1 which installs WinGet and applies WinGet Configuration. |

  ![Screenshot showing ArcBox logs folder on ArcBox-Client](./troubleshoot_logs.png)

### Exploring installation logs from the Linux virtual machines

In the case of a failed deployment, pointing to a failure in the _ubuntuK3sDeployment_ Azure deployment, an easy way to explore the deployment logs is available directly from the associated virtual machine.

- Connect using SSH to the associated virtual machine public IP:
  - _ubuntuK3sDeployment_ - _ArcBox-K3s-MGMT_ virtual machine.

    ![Screenshot showing ArcBox-K3s-Data virtual machine public IP](./arcbox_k3s_data_vm_ip.png)

    > **Note:** Port 22 isn't open by default in ArcBox deployments. You will need to [create an NSG rule](#connecting-directly-with-rdp) to allow network access to port 22, or use Azure Bastion or JIT to connect to the VM.

- As described in the message of the day (motd), depending on which virtual machine you logged into, the installation log can be found in the _jumpstart_logs_ folder. This installation logs can help determine the root cause for the failed deployment.
  - _ArcBox-K3s-MGMT_ log path: _jumpstart_logs/installK3s.log_

      ![Screenshot showing login and the message of the day](./login_motd.png)

- You might randomly get a similar error in the _InstallK3s.log_ to `Error from server (InternalError): error when creating "template.yaml": Internal error occurred: failed calling webhook "default.azuremachinetemplate.infrastructure.cluster.x-k8s.io": failed to call webhook: Post "https://capz-webhook-service.capz-system.svc:443/mutate-infrastructure-cluster-x-k8s-io-v1beta1-azuremachinetemplate?timeout=10s": EOF` - this is an issue we're currently investigating. To resolve please redeploy ArcBox.

If you are still having issues deploying ArcBox, please [submit an issue](https://aka.ms/JumpstartIssue) on GitHub and include a detailed description of your issue, the Azure region you are deploying to, the flavor of ArcBox you are trying to deploy. Inside the _C:\ArcBox\Logs_ folder you can also find instructions for uploading your logs to an Azure storage account for review by the Jumpstart team.
