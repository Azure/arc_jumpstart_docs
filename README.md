# Azure Arc Jumpstart documentation

Welcome to the Arc Jumpstart documentation repository! This repository is your go-to resource for in-depth guides, best practices, and detailed documentation related to Azure Arc. Whether you're a beginner exploring the basics or an experienced user optimizing your deployment, you'll find valuable insights tailored to your needs. This repository complements our [source code repository](https://aka.ms/JumpstartGitHubCode) and acts has the documentation source repository which populates the [Arc Jumpstart](https://aka.ms/arcjumpstart) website.

<p align="center">
  <img src="/img/logo/jumpstart.png" alt="Arc Jumpstart logo" width="320">
</p>

**Note:** This repository does not contain the source code for the automation scripts and tools of the Arc Jumpstart. The source code for Arc Jumpstart can be found in another [dedicated repository](https://aka.ms/JumpstartGitHubCode).

## What you'll find here

- **Documents:** Arc Jumpstart markdown files utilized in scenarios and solutions, offering comprehensive technical information.
- **Visual Resources:** Clear and concise screenshots providing visual context for easier comprehension of the documentation.
- **Supportive Documents and Files:** Additional resources used across the [Arc Jumpstart](https://aka.ms/ArcJumpstart) website, aiding in various contexts and providing supplemental information.

## How to utilize this repository

This documentation repository is tailored for contributors and works in tandem with the [our source code repository](https://aka.ms/JumpstartGitHubCode). While not mandatory, it is highly probable that contributors will need to clone both repositories to effectively contribute to Arc Jumpstart.

Before you start, we recommend familiarizing yourself with our comprehensive [contribution guidelines](https://aka.ms/JumpstartContribution). These guidelines outline the standards and practices we follow, ensuring consistency and quality across our documentation.

If you're unsure about your future contribution, don't hesitate to start a [GitHub discussion](https://aka.ms/JumpstartDiscussions). This is a great place to ask questions, share ideas, or get feedback on potential contributions. Our community is here to help and we welcome all levels of experience.

Happy contributing!

## Branch guidance

The Arc Jumpstart docs repository handles branching similarly to most code repositories. Two primary branches are maintained, each one attached to a specific website slot (prod/canary). 

The following branches are currently maintained:

| Branch                                                       | Website                    | Description                                                                                      |
| ------------------------------------------------------------ | -------------------------- | ------------------------------------------------------------------------------------------------ |
| [main](https://github.com/Azure/arc_jumpstart_docs) (primary)               | https://arcjumpstart.com/       | Latest Arc Jumpstart release documentation. This is the latest documentation available in the deployed to the production slot. |
| [canary](https://github.com/Azure/arc_jumpstart_docs/tree/canary) (canary) | https://preview.arcjumpstart.com/ | Pre-release documentation. Doc updates should be merged to the canary branch for preview validation before merging to the main branch. |

## Cloning the repositories

To contribute, you'll likely need to clone both this repository and the [source code repository](https://github.com/Azure/arc_jumpstart_docs). Use the following commands:

```bash
git clone https://github.com/Azure/arc_jumpstart_docs.git
git clone https://github.com/microsoft/azure_arc.git
```

As we continuously improve and expand Arc Jumpstart, we recommend keeping your local clones of the repositories up-to-date. You can do this by pulling the latest changes from the main branch:

```bash
git pull origin main
```

## Contribution and feedback

We value your input! If you have suggestions, feedback, or valuable insights to share, feel free to open an issue. Your contributions help us improve the documentation for the entire community.

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit the [Microsoft Contributor License Agreements website](https://cla.opensource.microsoft.com).

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).

Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
