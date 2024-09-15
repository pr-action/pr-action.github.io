<div align="center">

<div align="center">


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://khulnasoft.com/images/pr_action/logo-dark.png" width="330">
  <source media="(prefers-color-scheme: light)" srcset="https://khulnasoft.com/images/pr_action/logo-light.png" width="330">
  <img src="https://khulnasoft.com/images/pr_action/logo-light.png" alt="logo" width="330">

</picture>
<br/>
KhulnaSoft PR-Action aims to help efficiently review and handle pull requests, by providing AI feedback and suggestions
</div>

[![GitHub license](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://github.com/Pr-action/pr-action/blob/main/LICENSE)
[![Static Badge](https://img.shields.io/badge/Chrome-Extension-violet)](https://chromewebstore.google.com/detail/pr-action-chrome-extension/ephlnjeghhogofkifjloamocljapahnl)
[![Static Badge](https://img.shields.io/badge/Code-Benchmark-blue)](https://pr-action-docs.khulnasoft.com/finetuning_benchmark/)
[![Discord](https://badgen.net/badge/icon/discord?icon=discord&label&color=purple)](https://discord.com/channels/1057273017547378788/1126104260430528613)
[![Twitter](https://img.shields.io/twitter/follow/khulnasoft)](https://twitter.com/khulnasoft)
[![Cheat Sheet](https://img.shields.io/badge/Cheat-Sheet-red)](https://www.khulnasoft.com/images/pr_action/cheat_sheet.pdf)
    <a href="https://github.com/Pr-action/pr-action/commits/main">
    <img alt="GitHub" src="https://img.shields.io/github/last-commit/Pr-action/pr-action/main?style=for-the-badge" height="20">
    </a>
</div>

### [Documentation](https://pr-action-docs.khulnasoft.com/)
- See the [Installation Guide](https://pr-action-docs.khulnasoft.com/installation/) for instructions on installing PR-Action on different platforms.

- See the [Usage Guide](https://pr-action-docs.khulnasoft.com/usage-guide/) for instructions on running PR-Action tools via different interfaces, such as CLI, PR Comments, or by automatically triggering them when a new PR is opened.

- See the [Tools Guide](https://pr-action-docs.khulnasoft.com/tools/) for a detailed description of the different tools, and the available configurations for each tool.


## Table of Contents
- [News and Updates](#news-and-updates)
- [Overview](#overview)
- [Example results](#example-results)
- [Try it now](#try-it-now)
- [PR-Action Pro 💎](https://pr-action-docs.khulnasoft.com/overview/pr_action_pro/)
- [How it works](#how-it-works)
- [Why use PR-Action?](#why-use-pr-action)
  
## News and Updates

### September 12, 2024
[Dynamic context](https://pr-action-docs.khulnasoft.com/core-abilities/dynamic_context/) is now the default option for context extension. 
This feature enables PR-Action to dynamically adjusting the relevant context for each code hunk, while avoiding overflowing the model with too much information.

### September 3, 2024

New version of PR-Action, v0.24 was released. See the [release notes](https://github.com/Pr-action/pr-action/releases/tag/v0.24) for more information.

### August 26, 2024

New version of [PR Action Chrome Extension](https://chromewebstore.google.com/detail/pr-action-chrome-extension/ephlnjeghhogofkifjloamocljapahnl) was released, with full support of context-aware **PR Chat**. This novel feature is free to use for any open-source repository. See more details in [here](https://pr-action-docs.khulnasoft.com/chrome-extension/#pr-chat).

<kbd><img src="https://www.khulnasoft.com/images/pr_action/pr_chat_1.png" width="768"></kbd>

<kbd><img src="https://www.khulnasoft.com/images/pr_action/pr_chat_2.png" width="768"></kbd>


### August 11, 2024
Increased PR context size for improved results, and enabled [asymmetric context](https://github.com/Pr-action/pr-action/pull/1114/files#diff-9290a3ad9a86690b31f0450b77acd37ef1914b41fabc8a08682d4da433a77f90R69-R70)

### August 10, 2024
Added support for [Azure devops pipeline](https://pr-action-docs.khulnasoft.com/installation/azure/) - you can now easily run PR-Action as an Azure devops pipeline, without needing to set up your own server.


### August 5, 2024
Added support for [GitLab pipeline](https://pr-action-docs.khulnasoft.com/installation/gitlab/#run-as-a-gitlab-pipeline) - you can now run easily PR-Action as a GitLab pipeline, without needing to set up your own server.

### July 28, 2024

(1) improved support for bitbucket server - [auto commands](https://github.com/Pr-action/pr-action/pull/1059) and [direct links](https://github.com/Pr-action/pr-action/pull/1061)

(2) custom models are now [supported](https://pr-action-docs.khulnasoft.com/usage-guide/changing_a_model/#custom-models)



## Overview
<div style="text-align:left;">

Supported commands per platform:

|       |                                                                                                         | GitHub             | Gitlab             | Bitbucket          | Azure DevOps |
|-------|---------------------------------------------------------------------------------------------------------|:--------------------:|:--------------------:|:--------------------:|:------------:|
| TOOLS | Review                                                                                                  | ✅ | ✅ | ✅ |      ✅       |
|       | ⮑ Incremental                                                                                           | ✅ |                    |                    |              |
|       | ⮑ [SOC2 Compliance](https://pr-action-docs.khulnasoft.com/tools/review/#soc2-ticket-compliance) 💎            | ✅ | ✅ | ✅ |              |
|       | Describe                                                                                                | ✅ | ✅ | ✅ |      ✅       |
|       | ⮑ [Inline File Summary](https://pr-action-docs.khulnasoft.com/tools/describe#inline-file-summary) 💎          | ✅ |                    |                    |              |
|       | Improve                                                                                                 | ✅ | ✅ | ✅ |      ✅       |
|       | ⮑ Extended                                                                                              | ✅ | ✅ | ✅ |      ✅       |
|       | Ask                                                                                                     | ✅ | ✅ | ✅ |      ✅       |
|       | ⮑ [Ask on code lines](https://pr-action-docs.khulnasoft.com/tools/ask#ask-lines)                              | ✅ | ✅ |                    |              |
|       | [Custom Prompt](https://pr-action-docs.khulnasoft.com/tools/custom_prompt/) 💎                                | ✅ | ✅ | ✅ |              |
|       | [Test](https://pr-action-docs.khulnasoft.com/tools/test/) 💎                                                  | ✅ | ✅ |                    |              |
|       | Reflect and Review                                                                                      | ✅ | ✅ | ✅ |      ✅       |
|       | Update CHANGELOG.md                                                                                     | ✅ | ✅ | ✅ |      ✅       |
|       | Find Similar Issue                                                                                      | ✅ |                    |                    |              |
|       | [Add PR Documentation](https://pr-action-docs.khulnasoft.com/tools/documentation/) 💎                         | ✅ | ✅ |                   |              |
|       | [Custom Labels](https://pr-action-docs.khulnasoft.com/tools/custom_labels/) 💎                                | ✅ | ✅ |                    |              |
|       | [Analyze](https://pr-action-docs.khulnasoft.com/tools/analyze/) 💎                                            | ✅ | ✅ |                    |              |
|       | [CI Feedback](https://pr-action-docs.khulnasoft.com/tools/ci_feedback/) 💎                                    | ✅ |                    |                    |              |
|       | [Similar Code](https://pr-action-docs.khulnasoft.com/tools/similar_code/) 💎                                  | ✅ |                    |                    |              |
|       |                                                                                                         |                    |                    |                    |              |
| USAGE | CLI                                                                                                     | ✅ | ✅ | ✅ |      ✅       |
|       | App / webhook                                                                                           | ✅ | ✅ | ✅ |      ✅       |
|       | Tagging bot                                                                                             | ✅ |                    |                    |              |
|       | Actions                                                                                                 | ✅ |✅| ✅ |✅|
|       |                                                                                                         |                    |                    |                    |              |
| CORE  | PR compression                                                                                          | ✅ | ✅ | ✅ |      ✅       |
|       | Repo language prioritization                                                                            | ✅ | ✅ | ✅ |      ✅       |
|       | Adaptive and token-aware file patch fitting                                                             | ✅ | ✅ | ✅ |      ✅       |
|       | Multiple models support                                                                                 | ✅ | ✅ | ✅ |      ✅       |
|       | [Static code analysis](https://pr-action-docs.khulnasoft.com/core-abilities/#static-code-analysis) 💎         | ✅ | ✅ | ✅ |              |
|       | [Global and wiki configurations](https://pr-action-docs.khulnasoft.com/usage-guide/configuration_options/) 💎 | ✅ | ✅ | ✅ |              |
|       | [PR interactive actions](https://www.khulnasoft.com/images/pr_action/pr-actions.mp4) 💎                       | ✅ |        ✅           |                    |              |
- 💎 means this feature is available only in [PR-Action Pro](https://www.khulnasoft.com/pricing/)

[//]: # (- Support for additional git providers is described in [here]&#40;./docs/Full_environments.md&#41;)
___

‣ **Auto Description ([`/describe`](https://pr-action-docs.khulnasoft.com/tools/describe/))**: Automatically generating PR description - title, type, summary, code walkthrough and labels.
\
‣ **Auto Review ([`/review`](https://pr-action-docs.khulnasoft.com/tools/review/))**: Adjustable feedback about the PR, possible issues, security concerns, review effort and more.
\
‣ **Code Suggestions ([`/improve`](https://pr-action-docs.khulnasoft.com/tools/improve/))**: Code suggestions for improving the PR.
\
‣ **Question Answering ([`/ask ...`](https://pr-action-docs.khulnasoft.com/tools/ask/))**: Answering free-text questions about the PR.
\
‣ **Update Changelog ([`/update_changelog`](https://pr-action-docs.khulnasoft.com/tools/update_changelog/))**: Automatically updating the CHANGELOG.md file with the PR changes.
\
‣ **Find Similar Issue ([`/similar_issue`](https://pr-action-docs.khulnasoft.com/tools/similar_issues/))**: Automatically retrieves and presents similar issues.
\
‣ **Add Documentation 💎  ([`/add_docs`](https://pr-action-docs.khulnasoft.com/tools/documentation/))**: Generates documentation to methods/functions/classes that changed in the PR.
\
‣ **Generate Custom Labels 💎 ([`/generate_labels`](https://pr-action-docs.khulnasoft.com/tools/custom_labels/))**: Generates custom labels for the PR, based on specific guidelines defined by the user.
\
‣ **Analyze 💎 ([`/analyze`](https://pr-action-docs.khulnasoft.com/tools/analyze/))**: Identify code components that changed in the PR, and enables to interactively generate tests, docs, and code suggestions for each component.
\
‣ **Custom Prompt 💎 ([`/custom_prompt`](https://pr-action-docs.khulnasoft.com/tools/custom_prompt/))**: Automatically generates custom suggestions for improving the PR code, based on specific guidelines defined by the user.
\
‣ **Generate Tests 💎 ([`/test component_name`](https://pr-action-docs.khulnasoft.com/tools/test/))**: Generates unit tests for a selected component, based on the PR code changes.
\
‣ **CI Feedback 💎 ([`/checks ci_job`](https://pr-action-docs.khulnasoft.com/tools/ci_feedback/))**: Automatically generates feedback and analysis for a failed CI job.
\
‣ **Similar Code 💎 ([`/find_similar_component`](https://pr-action-docs.khulnasoft.com/tools/similar_code/))**: Retrieves the most similar code components from inside the organization's codebase, or from open-source code.
___

## Example results
</div>
<h4><a href="https://github.com/Pr-action/pr-action/pull/530">/describe</a></h4>
<div align="center">
<p float="center">
<img src="https://www.khulnasoft.com/images/pr_action/describe_new_short_main.png" width="512">
</p>
</div>
<hr>

<h4><a href="https://github.com/Pr-action/pr-action/pull/732#issuecomment-1975099151">/review</a></h4>
<div align="center">
<p float="center">
<kbd>
<img src="https://www.khulnasoft.com/images/pr_action/review_new_short_main.png" width="512">
</kbd>
</p>
</div>
<hr>

<h4><a href="https://github.com/Pr-action/pr-action/pull/732#issuecomment-1975099159">/improve</a></h4>
<div align="center">
<p float="center">
<kbd>
<img src="https://www.khulnasoft.com/images/pr_action/improve_new_short_main.png" width="512">
</kbd>
</p>
</div>
<hr>

<h4><a href="https://github.com/Pr-action/pr-action/pull/530">/generate_labels</a></h4>
<div align="center">
<p float="center">
<kbd><img src="https://www.khulnasoft.com/images/pr_action/geneare_custom_labels_main_short.png" width="300"></kbd>
</p>
</div>

[//]: # (<h4><a href="https://github.com/Pr-action/pr-action/pull/78#issuecomment-1639739496">/reflect_and_review:</a></h4>)

[//]: # (<div align="center">)

[//]: # (<p float="center">)

[//]: # (<img src="https://www.khulnasoft.com/images/reflect_and_review.gif" width="800">)

[//]: # (</p>)

[//]: # (</div>)

[//]: # (<h4><a href="https://github.com/Pr-action/pr-action/pull/229#issuecomment-1695020538">/ask:</a></h4>)

[//]: # (<div align="center">)

[//]: # (<p float="center">)

[//]: # (<img src="https://www.khulnasoft.com/images/ask-2.gif" width="800">)

[//]: # (</p>)

[//]: # (</div>)

[//]: # (<h4><a href="https://github.com/Pr-action/pr-action/pull/229#issuecomment-1695024952">/improve:</a></h4>)

[//]: # (<div align="center">)

[//]: # (<p float="center">)

[//]: # (<img src="https://www.khulnasoft.com/images/improve-2.gif" width="800">)

[//]: # (</p>)

[//]: # (</div>)
<div align="left">


</div>
<hr>


## Try it now

Try the GPT-4 powered PR-Action instantly on _your public GitHub repository_. Just mention `@KhulnaSoft-Action` and add the desired command in any PR comment. The action will generate a response based on your command.
For example, add a comment to any pull request with the following text:
```
@KhulnaSoft-Action /review
```
and the action will respond with a review of your PR.

Note that this is a promotional bot, suitable only for initial experimentation.
It does not have 'edit' access to your repo, for example, so it cannot update the PR description or add labels (`@KhulnaSoft-Action /describe` will publish PR description as a comment). In addition, the bot cannot be used on private repositories, as it does not have access to the files there.


![Review generation process](https://www.khulnasoft.com/images/demo-2.gif)


To set up your own PR-Action, see the [Installation](https://pr-action-docs.khulnasoft.com/installation/) section below.
Note that when you set your own PR-Action or use KhulnaSoft hosted PR-Action, there is no need to mention `@KhulnaSoft-Action ...`. Instead, directly start with the command, e.g., `/ask ...`.

---


## PR-Action Pro 💎
[PR-Action Pro](https://www.khulnasoft.com/pricing/) is a hosted version of PR-Action, provided by KhulnaSoft. It is available for a monthly fee, and provides the following benefits:
1. **Fully managed** - We take care of everything for you - hosting, models, regular updates, and more. Installation is as simple as signing up and adding the PR-Action app to your GitHub\GitLab\BitBucket repo.
2. **Improved privacy** - No data will be stored or used to train models. PR-Action Pro will employ zero data retention, and will use an OpenAI account with zero data retention.
3. **Improved support** - PR-Action Pro users will receive priority support, and will be able to request new features and capabilities.
4. **Extra features** -In addition to the benefits listed above, PR-Action Pro will emphasize more customization, and the usage of static code analysis, in addition to LLM logic, to improve results. 
See [here](https://pr-action-docs.khulnasoft.com/#pr-action-pro) for a list of features available in PR-Action Pro.



## How it works

The following diagram illustrates PR-Action tools and their flow:

![PR-Action Tools](https://khulnasoft.com/images/pr_action/diagram-v0.9.png)

Check out the [PR Compression strategy](https://pr-action-docs.khulnasoft.com/core-abilities/#pr-compression-strategy) page for more details on how we convert a code diff to a manageable LLM prompt

## Why use PR-Action?

A reasonable question that can be asked is: `"Why use PR-Action? What makes it stand out from existing tools?"`

Here are some advantages of PR-Action:

- We emphasize **real-life practical usage**. Each tool (review, improve, ask, ...) has a single GPT-4 call, no more. We feel that this is critical for realistic team usage - obtaining an answer quickly (~30 seconds) and affordably.
- Our [PR Compression strategy](https://pr-action-docs.khulnasoft.com/core-abilities/#pr-compression-strategy)  is a core ability that enables to effectively tackle both short and long PRs.
- Our JSON prompting strategy enables to have **modular, customizable tools**. For example, the '/review' tool categories can be controlled via the [configuration](pr_action/settings/configuration.toml) file. Adding additional categories is easy and accessible.
- We support **multiple git providers** (GitHub, Gitlab, Bitbucket), **multiple ways** to use the tool (CLI, GitHub Action, GitHub App, Docker, ...), and **multiple models** (GPT-4, GPT-3.5, Anthropic, Cohere, Llama2).


## Data privacy

### Self-hosted PR-Action

- If you host PR-Action with your OpenAI API key, it is between you and OpenAI. You can read their API data privacy policy here:
https://openai.com/enterprise-privacy

### KhulnaSoft-hosted PR-Action Pro 💎

- When using PR-Action Pro 💎, hosted by KhulnaSoft, we will not store any of your data, nor will we use it for training. You will also benefit from an OpenAI account with zero data retention.

- For certain clients, KhulnaSoft-hosted PR-Action Pro will use KhulnaSoft’s proprietary models — if this is the case, you will be notified.

- No passive collection of Code and Pull Requests’ data — PR-Action will be active only when you invoke it, and it will then extract and analyze only data relevant to the executed command and queried pull request.

### PR-Action Chrome extension

- The [PR-Action Chrome extension](https://chromewebstore.google.com/detail/pr-action-chrome-extension/ephlnjeghhogofkifjloamocljapahnl) serves solely to modify the visual appearance of a GitHub PR screen. It does not transmit any user's repo or pull request code. Code is only sent for processing when a user submits a GitHub comment that activates a PR-Action tool, in accordance with the standard privacy policy of PR-Action.

## Links

[![Join our Discord community](https://raw.githubusercontent.com/Pr-action/khulnasoft-vscode-release/main/media/docs/Joincommunity.png)](https://discord.gg/kG35uSHDBc)

- Discord community: https://discord.gg/kG35uSHDBc
- KhulnaSoft site: https://khulnasoft.com
- Blog: https://www.khulnasoft.com/blog/
- Troubleshooting: https://www.khulnasoft.com/blog/technical-faq-and-troubleshooting/
- Support: support@khulnasoft.com
