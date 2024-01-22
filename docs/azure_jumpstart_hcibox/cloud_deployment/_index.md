---
type: docs
linkTitle: "Cloud Deployment"
isGettingStarted: false
weight: 2
---

## Start post-deployment automation

Once your deployment is complete, you can open the Azure portal and see the initial HCIBox resources inside your resource group. Now you must remote into the _HCIBox-Client_ VM to continue the next phase of the deployment.

  ![Screenshot showing all deployed resources in the resource group](./deployed_resources.png)

   > **Note:** For enhanced HCIBox security posture, RDP (3389) and SSH (22) ports are not open by default in HCIBox deployments. You will need to create a network security group (NSG) rule to allow network access to port 3389, or use [Azure Bastion](https://learn.microsoft.com/azure/bastion/bastion-overview) or [Just-in-Time (JIT)](https://learn.microsoft.com/azure/defender-for-cloud/just-in-time-access-usage?tabs=jit-config-asc%2Cjit-request-asc) access to connect to the VM.

### Connecting to the HCIBox Client virtual machine

Various options are available to connect to _HCIBox-Client_ VM, depending on the parameters you supplied during deployment.

- [RDP](#connecting-directly-with-rdp) - available after configuring access to port 3389 on the _Arc-App-Client-NSG_, or by enabling [Just-in-Time access (JIT)](#connect-using-just-in-time-access-jit).
- [Azure Bastion](#connect-using-azure-bastion) - available if *`true`* was the value of your _`deployBastion`_ parameter during deployment.

#### Connecting directly with RDP

By design, HCIBox does not open port 3389 on the network security group. Therefore, you must create an NSG rule to allow inbound 3389.

  > **Note:** If you deployed with Azure Developer CLI then this step is automatically done for you as part of the automation.

- Open the _HCIBox-NSG_ resource in Azure portal and click "Add" to add a new rule.

  ![Screenshot showing HCIBox-Client NSG with blocked RDP](./rdp_nsg_blocked.png)

  ![Screenshot showing adding a new inbound security rule](./nsg_add_rule.png)

- Specify the IP address that you will be connecting from and select RDP as the service with "Allow" set as the action. You can retrieve your public IP address by accessing [https://icanhazip.com](https://icanhazip.com) or [https://whatismyip.com](https://whatismyip.com).

  <img src="./nsg_add_rdp_rule.png" alt="Screenshot showing adding a new allow RDP inbound security rule" width="400">

  ![Screenshot showing all inbound security rule](./rdp_nsg_all_rules.png)

  ![Screenshot showing connecting to the VM using RDP](./rdp_connect.png)

#### Connect using Azure Bastion

- If you have chosen to deploy Azure Bastion in your deployment, use it to connect to the VM.

  ![Screenshot showing connecting to the VM using Bastion](./bastion_connect.png)

  > **Note:** When using Azure Bastion, the desktop background image is not visible. Therefore some screenshots in this guide may not exactly match your experience if you are connecting to _HCIBox-Client_ with Azure Bastion.

#### Connect using just-in-time access (JIT)

If you already have [Microsoft Defender for Cloud](https://learn.microsoft.com/azure/defender-for-cloud/just-in-time-access-usage?tabs=jit-config-asc%2Cjit-request-asc) enabled on your subscription and would like to use JIT to access the Client VM, use the following steps:

- In the Client VM configuration pane, enable just-in-time. This will enable the default settings.

  ![Screenshot showing the Microsoft Defender for cloud portal, allowing RDP on the client VM](./jit_allowing_rdp.png)

  ![Screenshot showing connecting to the VM using RDP](./rdp_connect.png)

  ![Screenshot showing connecting to the VM using JIT](./jit_rdp_connect.png)

#### The Logon scripts

- Once you log into the _HCIBox-Client_ VM, a PowerShell script will open and start running. **This script will take between 1-2 hours to finish**, and once completed, the script window will close automatically. At this point, the infrastructure deployment is complete.

  ![Screenshot showing _HCIBox-Client_](./automation.png)

  > **Note:** The automation will take 1-2 hours to fully complete. Do not close the PowerShell window during this time. When automation is completed successfully the PowerShell window will close and the desktop background will be changed to the HCIBox wallpaper.

- Infrastructure deployment is complete. Review the logs in C:\HCIBox\Logs for any issues.

- Check in Azure portal that both HCI nodes have been onboarded as Arc-enabled servers.

- Verify that both of the Arc-enabled servers have successfully installed the three HCI extensions: TelemetryAndDiagnostics, LCMController, DeviceManagement

### Azure portal Azure Stack HCI cluster validation and deployment

Azure Stack HCI uses a two-step process to create and register clusters in Azure using an ARM template.

  1. **Validate** - an ARM template is deployed with a "validate" flag. This begins the final cluster validation step and takes around 20 minutes.
  2. **Deploy** - the same ARM template is redeployed with the "deploy" flag. This deploys the cluster and Arc infrastructure and registers the cluster. This step takes around 2-3 hours.

#### Validate cluster in Azure portal

- Now you will use the generated ARM template to validate the HCI cluster in Azure portal. Open File Explorer on _HCIBox-Client_ and navigate to the _C:\HCIBox_ folder. Right click on the folder and open in VSCode.

- Open and review the hci.json and hci.parameters.json files in VSCode. Verify that the parameters file looks correct without "staging" placeholder values.

- Navigate to Azure portal and type "custom deployment" in the search bar, then select "Deploy a custom template".

  ![Screenshot showing custom deployment option](./deploy_custom_template.png)

- Select "Build your own template in the editor".

  ![Screenshot showing building your own template option](./build_your_own_template.png)

- Paste the contents of hci.json into the editor and click "Save".

  ![Screenshot showing hci.json in Azure portal](./save_template.png)

- Click "Edit parameters" and then paste the contents of hci.parameters.json into the editor and click "Save."

  ![Screenshot showing edit parameters option](./edit_parameters.png)

#### Deploy cluster in Azure portal

- When validation is complete navigate to the cluster resource in your HCIBox resource group.

- Click the link to deploy the validated cluster resource and then click through again to deploy the cluster. The cluster may take several hours to deploy.

- You can monitor progress on the Deployments tab of the cluster resource.


