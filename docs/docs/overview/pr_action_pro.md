### Overview

[PR-Action Pro](https://www.khulnasoft.com/pricing/) is a hosted version of PR-Action, provided by KhulnaSoft. A complimentary two-week trial is offered, followed by a monthly subscription fee.
PR-Action Pro is designed for companies and teams that require additional features and capabilities. It provides the following benefits:

1. **Fully managed** - We take care of everything for you - hosting, models, regular updates, and more. Installation is as simple as signing up and adding the PR-Action app to your GitHub\GitLab\BitBucket repo.

2. **Improved privacy** - No data will be stored or used to train models. PR-Action Pro will employ zero data retention, and will use an OpenAI and Claude accounts with zero data retention.

3. **Improved support** - PR-Action Pro users will receive priority support, and will be able to request new features and capabilities.

4. **Supporting self-hosted git servers** - PR-Action Pro can be installed on GitHub Enterprise Server, GitLab, and BitBucket. For more information, see the [installation guide](https://pr-action.khulnasoft.com/installation/pr_action_pro/).

5. **PR Chat** - PR-Action Pro allows you to engage in [private chat](https://pr-action.khulnasoft.com/chrome-extension/features/#pr-chat) about your pull requests on private repositories.

### Additional features

Here are some of the additional features and capabilities that PR-Action Pro offers:

| Feature                                                                                                              | Description                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Model selection**](https://pr-action.khulnasoft.com/usage-guide/PR_action_pro_models/#pr-action-pro-models)          | Choose the model that best fits your needs, among top models like `GPT4` and `Claude-Sonnet-3.5`                                                                 
| [**Global and wiki configuration**](https://pr-action.khulnasoft.com/usage-guide/configuration_options/)              | Control configurations for many repositories from a single location; <br>Edit configuration of a single repo without commiting code                              |
| [**Apply suggestions**](https://pr-action.khulnasoft.com/tools/improve/#overview)                                     | Generate commitable code from the relevant suggestions interactively by clicking on a checkbox                                                                   |
| [**Suggestions impact**](https://pr-action.khulnasoft.com/tools/improve/#assessing-impact)                         | Automatically mark suggestions that were implemented by the user (either directly in GitHub, or indirectly in the IDE) to enable tracking of the impact of the suggestions |
| [**CI feedback**](https://pr-action.khulnasoft.com/tools/ci_feedback/) | Automatically analyze failed CI checks on GitHub and provide actionable feedback in the PR conversation, helping to resolve issues quickly |
| [**Advanced usage statistics**](https://www.khulnasoft.com/contact/#/)                                                    | PR-Action Pro offers detailed statistics at user, repository, and company levels, including metrics about PR-Action usage, and also general statistics and insights |
| [**Incorporating companies' best practices**](https://pr-action.khulnasoft.com/tools/improve/#best-practices)         | Use the companies' best practices as reference to increase the effectiveness and the relevance of the code suggestions                                           |
| [**Interactive triggering**](https://pr-action.khulnasoft.com/tools/analyze/#example-usage)                           | Interactively apply different tools via the `analyze` command                                                                                                    |
| [**SOC2 compliance check**](https://pr-action.khulnasoft.com/tools/review/#configuration-options)                     | Ensures the PR contains a ticket to a project management system (e.g., Jira, Asana, Trello, etc.)                                                                
| [**Custom labels**](https://pr-action.khulnasoft.com/tools/describe/#handle-custom-labels-from-the-repos-labels-page) | Define custom labels for PR-Action to assign to the PR                                                                                                            |

### Additional tools

Here are additional tools that are available only for PR-Action Pro users:

| Feature | Description |
|---------|-------------|
| [**Custom Prompt Suggestions**](https://pr-action.khulnasoft.com/tools/custom_prompt/) | Generate code suggestions based on custom prompts from the user |
| [**Analyze PR components**](https://pr-action.khulnasoft.com/tools/analyze/) | Identify the components that changed in the PR, and enable to interactively apply different tools to them |
| [**Tests**](https://pr-action.khulnasoft.com/tools/test/) | Generate tests for code components that changed in the PR |
| [**PR documentation**](https://pr-action.khulnasoft.com/tools/documentation/) | Generate docstring for code components that changed in the PR |
| [**Improve Component**](https://pr-action.khulnasoft.com/tools/improve_component/) | Generate code suggestions for code components that changed in the PR |
| [**Similar code search**](https://pr-action.khulnasoft.com/tools/similar_code/) | Search for similar code in the repository, organization, or entire GitHub |


### Supported languages

PR-Action Pro leverages the world's leading code models - Claude 3.5 Sonnet and GPT-4. 
As a result, its primary tools such as `describe`, `review`, and `improve`, as well as the PR-chat feature, support virtually all programming languages.

For specialized commands that require static code analysis, PR-Action Pro offers support for specific languages. For more details about features that require static code analysis, please refer to the [documentation](https://pr-action.khulnasoft.com/tools/analyze/#overview).