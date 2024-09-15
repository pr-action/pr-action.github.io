## [Version 0.11] - 2023-12-07
- khulnasoft/pr-action:0.11
- khulnasoft/pr-action:0.11-github_app
- khulnasoft/pr-action:0.11-bitbucket-app
- khulnasoft/pr-action:0.11-gitlab_webhook
- khulnasoft/pr-action:0.11-github_polling
- khulnasoft/pr-action:0.11-github_action

### Added::Algo
- New section in `/describe` tool - [PR changes walkthrough](https://github.com/Pr-action/pr-action/pull/509)
- Improving PR Action [prompts](https://github.com/Pr-action/pr-action/pull/501)
- Persistent tools (`/review`, `/describe`) now send an [update message](https://github.com/Pr-action/pr-action/pull/499) after finishing
- Add Amazon Bedrock [support](https://github.com/Pr-action/pr-action/pull/483)

### Fixed
- Update [dependencies](https://github.com/Pr-action/pr-action/pull/503) in requirements.txt for Python 3.12


## [Version 0.10] - 2023-11-15
- khulnasoft/pr-action:0.10
- khulnasoft/pr-action:0.10-github_app
- khulnasoft/pr-action:0.10-bitbucket-app
- khulnasoft/pr-action:0.10-gitlab_webhook
- khulnasoft/pr-action:0.10-github_polling
- khulnasoft/pr-action:0.10-github_action

### Added::Algo
- Review tool now works with [persistent comments](https://github.com/Pr-action/pr-action/pull/451) by default
- Bitbucket now publishes review suggestions with [code links](https://github.com/Pr-action/pr-action/pull/428)
- Enabling to limit [max number of tokens](https://github.com/Pr-action/pr-action/pull/437/files)
- Support ['gpt-4-1106-preview'](https://github.com/Pr-action/pr-action/pull/437/files) model
- Support for Google's [Vertex AI](https://github.com/Pr-action/pr-action/pull/436)
- Implementing [thresholds](https://github.com/Pr-action/pr-action/pull/423) for incremental PR reviews
- Decoupled custom labels from [PR type](https://github.com/Pr-action/pr-action/pull/431)

### Fixed
- Fixed bug in [parsing quotes](https://github.com/Pr-action/pr-action/pull/446) in CLI
- Preserve [user-added labels](https://github.com/Pr-action/pr-action/pull/433) in pull requests
- Bug fixes in GitLab and BitBucket

## [Version 0.9] - 2023-10-29
- khulnasoft/pr-action:0.9
- khulnasoft/pr-action:0.9-github_app
- khulnasoft/pr-action:0.9-bitbucket-app
- khulnasoft/pr-action:0.9-gitlab_webhook
- khulnasoft/pr-action:0.9-github_polling
- khulnasoft/pr-action:0.9-github_action

### Added::Algo
- New tool - [generate_labels](https://github.com/Pr-action/pr-action/blob/main/docs/GENERATE_CUSTOM_LABELS.md)
- New ability to use [customize labels](https://github.com/Pr-action/pr-action/blob/main/docs/GENERATE_CUSTOM_LABELS.md#how-to-enable-custom-labels) on the `review` and `describe` tools.
- New tool - [add_docs](https://github.com/Pr-action/pr-action/blob/main/docs/ADD_DOCUMENTATION.md)
- GitHub Action: Can now use a `.pr_action.toml` file to control configuration parameters (see [Usage Guide](./Usage.md#working-with-github-action)).
- GitHub App: Added ability to trigger tools on [push events](https://github.com/Pr-action/pr-action/blob/main/Usage.md#github-app-automatic-tools-for-new-code-pr-push)
- Support custom domain URLs for Azure devops integration (see [link](https://github.com/Pr-action/pr-action/pull/381)).
- PR Description default mode is now in [bullet points](https://github.com/Pr-action/pr-action/blob/main/pr_action/settings/configuration.toml#L35).

### Added::Documentation
Significant documentation updates (see [Installation Guide](https://github.com/Pr-action/pr-action/blob/main/INSTALL.md), [Usage Guide](https://github.com/Pr-action/pr-action/blob/main/Usage.md), and [Tools Guide](https://github.com/Pr-action/pr-action/blob/main/docs/TOOLS_GUIDE.md))

### Fixed
- Fixed support for BitBucket pipeline (see [link](https://github.com/Pr-action/pr-action/pull/386))
- Fixed a bug in `review -i` tool
- Added blacklist for specific file extensions in `add_docs` tool (see [link](https://github.com/Pr-action/pr-action/pull/385/))

## [Version 0.8] - 2023-09-27
- khulnasoft/pr-action:0.8
- khulnasoft/pr-action:0.8-github_app
- khulnasoft/pr-action:0.8-bitbucket-app
- khulnasoft/pr-action:0.8-gitlab_webhook
- khulnasoft/pr-action:0.8-github_polling
- khulnasoft/pr-action:0.8-github_action

### Added::Algo
- GitHub Action: Can control which tools will run automatically when a new PR is created. (see usage guide: https://github.com/Pr-action/pr-action/blob/main/Usage.md#working-with-github-action)
- Code suggestion tool: Will try to avoid an 'add comments' suggestion  (see https://github.com/Pr-action/pr-action/pull/327)

### Fixed
- Gitlab: Fixed a bug of improper usage of pr_id


## [Version 0.7] - 2023-09-20

### Docker Tags
- khulnasoft/pr-action:0.7
- khulnasoft/pr-action:0.7-github_app
- khulnasoft/pr-action:0.7-bitbucket-app
- khulnasoft/pr-action:0.7-gitlab_webhook
- khulnasoft/pr-action:0.7-github_polling
- khulnasoft/pr-action:0.7-github_action
 
### Added::Algo
- New tool /similar_issue - Currently on GitHub app and CLI: indexes the issues in the repo, find the most similar issues to the target issue.
- Describe markers: Empower the /describe tool with a templating capability (see more details in https://github.com/Pr-action/pr-action/pull/273).
- New feature in the /review tool - added an estimated effort estimation to the review (https://github.com/Pr-action/pr-action/pull/306).

### Added::Infrastructure
- Implementation of a GitLab webhook.
- Implementation of a BitBucket app.

### Fixed
- Protection against no code suggestions generated.
- Resilience to repositories where the languages cannot be automatically detected.
