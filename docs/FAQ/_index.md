---
type: docs
title: "Jumpstart FAQ"
linkTitle: "Jumpstart FAQ"
weight: 8
---

# Jumpstart Frequently Asked Questions (FAQ)

## Can I contribute to the Arc Jumpstart?

Absolutely! Arc Jumpstart is a community-driven open source project, and contributions are welcomed. To get started, review the [Jumpstart contribution guidelines](../contribution_guidelines/) and our [Code of Conduct](https://aka.ms/JumpstartCOC).

## Can I use an Azure free trial account with Arc Jumpstart?

Yes, you can use an Azure [free trial account](https://azure.microsoft.com/free). However, some Jumpstart features may require additional Azure consumption isn’t provided in a free trial.

## Does Azure Arc Jumpstart provide free credit to Azure or other cloud providers?

Arc Jumpstart does not provide free credit to Azure or any other cloud providers. To use the Jumpstart you must provide your own environments to run any of the scenarios or solutions.

## What permissions do I need to deploy Arc Jumpstart scenarios and solutions?

Each Arc Jumpstart scenario and solution describes what is needed to run the automation — take a look at the prerequisites section. Most of them will ask you to create a service principal, so you will need an Azure **User Access Administrator** or **Role Base Access Control Administrator** permissions.

## Is Arc Jumpstart considered "production-ready"?

The intention of the Arc Jumpstart is to focus on the core Azure Arc, edge, and IoT capabilities, deployment scenarios, use cases, and ease of use. It does not focus on Azure best practices, and/or other products or open source projects being leveraged in our code. Jumpstart Scenarios, ArcBox, HCIBox, and Agora are all intended for evaluation, training, and demo purposes only and are not supported for production use cases.

## Is there guidance on how to run a demo using the Arc Jumpstart?

You can get additional information and insights on how to use Arc Jumpstart on our [YouTube channel](https://www.youtube.com/@azurearcjumpstart).

## What if something doesn’t work?

If you have any issues or questions, please [open a GitHub issue](https://aka.ms/JumpstartIssue), and one of our Jumpstart core maintainers or community members will address it as soon as possible. For any Azure product-related issues, please open a [support ticket](https://azure.microsoft.com/support/create-ticket).

## Can I suggest improvements and features?

Of course! For any suggestion, please [open a GitHub feature](https://aka.ms/JumpstartFeature), and one of our Jumpstart core maintainers will address it as soon as possible. You are also encouraged to start a thread in our [GitHub Discussions](https://aka.ms/JumpstartDiscussions).

## I want to share my awesome Azure Arc, edge, or IoT story with the Jumpstart community—how can I do that?

We’d love to hear it! Fill out the [submission form](https://aka.ms/LightningGuest) and we’ll get back to you soon.

## Is there a public Azure Arc Jumpstart Roadmap?

An up-to-date roadmap for Arc Jumpstart scenarios can be found under [the repository GitHub Project](https://aka.ms/JumpstartRoadmap).


# Jumpstart Drops Frequently Asked Questions (FAQ)

## Can I contribute a Drop?
Arc Jumpstart Drops is fully open-source and welcomes all contributions that follow the Jumpstart Drops [contribution process](../contribution_guidelines/). Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant Arc Jumpstart team the rights to use your contribution. For details, visit [Microsoft CLA](https://cla.opensource.microsoft.com).

## Do I need to host my contribution source code inside the Jumpstart Drops GitHub repository?
No, it's not mandatory to host your contribution source code in the Jumpstart Drops repository. You have two options for hosting the code, and you can choose the one that suits your use case better:

- **Include the code in the Pull Request (PR)**: You can include the code as part of your PR and host it within the Arc [Jumpstart Drops GitHub repository](https://github.com/Azure/arc_jumpstart_drops).
- **Keep the code in your own repository**: Alternatively, you can keep the code in your own repository and provide a reference/URL to it in the Drop [definition file](https://github.com/Azure/arc_jumpstart_drops/blob/main/SCHEMA.md).

## Do I need to authenticate to the Arc Jumpstart website to contribute or use Jumpstart Drops?
No, authentication and logging in to the portal aren't required to contribute or use Jumpstart Drops. However, if you are logged in, we're developing features to provide contributors with insights on their contributions and enhance their experience and submission.

### What's the Jumnpstart Drop licensing schema?
Jumpstart Drops follows the same [MIT](https://github.com/Azure/arc_jumpstart_drops/blob/main/LICENSE) licensing as all the other Arc Jumpstart Products. All contributions should also be under an [MIT](https://github.com/Azure/arc_jumpstart_drops/blob/main/LICENSE) license. 

The MIT license is a permissive open-source software license that allows for the use, modification, and distribution of the licensed software, as long as the original copyright notice and license terms are included in any copies or distributions of the software. 

For more information, see [contribution process](../contribution_guidelines/).

## How can I discover a Jumsptart Drop?
To discover a Jumpstart Drop tailored to your needs, leverage the filters and sorting options available on the Arc Jumpstart Drops main page. Start by visiting [Arc Jumpstart Drops](https://arcjumpstart.com/arc_jumpstart_drops) and then use the panel on the right-hand side to filter by criteria such as *Programming* *Language*, *Product*, *Difficulty*, *Industry*, *Topic*, and more. Additionally, you can always use the search bar at the top to search across all Jumpstart content, including Jumpstart Drops.

## How do I use a Jumpstart Drop?
Using Jumsptart Drop is straightforward. Simply download the Jumnpstart Drop by clicking the Download button on the Jumpstart Drop's page. After downloading, you will have a .zip file containing all the necessary source code to run the Jumpstart Drop. Depending on the Jumpstart Drop, you may need to configure some prerequisites, but all instructions should be included in the *index.md* file of the Jumpstart Drop.

## How do I submit a Jumpstart Drop?
Submitting a Jumpstart Drop is easy, upload your content and create a pull request directly in the Arc Jumpstart Drops repository.
<!-- You can choose to create a pull request directly in the Arc Jumpstart Drops repository or use the [Submit Jumpstart Drop](https://arcjumpstart.com/arc_jumpstart_drops) form for a streamlined process.  -->
Refer to the Jumpstart Drops [contribution process](../contribution_guidelines/) guide for detailed instructions.

## How's support and maintenance handled for Jumpstart Drops?
Support and maintenance for Jumpstart Drops are managed through GitHub Issues, where bugs and feature requests can be tracked. The project follows the support approach outlined in [Arc Jumpstart Support](https://github.com/Azure/arc_jumpstart_docs/blob/main/SUPPORT.md).

**Important**: _Please note that Jumpstart Drops don't come with official support or warranty, but the community is encouraged to provide assistance to the best of their ability._

## What tools are used for code maintenance in this project?
All Jumpstart Drop owners are responsible for the code maintenance of their source code. If you chose to host the Jumpstart Drop source code as part of the Jumpstart Drops repository, we will run some check for code maintenance, like **CodeQL** and **GitHub Dependabot** security alerts. We're actively looking into developing new features to help contributors maintain their source code. If you have suggestions, please create an [Issue](https://github.com/Azure/arc_jumpstart_drops/issues/new?assignees=fcabrera23&labels=triage&projects=&template=%F0%9F%90%9Bbug-report.md&title=) with your suggested approach.