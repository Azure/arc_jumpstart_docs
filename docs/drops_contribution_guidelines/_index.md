---
type: docs
title: "Jumpstart Drops contribution guidelines"
linkTitle: "Jumpstart Drops contribution guidelines"
weight: 7
---

## Jumpstart Drops contribution guidelines

**Welcome to Jumpstart Drops contribution guidelines!**

We welcome contributions following the guidelines described in the Arc Jumpstart [contribution guidelines](./../contribution_guidelines).
Our goal is to create a simplified contribution process for our users that ensures high-quality standards for all submissions. There are two ways to contribute to Jumpstart Drops:

  1. Manual approach with a GitHub pull request
  2. Using the Drop [Creation Wizard](https://aka.ms/JumpstartDropsWizard)

### Using the Drop Creation Wizard
The **"Create Drop"** wizard simplifies the contribution process by guiding contributors through each step, making it easy to submit a new Drop. With the wizard, contributors can also use the live preview option to see how the Drop will appear on the website before finalizing the submission. This ensures that everything is perfect before sharing it with the community.

> **Note:** For video instructions on how to use the wizard, see the Jumpstart Drops Wizard [video series](https://aka.ms/JumpstartDropsWizard).

To submit a Drop using this method, follow the step-by-step guide below:

<div style="position: relative; box-sizing: content-box; max-height: 80vh; max-height: 80svh; width: 100%; aspect-ratio: 1.7170283806343907; padding: 40px 0 40px 0;"><iframe src="https://app.supademo.com/embed/cm7kw351x00n8zx0iazc9ippi?embed_v=2" loading="lazy" title="aka.ms/jumpstartdrops" allow="clipboard-write" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

### Manual approach with a GitHub Pull Request

The first is by opening a GitHub Pull Request following a simple [JSON scheme](https://github.com/Azure/arc_jumpstart_drops/blob/main/SCHEMA.md).

The contribution process consists of the following steps:

 ![Contribution flow](./contribution_flow.png)

  1. **Define source code hosting:** There are two alternatives to host the source code:

      - **Include Code in Pull Request:** Include the code/artifacts in the pull request and host all the content as part of the [Arc Jumpstart Drops repository](https://github.com/Azure/arc_jumpstart_drops).
      - **Reference to Author's Repository:** Keep the code in the author's repository and provide a reference URL under the _"Source"_ in the Drop definition file (check [Drops schema](https://github.com/Azure/arc_jumpstart_drops/blob/main/SCHEMA.md)). Ensure that the repository is publicly available.

  2. **Artifacts creation and uploading:** Develop and validate the source code of your Jumpstart Drop and the JSON schema file. Before submitting your pull request, ensure to check the following:

      - Test your Drop end-to-end in a new, unmodified environment to ensure it works as expected.
      - Choose a descriptive and actionable title that accurately represents your Drop's purpose. Remember that users will see this title when browsing the Drops gallery and should have a good idea of your Drop just by seeing the Drop's card.
      - Provide clear documentation that includes screenshots or videos demonstrating the steps involved and potential outcomes.
      - Have someone else review your code before submitting it. Don't include any credentials as part of your submission.
      - Ensure checking the spelling, grammar, and wording of your submission. To help validation, use [Vale](https://vale.sh/), already configured as part of the project. Ensure to use `vale sync` before starting linting, to get the latest configurations.

The final submission should contain the following files:

- **Source Code**: Include all the code files you've created, along with any necessary documentation (README, images, videos, etc.). Ensure these files follow the correct structure defined in the [folder structure](#folder-structure) section.

- **Drop Definition**: Provide a JSON file with all the required fields as described in the [Drops Schema](https://github.com/Azure/arc_jumpstart_drops/blob/main/SCHEMA.md) definition. This file will be used by the Arc Jumpstart Drops page to create a Drop card with all the necessary information, as you can see in the following image.

    ![Drop card](./drop_definition.png)

    1. Drop card created for each *JSON* definition schema file placed under the [drops](https://github.com/Azure/arc_jumpstart_drops/tree/main/drops) folder, with a unique *Title* and *Authors*. The name should be unique, have a proper description, and use **snake_case**.
    2. Description of the Drop.
    3. Filter bar to filter Drops based on the metadata of the Drop, like tags, products, creation date, and topics.
    4. Tags and action buttons: _Download_ and _Share_.

3. **Create Pull Request to Canary**: Submit your pull request (PR) to the Canary branch of [Arc Jumpstart Drops](https://github.com/Azure/arc_jumpstart_drops).

    For example, the following Drop submission aims to contribute the code to the [arc_jumpstart_drops](https://github.com/Azure/arc_jumpstart_drops) repository, hence as part of the pull request you can see the `win11_iot_ram_deduction.json` file under the `drops` folder, and then the artifacts under the `script_automation/win11_iot_ram_deduction` folder. Also, you can see that the *Source* is pointing to the [arc_jumpstart_drops](https://github.com/Azure/arc_jumpstart_drops) repository.

    ![Pull request example](./drop_submission.png)

4. **GitHub Checks**: As part of the validation process, there are multiple [GitHub Actions](https://github.com/Azure/arc_jumpstart_drops/actions) that run during the pull request review process to ensure:

      - Drop JSON schema definition and folder structure.
      - [MIT licensing](https://github.com/Azure/arc_jumpstart_drops?tab=MIT-1-ov-file#readme) and Microsoft CLA license check.
      - CodeQL for vulnerabilities.
      - [Vale.sh](https://vale.sh/) linter for documentation grammar and styling.

    When creating a pull request, you'll see your checks running for ~2-3 minutes. Carefully review the result of the checks, and fix any errors found on your submission.

     ![Pull request checks](./checks.png)

   - **Manual review from Jumpstart Core maintainers**: Reviewers will be added based on the products and type of Drop submitted. The PR can only be merged if all GitHub checks pass and at least 2 reviewers approve the submission.

   - **Merge to Canary**: If everything is correct, the PR will be merged to the **canary** branch, and the new Drop will be part of the approved Drops curated list.

   - **Validation with Preview Site**: Validate the changes using the [Preview Arc Jumpstart site](https://bvt.test.arcjumpstart.azure.com/azure_jumpstart_drops). Ensure to check that your Drop is rendering correctly. Take some time to review the Drop card, and once finished, review the right-sidebar with all the context from your _README.md_ or _Index.md_.

   - **Merge to Main**: Finally, once the **Canary** branch is merged to **Main** and published to Production, the Drop will be available as part of [Jumpstart Drops](https://jumpstart.azure.com/azure_jumpstart_drops).

## Drop Index

<div style="position: relative; box-sizing: content-box; max-height: 80vh; max-height: 80svh; width: 100%; aspect-ratio: 1.7170283806343907; padding: 40px 0 40px 0;"><iframe src="https://app.supademo.com/embed/cm7memt8s00m82l0jn4kvbfpn?embed_v=2" loading="lazy" title="Jumpstart Drops Index" allow="clipboard-write" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

## Folder structure

The folder structure guidelines for submitting Drop source code as part of a Pull Request into the Arc Jumpstart Drops repository are as follows:

<div style="position: relative; box-sizing: content-box; max-height: 80vh; max-height: 80svh; width: 100%; aspect-ratio: 1.7777777777777777; padding: 40px 0 40px 0;"><iframe src="https://app.supademo.com/embed/cm7mh44g4014iz50ib91kmzan?embed_v=2" loading="lazy" title="Jumpstart Drops folder structure" allow="clipboard-write" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>
