# PR-Action

[![GitHub license](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://github.com/khulnasoft/pr-action/blob/main/LICENSE)
[![Static Badge](https://img.shields.io/badge/Chrome-Extension-violet)](https://chromewebstore.google.com/detail/pr-action-chrome-extension/ephlnjeghhogofkifjloamocljapahnl)
[![Static Badge](https://img.shields.io/badge/Code-Benchmark-blue)](https://khulnasoft.github.io/pr-action/finetuning_benchmark/)
[![Discord](https://badgen.net/badge/icon/discord?icon=discord&label&color=purple)](https://discord.gg/NfDj6xsR)
[![Twitter](https://img.shields.io/twitter/follow/khulnasoft)](https://twitter.com/khulnasoft)
    <a href="https://github.com/khulnasoft/pr-action/commits/main">
    <img alt="GitHub" src="https://img.shields.io/github/last-commit/khulnasoft/pr-action/main?style=for-the-badge" height="20">
    </a>
</div>

### [Documentation](https://khulnasoft.github.io/pr-action/)
- See the [Installation Guide](https://khulnasoft.github.io/pr-action/installation/) for instructions on installing PR-Action on different platforms.

- See the [Usage Guide](https://khulnasoft.github.io/pr-action/usage-guide/) for instructions on running PR-Action tools via different interfaces, such as CLI, PR Comments, or by automatically triggering them when a new PR is opened.

- See the [Tools Guide](https://khulnasoft.github.io/pr-action/tools/) for a detailed description of the different tools, and the available configurations for each tool.


## Table of Contents
- [Table of Contents](#table-of-contents)
- [News and Updates](#news-and-updates)
  - [May 31, 2024](#may-31-2024)
  - [May 23, 2024](#may-23-2024)
  - [May 21, 2024](#may-21-2024)
- [Overview](#overview)
- [Example results](#example-results)
- [Try it now](#try-it-now)
- [PR-Action Pro 💎](#pr-action-pro-)
- [Why use PR-Action?](#why-use-pr-action)
- [Data privacy](#data-privacy)
  - [Self-hosted PR-Action](#self-hosted-pr-action)
  - [KhulnaSoft-hosted PR-Action Pro 💎](#khulnasoft-hosted-pr-action-pro-)
  - [PR-Action Chrome extension](#pr-action-chrome-extension)
- [Links](#links)
  
## News and Updates

### May 31, 2024

Check out the new [**PR-Action Code Fine-tuning Benchmark**](https://khulnasoft.github.io/pr-action/finetuning_benchmark/)

### May 23, 2024

We released a new version of [PR-Action Chrome extension](https://chromewebstore.google.com/detail/pr-action-chrome-extension/ephlnjeghhogofkifjloamocljapahnl), with two new features:

- PR-Action filters 🎨
- Code suggestions interactions 🔗

See more [here](https://www.youtube.com/watch?v=v9bJ1frtPcg)


### May 21, 2024
Check out KhulnaSoft new project, [**Coverage-Ai**](https://github.com/KhulnaSoft/coverage-ai), that can automatically generate qualified tests to enhance existing test suites, aiming to increase code and behavior coverage efficiently.


## Overview
<div style="text-align:left;">

Supported commands per platform:

|       |                                                                                                         | GitHub             | Gitlab             | Bitbucket          | Azure DevOps       |
|-------|---------------------------------------------------------------------------------------------------------|:--------------------:|:--------------------:|:--------------------:|:--------------------:|
| TOOLS | Review                                                                                                  | ✅ | ✅ | ✅ | ✅ |
|       | ⮑ Incremental                                                                                           | ✅ |                    |                    |                    |
|       | ⮑ [SOC2 Compliance](https://khulnasoft.github.io/pr-action/tools/review/#soc2-ticket-compliance) 💎            | ✅ | ✅ | ✅ | ✅ |
|       | Describe                                                                                                | ✅ | ✅ | ✅ | ✅ |
|       | ⮑ [Inline File Summary](https://khulnasoft.github.io/pr-action/tools/describe#inline-file-summary) 💎          | ✅ |                    |                    |                    |
|       | Improve                                                                                                 | ✅ | ✅ | ✅ | ✅ |
|       | ⮑ Extended                                                                                              | ✅ | ✅ | ✅ | ✅ |
|       | Ask                                                                                                     | ✅ | ✅ | ✅ | ✅ |
|       | ⮑ [Ask on code lines](https://khulnasoft.github.io/pr-action/tools/ask#ask-lines)                              | ✅ | ✅ |                    |                    |
|       | [Custom Prompt](https://khulnasoft.github.io/pr-action/tools/custom_prompt/) 💎                                | ✅ | ✅ | ✅ | ✅ |
|       | [Test](https://khulnasoft.github.io/pr-action/tools/test/) 💎                                                  | ✅ | ✅ |                    | ✅ |
|       | Reflect and Review                                                                                      | ✅ | ✅ | ✅ | ✅ |
|       | Update CHANGELOG.md                                                                                     | ✅ | ✅ | ✅ | ✅ |
|       | Find Similar Issue                                                                                      | ✅ |                    |                    |                    |
|       | [Add PR Documentation](https://khulnasoft.github.io/pr-action/tools/documentation/) 💎                         | ✅ | ✅ |                   | ✅ |
|       | [Custom Labels](https://khulnasoft.github.io/pr-action/tools/custom_labels/) 💎                                | ✅ | ✅ |                    | ✅ |
|       | [Analyze](https://khulnasoft.github.io/pr-action/tools/analyze/) 💎                                            | ✅ | ✅ |                    | ✅ |
|       | [CI Feedback](https://khulnasoft.github.io/pr-action/tools/ci_feedback/) 💎                                    | ✅ |                    |                    |                    |
|       | [Similar Code](https://khulnasoft.github.io/pr-action/tools/similar_code/) 💎                                  | ✅ |                    |                    |                    |
|       |                                                                                                         |                    |                    |                    |                    |
| USAGE | CLI                                                                                                     | ✅ | ✅ | ✅ | ✅ |
|       | App / webhook                                                                                           | ✅ | ✅ | ✅ | ✅ |
|       | Tagging bot                                                                                             | ✅ |                    |                    |                    |
|       | Actions                                                                                                 | ✅ |                    | ✅ |                    |
|       |                                                                                                         |                    |                    |                    |                    |
| CORE  | PR compression                                                                                          | ✅ | ✅ | ✅ | ✅ |
|       | Repo language prioritization                                                                            | ✅ | ✅ | ✅ | ✅ |
|       | Adaptive and token-aware file patch fitting                                                             | ✅ | ✅ | ✅ | ✅ |
|       | Multiple models support                                                                                 | ✅ | ✅ | ✅ | ✅ |
|       | [Static code analysis](https://khulnasoft.github.io/pr-action/core-abilities/#static-code-analysis) 💎         | ✅ | ✅ | ✅ | ✅ |
|       | [Global and wiki configurations](https://khulnasoft.github.io/pr-action/usage-guide/configuration_options/) 💎 | ✅ | ✅ | ✅ | ✅ |
|       | [PR interactive actions](https://www.khulnasoft.com/images/pr_action/pr-actions.mp4) 💎                       | ✅ |                    |                    |                    |
- 💎 means this feature is available only in [PR-Action Pro](https://www.khulnasoft.com/pricing/)

[//]: # (- Support for additional git providers is described in [here]&#40;./docs/Full_environments.md&#41;)
___

‣ **Auto Description ([`/describe`](https://khulnasoft.github.io/pr-action/tools/describe/))**: Automatically generating PR description - title, type, summary, code walkthrough and labels.
\
‣ **Auto Review ([`/review`](https://khulnasoft.github.io/pr-action/tools/review/))**: Adjustable feedback about the PR, possible issues, security concerns, review effort and more.
\
‣ **Code Suggestions ([`/improve`](https://khulnasoft.github.io/pr-action/tools/improve/))**: Code suggestions for improving the PR.
\
‣ **Question Answering ([`/ask ...`](https://khulnasoft.github.io/pr-action/tools/ask/))**: Answering free-text questions about the PR.
\
‣ **Update Changelog ([`/update_changelog`](https://khulnasoft.github.io/pr-action/tools/update_changelog/))**: Automatically updating the CHANGELOG.md file with the PR changes.
\
‣ **Find Similar Issue ([`/similar_issue`](https://khulnasoft.github.io/pr-action/tools/similar_issues/))**: Automatically retrieves and presents similar issues.
\
‣ **Add Documentation 💎  ([`/add_docs`](https://khulnasoft.github.io/pr-action/tools/documentation/))**: Generates documentation to methods/functions/classes that changed in the PR.
\
‣ **Generate Custom Labels 💎 ([`/generate_labels`](https://khulnasoft.github.io/pr-action/tools/custom_labels/))**: Generates custom labels for the PR, based on specific guidelines defined by the user.
\
‣ **Analyze 💎 ([`/analyze`](https://khulnasoft.github.io/pr-action/tools/analyze/))**: Identify code components that changed in the PR, and enables to interactively generate tests, docs, and code suggestions for each component.
\
‣ **Custom Prompt 💎 ([`/custom_prompt`](https://khulnasoft.github.io/pr-action/tools/custom_prompt/))**: Automatically generates custom suggestions for improving the PR code, based on specific guidelines defined by the user.
\
‣ **Generate Tests 💎 ([`/test component_name`](https://khulnasoft.github.io/pr-action/tools/test/))**: Generates unit tests for a selected component, based on the PR code changes.
\
‣ **CI Feedback 💎 ([`/checks ci_job`](https://khulnasoft.github.io/pr-action/tools/ci_feedback/))**: Automatically generates feedback and analysis for a failed CI job.
\
‣ **Similar Code 💎 ([`/find_similar_component`](https://khulnasoft.github.io/pr-action/tools/similar_code/))**: Retrieves the most similar code components from inside the organization's codebase, or from open-source code.
___

## Try it now

Try the GPT-4 powered PR-Action instantly on _your public GitHub repository_. Just mention `@KhulnaSoft` and add the desired command in any PR comment. The agent will generate a response based on your command.
For example, add a comment to any pull request with the following text:
```
@KhulnaSoft /review
```
and the agent will respond with a review of your PR


To set up your own PR-Action, see the [Installation](https://khulnasoft.github.io/pr-action/installation/) section below.
Note that when you set your own PR-Action or use KhulnaSoft hosted PR-Action, there is no need to mention `@KhulnaSoft ...`. Instead, directly start with the command, e.g., `/ask ...`.

---

[//]: # (## Installation)

[//]: # (To use your own version of PR-Action, you first need to acquire two tokens:)

[//]: # ()
[//]: # (1. An OpenAI key from [here]&#40;https://platform.openai.com/&#41;, with access to GPT-4.)

[//]: # (2. A GitHub personal access token &#40;classic&#41; with the repo scope.)

[//]: # ()
[//]: # (There are several ways to use PR-Action:)

[//]: # ()
[//]: # (**Locally**)

[//]: # (- [Using pip package]&#40;https://khulnasoft.github.io/pr-action/installation/locally/#using-pip-package&#41;)

[//]: # (- [Using Docker image]&#40;https://khulnasoft.github.io/pr-action/installation/locally/#using-docker-image&#41;)

[//]: # (- [Run from source]&#40;https://khulnasoft.github.io/pr-action/installation/locally/#run-from-source&#41;)

[//]: # ()
[//]: # (**GitHub specific methods**)

[//]: # (- [Run as a GitHub Action]&#40;https://khulnasoft.github.io/pr-action/installation/github/#run-as-a-github-action&#41;)

[//]: # (- [Run as a GitHub App]&#40;https://khulnasoft.github.io/pr-action/installation/github/#run-as-a-github-app&#41;)

[//]: # ()
[//]: # (**GitLab specific methods**)

[//]: # (- [Run a GitLab webhook server]&#40;https://khulnasoft.github.io/pr-action/installation/gitlab/&#41;)

[//]: # ()
[//]: # (**BitBucket specific methods**)

[//]: # (- [Run as a Bitbucket Pipeline]&#40;https://khulnasoft.github.io/pr-action/installation/bitbucket/&#41;)

## PR-Action Pro 💎
[PR-Action Pro](https://www.khulnasoft.com/pricing/) is a hosted version of PR-Action, provided by KhulnaSoft. It is available for a monthly fee, and provides the following benefits:
1. **Fully managed** - We take care of everything for you - hosting, models, regular updates, and more. Installation is as simple as signing up and adding the PR-Action app to your GitHub\GitLab\BitBucket repo.
2. **Improved privacy** - No data will be stored or used to train models. PR-Action Pro will employ zero data retention, and will use an OpenAI account with zero data retention.
3. **Improved support** - PR-Action Pro users will receive priority support, and will be able to request new features and capabilities.
4. **Extra features** -In addition to the benefits listed above, PR-Action Pro will emphasize more customization, and the usage of static code analysis, in addition to LLM logic, to improve results. 
See [here](https://khulnasoft.github.io/pr-action/#pr-action-pro) for a list of features available in PR-Action Pro.



## Why use PR-Action?

A reasonable question that can be asked is: `"Why use PR-Action? What makes it stand out from existing tools?"`

Here are some advantages of PR-Action:

- We emphasize **real-life practical usage**. Each tool (review, improve, ask, ...) has a single GPT-4 call, no more. We feel that this is critical for realistic team usage - obtaining an answer quickly (~30 seconds) and affordably.
- Our [PR Compression strategy](https://khulnasoft.github.io/pr-action/core-abilities/#pr-compression-strategy)  is a core ability that enables to effectively tackle both short and long PRs.
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

[![Join our Discord community](https://raw.githubusercontent.com/KhulnaSoft/khulnasoft-vscode-release/main/media/docs/Joincommunity.png)](https://discord.gg/kG35uSHDBc)

- Discord community: https://discord.gg/NfDj6xsR
- KhulnaSoft site: https://khulnasoft.com
- Blog: https://www.khulnasoft.com/blog/
- Troubleshooting: https://www.khulnasoft.com/blog/technical-faq-and-troubleshooting/
- Support: support@khulnasoft.com
