---
type: docs
linkTitle: "Windows Admin Center"
weight: 9
toc_hide: true
---

## Windows Admin Center operations

Windows Admin Center (preview) is available from inside the Azure portal and can be used with HCIBox.

## Windows Admin Center in Azure portal

Windows Admin Center can be used directly from the Azure portal. To set this up for your HCIBox cluster, follow these steps:

- Navigate to the _HCIBox-Cluster_ resource and select the Windows Admin Center blade.

  ![Screenshot showing opening WAC in portal](./wac_portal_setup_1.png)

- Leave the port set to the default value and click Install. Installation will take a few minutes to complete.

  ![Screenshot showing installing WAC in portal](./wac_portal_setup_2.png)

- Once installation is complete, click Connect from the Windows Admin Center blade on the cluster resource.

  ![Screenshot showing connecting to WAC in portal](./wac_portal_setup_3.png)

- Connecting to Windows Admin Center requires using the domain account credential. Connect with your domain account as shown in the screenshot below.

  ![Screenshot showing connecting with domain account](./wac_portal_setup_4.png)

- You can now explore your cluster using Windows Admin Center in Azure portal.

  ![Screenshot showing Windows Admin Center in Azure portal](./wac_portal.png)

## Next steps

For additional Windows Admin Center operations, review the [official documentation](https://learn.microsoft.com/windows-server/manage/windows-admin-center/overview).
