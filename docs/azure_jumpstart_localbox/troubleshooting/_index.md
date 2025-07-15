---
type: docs
linkTitle: "Troubleshooting"
weight: 10
---
# Troubleshooting LocalBox

## Troubleshooting Deployments

Occasionally deployments of LocalBox may fail at various stages. Common reasons for failed deployments include:

- Not enough vCPU quota available in your target Azure region - check vCPU quota and ensure you have at least 32 available. See the [prerequisites](../getting_started/#prerequisites) section for more details.
- Corruption when downloading LocalBox VHD files can interrupt deployments. LocalBox should automatically halt if this occurs. Re-running the PowerShell script at _C:\LocalBox\LocalBoxLogonScript.ps1_ can often repair this issue.
- RBAC permissions - check that Owner permissions is assigned to the user performing the deployment, without any [conditions](https://learn.microsoft.com/azure/role-based-access-control/delegate-role-assignments-portal?tabs=condition-editor) possibly constraining the Owner role.

If you have issues that you cannot resolve when deploying LocalBox please submit an issue on the [GitHub repo](https://github.com/microsoft/azure_arc/issues)

## Verifying Deployment with Pester Tests

LocalBox automatically runs a suite of Pester tests to verify that the infrastructure has been deployed correctly. These tests are executed at the end of the deployment process and on each user logon.

### What the Tests Verify

The Pester test suite includes two main test files:

- **Common Tests** (`common.tests.ps1`): Verifies that the LocalBox resource group contains the expected number of resources (25 or more)
- **Azure Local Tests** (`azlocal.tests.ps1`): Verifies that:
  - Virtual machines exist and are running
  - Azure Arc connected machines are properly registered and connected
  - If auto-deployment is enabled, the Azure Local cluster exists and is in a "Connected" state

### Viewing Test Results

Test results are displayed in several locations:

1. **Desktop Wallpaper**: Test results are automatically added to the desktop wallpaper using BGInfo, showing the number of tests that passed and failed
2. **Azure Resource Tags**: Test results are stored as tags on both the resource group and the LocalBox-Client VM:
   - `DeploymentStatus`: Shows test counts (e.g., "Tests succeeded: 15 Tests failed: 0")
   - `DeploymentProgress`: Shows overall status ("Completed" or "Failed")

### Reviewing Test Logs

To view detailed test output and identify which specific tests failed:

1. Navigate to the logs folder: `C:\LocalBox\Logs\`
2. Open `DeploymentStatus.log` - this contains the detailed Pester test output for failed (if any) and passed tests
3. Failed tests will show detailed error messages explaining what validation failed

### Manually Running Tests

If you need to re-run the tests manually:

1. Open PowerShell as Administrator on the LocalBox-Client VM
2. Run: `& "C:\LocalBox\Tests\Invoke-Test.ps1"`

The tests will execute and update both the wallpaper display and Azure resource tags with the current results.

### Common Test Failures and Solutions

- **Azure Arc Connected Machine tests fail**: Check that the Azure Arc agent is properly installed and the VM can connect to Azure
- **Cluster connectivity tests fail**: Verify that the Azure Local instance deployment completed successfully and the instance is properly registered with Azure. For additional details, go to the LocalBox resource group, click on _Deployments_ and review any errors for the 'localcluster-validate' and 'localcluster-deploy' deployments.
- **Resource count tests fail**: Check that all expected Azure resources were created in the resource group

### Exploring logs from the _LocalBox-Client_ virtual machine

Occasionally, you may need to review log output from scripts that run on the _LocalBox-Client_ virtual machines in case of deployment failures. To make troubleshooting easier, the LocalBox deployment scripts collect all relevant logs in the _C:\LocalBox\Logs_ folder on _LocalBox-Client_. A short description of the logs and their purpose can be seen in the list below:

| Log file                                      | Description                                                                                                                               |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| _C:\LocalBox\Logs\Bootstrap.log_              | Output from the initial bootstrapping script that runs on _LocalBox-Client_.                                                              |
| _C:\LocalBox\Logs\New-LocalBoxCluster.log_    | Output of _New-LocalBoxCluster.ps1_ which configures the Hyper-V host and builds the Azure Local instance, management VMs, and other configurations. |
| _C:\LocalBox\Logs\Generate-ARM-Template.log_  | Log output of the script that builds the _azlocal.json_ and _azlocal.parameters.json_ file                                                        |
| _C:\LocalBox\Logs\LocalBoxLogonScript.log_    | Log output from the orchestrator script that manages the provisioning processes.                          |
| _C:\LocalBox\Logs\DeploymentStatus.log_    | Log output from _Invoke-Test.ps1 script_
| _C:\LocalBox\Logs\Tools.log_                  | Log output from tools installation during bootstrap                                                                                       |

  ![Screenshot showing LocalBox logs folder on LocalBox-Client](./troubleshoot_logs.png)

If you are still having issues deploying LocalBox, please [submit an issue](https://aka.ms/JumpstartIssue) on GitHub and include a detailed description of your issue and the Azure region you are deploying to. Inside the _C:\LocalBox\Logs_ folder you can also find instructions for uploading your logs to an Azure storage account for review by the Jumpstart team.
