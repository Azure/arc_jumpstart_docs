---
type: docs
weight: 3
title: Jumpstart Cerebral - Operations Assistance with Gen AI
linkTitle: Jumpstart Cerebral - Operations Assistance with Gen AI
---

# Jumpstart Cerebral - Gen AI Commercial and Operations assistance

## Overview

<img src="./img/cerebral_logo.png" alt="Jumpstart Cerebral logo" width="150"/>

Jumpstart Cerebral is an advanced Generative AI assistant that revolutionizes how store personnel interact with critical information across Contoso Hypermarket's diverse data sources. By combining powerful large language models with specialized databases, Cerebral delivers contextual assistance and intelligent insights through natural language interactions. The system leverages [Retrieval Augmented Generation (RAG)](https://azure.microsoft.com/products/phi) to synthesize information from technical documentation, real-time metrics, and business data into comprehensive, tailored responses.

Cerebral innovative hybrid architecture optimally balances edge computing with cloud capabilities. Whether processing queries via [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/overview) in the cloud or utilizing [Small Language Models (SLM)](https://azure.microsoft.com/products/phi) at the edge, Cerebral intelligently routes and handles requests based on their complexity and urgency. Through its deep understanding of industry context and user roles, Cerebral acts as an intelligent partner that enables staff to focus on value-adding activities rather than searching through multiple systems.

> **Note**: For detailed information about Cerebral's Generative AI capabilities, explore the [Azure OpenAI Service documentation](https://learn.microsoft.com/azure/ai-services/openai/overview) and [Microsoft Phi-3 - small language models (SLMs)](https://azure.microsoft.com/blog/introducing-phi-3-redefining-whats-possible-with-slms/)

## Business challenges

In today's complex retail environment, organizations face critical operational challenges that impact efficiency and decision-making capabilities. Store managers and staff often struggle with fragmented information spread across multiple systems, leading to delayed responses to critical inventory and operational issues. New employees face steep learning curves as they attempt to navigate various platforms and documentation sources, while maintenance teams lose valuable time searching through scattered technical documentation for troubleshooting procedures.

Cerebral addresses these pain points by providing a unified, intelligent interface that breaks down information silos and streamlines access to critical data and documentation. By leveraging natural language processing and contextual understanding, it transforms complex data retrieval and decision-making processes into simple, conversational interactions. This approach significantly reduces response times to operational issues, accelerates employee onboarding, and enables more efficient maintenance operations through instant access to relevant technical information.

## Architecture

The power of Cerebral lies in its sophisticated hybrid architecture that balances local processing with cloud capabilities. At its core, Cerebral operates on an edge-located [Arc-enabled Kubernetes cluster](https://learn.microsoft.com/azure/azure-arc/kubernetes/overview), which hosts the local language model (Microsoft Phi-3 Mini-4k) for rapid response to common queries. This edge infrastructure connects seamlessly with cloud services through [Azure IoT Operations](https://azure.microsoft.com/products/iot-operations), enabling a robust and scalable system that can handle everything from simple information requests to complex analytical queries.

Cerebral exposes its functionality through a comprehensive API layer that supports both REST and WebSocket connections, enabling real-time interactions and seamless integration with applications like the Contoso Hypermarket web interface.

At its core, Cerebral employs a query processing orchestrator that intelligently routes requests to appropriate data sources based on the nature of the query. For commercial data such as sales, inventory, and customer information, the system interfaces with SQL Server. Real-time device metrics and operational data are managed through InfluxDB, a specialized time-series database that captures everything from equipment performance to environmental readings. Technical documentation and operational procedures are accessed through a [Chroma vector database](https://www.trychroma.com/), enabling powerful RAG (Retrieval Augmented Generation) capabilities.

![Screenshot of Cerebral solution architecture diagram](./img/cerebral_architecture.png)

The system's AI processing capabilities are designed for flexibility, with the ability to leverage either Azure OpenAI for complex cloud-based processing or Small Language Models (SLM) for edge processing. This hybrid approach ensures optimal performance while maintaining data privacy and enabling offline operations when needed.

To support development, testing, and demonstrations, Cerebral includes a sophisticated data simulator that generates realistic streams of commercial transactions, device telemetry, and equipment status updates. This simulation capability is crucial for system validation and training scenarios.

> **Note**: To understand how Cerebral integrates with Contoso Hypermarket's data infrastructure, explore both the [Data pipeline and reporting for commercial sales](../data_pipeline/commercial/_index.md) and the [Data pipeline and reporting for operational technology (OT)](../data_pipeline/operational/_index.md) guides.

While currently demonstrated within Contoso Hypermarket's retail environment, the architecture is inherently designed for multi-industry adaptation. New data sources, industry verticals, and processing pipelines can be seamlessly integrated, ensuring that Cerebral can evolve to meet the needs of diverse operational contexts while maintaining consistent performance and reliability.

## Interacting with Cerebral

Throughout the Contoso Hypermarket interface, whether you're a store manager reviewing sales data, a maintenance technician checking equipment status, or a shopper seeking assistance, Cerebral is your AI-powered assistant ready to help with any query. The system provides an intuitive and seamless way to access information across all store systems and documentation.

> **Note**: To learn more about using the Contoso Hypermarket web applications and how Cerebral integrates with different operational interfaces, please refer to our [Shopper Insights Guide](../shopper_insights/_index.md).

### Getting started with Cerebral

1. **Accessing the Assistant**
   - Locate the Cerebral icon in the top-right corner of any page
   - Click the icon to open the sliding sidebar interface
   - The sidebar will smoothly slide in from the right side of the screen

![Screenshot of Cerebral location in the the Contoso Hypermarket's web interface](./img/cerebral_location.png)

2. **Interface Overview**
   - The sidebar presents a clean, focused chat interface
   - You'll see a welcome message: "Hi, I'm here to help! You can ask me questions using text or voice."
   - A text input field is available at the bottom of the panel
   - Voice input can be activated using the microphone icon
   - For technical users, a "Debug" checkbox is available to view backend processing details

![Screenshot of Cerebral interface](./img/cerebral_interface.png)

1. **Interaction Methods**
   - Type your question directly into the text field and press enter or click the send button
   - Click the microphone icon to use voice input
   - Cerebral will process your query and provide relevant information, data, or procedures based on your request

![Screenshot of Cerebral interface record button](./img/cerebral_interface_audio.png)

The interface is designed to be non-intrusive while remaining easily accessible throughout your work session. You can minimize the sidebar at any time by clicking the 'X' in the top-right corner, and reopen it whenever you need assistance.

The interaction is straightforward and natural - simply type your question or click the microphone icon to speak. Cerebral understands natural language queries across a wide range of topics. Below is an example of how a Sales Analyst can ask Cerebral _"What are our top 5 selling products this week?"_:

![Screenshot of Sales Analyst Cerebral interaction example](./img/sales_analyst_example.png)

Note that the examples and screenshots shown in this documentation are for illustration purposes only. While the core functionality remains the same, Cerebral's responses are dynamic and contextual to your specific situation and the latest available information and actual results and responses from Cerebral may vary depending on:

- Current data in your systems
- Real-time operational status
- Specific store configuration
- Updated procedures and documentation

> **Note**: For additional prompt examples, please refer to the ["Prompt examples"](https://github.com/fcabrera23/arc_jumpstart_docs/blob/canary/docs/azure_jumpstart_ag/contoso_hypermarket/cerebral/cerebral_appendix.md#prompt-examples) section in the Jumpstart Cerebral appendix file.

Based on your query, Cerebral automatically classifies the type of request and routes it to the appropriate system (documentation, real-time data, or business intelligence) to provide relevant and contextual responses. For demonstration purposes, users can enable the "Debug" checkbox in the interface to view behind-the-scenes details such as:

- Query classification (documentation, data, or relational)
- Generated database queries
- Data processing steps
- Response construction logic

![Screenshot of Cerebral interface debug toggle](./img/cerebral_debug_toggle.png)

> **Note**: For detailed information about data types and how Cerebral processes different sources of information, see the [Unified Data Sources](#unified-data-sources) section.

## Data integration and query processing

At the heart of Cerebral's architecture lies a sophisticated data integration system that seamlessly connects diverse information sources through an intelligent query processing pipeline. This unified approach transforms how organizations access and utilize their operational data.

### Unified data sources

The system orchestrates three specialized databases, each optimized for specific types of information and query patterns:

- **InfluxDB** powers Cerebral's real-time operational insights by managing time-series data from store equipment and systems. This specialized database captures everything from refrigeration temperatures to checkout queue lengths, enabling rapid analysis of current conditions and historical trends. Its optimized time-series capabilities ensure swift access to performance metrics and environmental data when seconds matter.

  - Captures real-time metrics from store equipment
  - Monitors system performance data
  - Tracks operational status
  - Stores historical trending data

> **Note**: For additional details, please refer to the ["MQTT simulated equipment metrics"](https://github.com/fcabrera23/arc_jumpstart_docs/blob/canary/docs/azure_jumpstart_ag/contoso_hypermarket/cerebral/cerebral_appendix.md#mqtt-simulated-equipment-metrics) section in the Jumpstart Cerebral appendix file.

- **SQL Server** handles all commercial operations data, providing a robust foundation for business intelligence. From transaction processing to inventory management, this relational database ensures accurate tracking of sales patterns, stock levels, and customer interactions, enabling data-driven decision making across the organization.

  - Manages transaction records
  - Tracks inventory levels
  - Stores customer data
  - Handles business intelligence queries

> **Note**: For additional details on the relational database structure and how it is used by Contoso Hypermarket for commercial and operational needs, please refer to the ["Relational database structure"](https://github.com/fcabrera23/arc_jumpstart_docs/blob/canary/docs/azure_jumpstart_ag/contoso_hypermarket/cerebral/cerebral_appendix.md#relational-database-structure) section in the Jumpstart Cerebral appendix file.

- **Chroma Vector Database** serves as the foundation for Cerebral's documentation intelligence. By indexing technical manuals, maintenance procedures, and operational guides, it enables sophisticated semantic search capabilities through Retrieval Augmented Generation (RAG). This allows Cerebral to understand the context and intent behind documentation queries, delivering precise and relevant information to users.
  
  - Stores and indexes technical documentation
  - Enables semantic search capabilities
  - Manages operational procedures and maintenance guides
  - Facilitates contextual information retrieval

### Available technical manuals

All technical documentation is automatically indexed and processed by Cerebral's RAG system, enabling natural language queries about any aspect of these systems. Instead of manually searching through PDFs, users can simply ask Cerebral specific questions about equipment operation, maintenance procedures, or troubleshooting steps.

> **Note**: For a list of the various technical manuals used by Contoso Hypermarket for operational needs, please refer to the ["Available technical manuals"](https://github.com/fcabrera23/arc_jumpstart_docs/blob/canary/docs/azure_jumpstart_ag/contoso_hypermarket/cerebral/cerebral_appendix.md#Available-technical-manuals) section in the Jumpstart Cerebral appendix file.

### Intelligent query routing

When a user interacts with Cerebral, their natural language query flows through a sophisticated decision tree that determines the optimal processing path. Questions about maintenance procedures are seamlessly routed to the vector database, equipment status checks are directed to the time-series database, and sales inquiries are processed through the relational database. This intelligent routing ensures that each query is handled by the most appropriate system, delivering fast, accurate responses while maintaining system efficiency.

For example, when a maintenance technician asks _"How do I calibrate Scale-02?"_, Cerebral recognizes this as a documentation query and leverages RAG to search the vector database for relevant procedures. Conversely, a store manager asking "What were our top-selling products today?" triggers a SQL query to analyze recent transaction data.

![Screenshot of Cerebral decision tree architecture diagram](./img/cerebral_decision_tree.png)

## Industry and Role adaptability

While Cerebral is currently showcased within Contoso Hypermarket's retail environment, its architecture is designed to be inherently multi-industry and role-adaptive. Through a sophisticated prompt catalog system, Cerebral can be customized to understand and respond to the unique contexts of different industries and professional roles.

Cerebral is design to support various roles and industry, for example, an Inventory Manager in the retail industry, how cares about monitoring the store stock levels.

> **Note**: For additional details on the the various industries and roles supported by Cerebral, please refer to the ["Industry and Role support"](https://github.com/fcabrera23/arc_jumpstart_docs/blob/canary/docs/azure_jumpstart_ag/contoso_hypermarket/cerebral/cerebral_appendix.md#Industry-and-Role-support) section in the Jumpstart Cerebral appendix file.

### Example prompts by category

Cerebral understands variations in phrasing and can maintain context through follow-up prompts. For example, in the "Documentation and Procedures" category, a prompt such _"What are the steps to close the store at the end of the day?"_ will lead to a step-by-step procedure with checklist. For more information about data sources and query processing, see the [Unified Data Sources](#unified-data-sources) section.

> **Note**: For additional examples of common prompts Cerebral can handle, please refer to the ["Common prompts Cerebral can handle"](https://github.com/fcabrera23/arc_jumpstart_docs/blob/canary/docs/azure_jumpstart_ag/contoso_hypermarket/cerebral/cerebral_appendix.md#Common-prompts-Cerebral-can-handle) section in the Jumpstart Cerebral appendix file.
>

### Prompt catalog system

Cerebral's flexibility comes from its extensible prompt catalog, which enables:

1. **Industry-Specific Context**
   - Customized terminology
   - Industry-relevant metrics
   - Sector-specific compliance requirements
   - Domain-specific best practices

2. **Role-Based Responses**
   - Tailored information access
   - Role-appropriate technical depth
   - Relevant recommendations
   - Authorized data visibility

Below is an example of how prompt customization scheme:

```json
{
    "industries": {
        "retail": {
            "roles": {
                "store_manager": {
                    "classification_prompt": "...",
                    "query_prompt": "...",
                    "response_prompt": "..."
                }
            }
        },
        "manufacturing": {
            "roles": {
                "maintenance_engineer": {
                    "classification_prompt": "...",
                    "query_prompt": "...",
                    "response_prompt": "..."
                }
            }
        }
    }
}
```

## Benefits of multi-industry design

Cerebral's architecture delivers three key advantages, making it a powerful solution across industries and roles:

1. **Scalability**: Easily expand to new industries and roles with minimal restructuring, supported by a flexible prompt management system and a growing knowledge base that adapts to new domains.  

2. **Consistency**: Standardized response formats and query handling ensure reliable, intuitive interactions across environments, streamlining maintenance and updates.  

3. **Customization**: Tailor each implementation with industry-specific terminology, role-based access controls, and context-relevant recommendations, providing actionable insights for every user, from store managers to maintenance engineers.  

This combination of scalability, consistency, and customization makes Cerebral adaptable and effective for diverse operational contexts.

## Next steps

Now that you have completed the _Jumpstart Cerebral - Gen AI Commercial and Operations assistance_ scenario, it's time to continue to the next one, [Commercial and Operations assistance with Speech-to-Text](../speech_to_text/_index.md).
