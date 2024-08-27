## PR-Action chrome extension
[PR-Action Chrome extension](https://chromewebstore.google.com/detail/pr-action-chrome-extension/ephlnjeghhogofkifjloamocljapahnl) is a collection of tools that integrates seamlessly with your GitHub environment, aiming to enhance your PR-Action usage experience, and providing additional features.

## Features

### PR Chat

The PR-Chat feature allows to freely chat with your PR code, within your GitHub environment.
It will seamlessly add the PR code as context to your chat session, and provide AI-powered feedback.

To enable private chat, simply install the PR-Action Chrome extension. After installation, each PR's file-changed tab will include a chat box, where you may ask questions about your code.
This chat session is **private**, and won't be visible to other users.

All open-source repositories are supported.
For private repositories, you will also need to install PR-Action Pro, After installation, make sure to open at least one new PR to fully register your organization. Once done, you can chat with both new and existing PRs across all installed repositories.

#### Chat security and privacy
 
We take your code's security and privacy seriously:

- The Chrome extension does not send your code to external servers.
- For private repositories, we will first validate the user's identity and permissions. After authentication, we generate responses using the existing PR-Action Pro integration.


<img src="https://khulnasoft.com/images/pr_action/pr_chat1.png" width="768">
<img src="https://khulnasoft.com/images/pr_action/pr_chat2.png" width="768">


### Toolbar extension
With PR-Action Chrome extension, it's [easier than ever](https://www.youtube.com/watch?v=gT5tli7X4H4) to interactively configure and experiment with the different tools and configuration options.

After you found the setup that works for you, you can also easily export it as a persistent configuration file, and use it for automatic commands.

<img src="https://khulnasoft.com/images/pr_action/toolbar1.png" width="512">

<img src="https://khulnasoft.com/images/pr_action/toolbar2.png" width="512">

### PR-Action filters

PR-Action filters is a sidepanel option. that allows you to filter different message in the conversation tab.

For example, you can choose to present only message from PR-Action, or filter those messages, focusing only on user's comments.

<img src="https://khulnasoft.com/images/pr_action/pr_action_filters1.png" width="256">

<img src="https://khulnasoft.com/images/pr_action/pr_action_filters2.png" width="256">


### Enhanced code suggestions

PR-Action Chrome extension adds the following capabilities to code suggestions tool's comments:

- Auto-expand the table when you are viewing a code block, to avoid clipping.
- Adding a "quote-and-reply" button, that enables to address and comment on a specific suggestion (for example, asking the author to fix the issue)


<img src="https://khulnasoft.com/images/pr_action/chrome_extension_code_suggestion1.png" width="512">

<img src="https://khulnasoft.com/images/pr_action/chrome_extension_code_suggestion2.png" width="512">

## Installation

Go to the marketplace and install the extension:
[PR-Action Chrome Extension](https://chromewebstore.google.com/detail/pr-action-chrome-extension/ephlnjeghhogofkifjloamocljapahnl)

## Pre-requisites

The PR-Action Chrome extension will work on any repo where you have previously [installed PR-Action](https://pr-action-docs.khulnasoft.com/installation/).

## Data privacy and security

The PR-Action Chrome extension only modifies the visual appearance of a GitHub PR screen. It does not transmit any user's repo or pull request code. Code is only sent for processing when a user submits a GitHub comment that activates a PR-Action tool, in accordance with the standard privacy policy of PR-Action.
