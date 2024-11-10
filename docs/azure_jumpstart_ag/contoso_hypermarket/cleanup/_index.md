---
type: docs
weight: 8
title: Clean up environment
linkTitle: Cleanup
---

# Cleanup deployment

To clean up your deployment, simply delete the resource group using Azure CLI or Azure portal.

  ```shell
  az group delete -n <name of your resource group>
  ```

  ![Screenshot showing az group delete](./img/az_group_delete.png)

  ![Screenshot showing group delete from Azure portal](./img/portal_delete.png)

## Next steps

If you still having issues with the deployment, please refer to the [Troubleshooting](../troubleshooting//) section. Otherwise, if you have additional questions or feedback, please refer to the [FAQ](../../../faq/) section.