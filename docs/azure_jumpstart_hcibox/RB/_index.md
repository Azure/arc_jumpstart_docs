---
type: docs
linkTitle: "Resource Bridge"
weight: 7
---

## Virtual machine provisioning with Azure Arc

Azure Stack HCI supports [VM provisioning the Azure portal](https://learn.microsoft.com/azure-stack/hci/manage/manage-arc-virtual-machines). Like all Azure Stack HCI clusters, the HCIBox cluster comes preconfigured with the components needed for VM management through Azure portal. Follow this guide to configure a basic VM from a marketplace image.

### Create Virtual Machine images from Azure marketplace

Before you can create virtual machines on your HCI cluster from Azure portal, you must create some VM images that can be used as a base. These images can be imported from Azure marketplace or provided directly by the user. In this use case you will create an image from Azure marketplace.

- Navigate to your cluster resource inside the HCIBox resource group and click it.

  ![Screenshot showing cluster resource](./hcicluster_rg.png)

- Click on "VM Images" in the menu and then click the "Add VM image" dropdown and select "From Azure Marketplace."

  ![Screenshot showing create VM](./add_image_from_marketplace.png)

- In this example we will select Windows Server 2022 Core Azure Edition from the list of images. Give your VM image a name, select the default custom location from the dropdown, and leave the storage path set to "Choose automatically." When everything looks good, click "Review and Create."

  ![Screenshot showing create VM image details](./vm_image_review_create.png)

- It will take some time for the VM image to download to your cluster from Azure marketplace. You can monitor progress by visiting the VM Image resource in your resource group and reviewing the resource properties.

  ![Screenshot of VM image properties](./monitor_vm_image_progress.png)

- Monitor the image as needed until is it finished downloading. While you wait, proceed to the next section to create the logical network on the cluster.

### Create a logical network on your HCI cluster

- From inside the _HCIBox-Client_ VM, open File Explorer and navigate to _C:\HCIBox_. Right click on the _Configure-VMLogicalNetwork.ps1_ PowerShell file and choose "Run with PowerShell." If you wish you can also review the file in VSCode.

## Next steps

Review the [Azure Stack HCI VM management](https://learn.microsoft.com/azure-stack/hci/manage/azure-arc-enabled-virtual-machines#what-is-azure-arc-resource-bridge) documentation for additional information.
