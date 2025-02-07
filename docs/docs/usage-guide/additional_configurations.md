## Show possible configurations
The possible configurations of pr-action are stored in [here](https://github.com/Pr-action/pr-action/blob/main/pr_action/settings/configuration.toml).
In the [tools](https://pr-action.github.io/tools/) page you can find explanations on how to use these configurations for each tool.

To print all the available configurations as a comment on your PR, you can use the following command:
```
/config
```

![possible_config1](https://khulnasoft.com/images/pr_action/possible_config1.png){width=512}


To view the **actual** configurations used for a specific tool, after all the user settings are applied, you can add for each tool a `--config.output_relevant_configurations=true` suffix.
For example:
```
/improve --config.output_relevant_configurations=true
```
Will output an additional field showing the actual configurations used for the `improve` tool.

![possible_config2](https://khulnasoft.com/images/pr_action/possible_config2.png){width=512}


## Ignoring files from analysis

In some cases, you may want to exclude specific files or directories from the analysis performed by KhulnaSoft PR-Action. This can be useful, for example, when you have files that are generated automatically or files that shouldn't be reviewed, like vendor code.

You can ignore files or folders using the following methods:
 - `IGNORE.GLOB`
 - `IGNORE.REGEX`

which you can edit to ignore files or folders based on glob or regex patterns.

### Example usage

Let's look at an example where we want to ignore all files with `.py` extension from the analysis.

To ignore Python files in a PR with online usage, comment on a PR:
`/review --ignore.glob="['*.py']"`


To ignore Python files in all PRs using `glob` pattern, set in a configuration file:
```
[ignore]
glob = ['*.py']
```

And to ignore Python files in all PRs using `regex` pattern, set in a configuration file:
```
[regex]
regex = ['.*\.py$']
```

## Extra instructions

All PR-Action tools have a parameter called `extra_instructions`, that enables to add free-text extra instructions. Example usage:
```
/update_changelog --pr_update_changelog.extra_instructions="Make sure to update also the version ..."
```

## Working with large PRs

The default mode of KhulnaSoft is to have a single call per tool, using GPT-4, which has a token limit of 8000 tokens.
This mode provides a very good speed-quality-cost tradeoff, and can handle most PRs successfully.
When the PR is above the token limit, it employs a [PR Compression strategy](../core-abilities/index.md).

However, for very large PRs, or in case you want to emphasize quality over speed and cost, there are two possible solutions:
1) [Use a model](https://pr-action.github.io/Docs-PR-Action/usage-guide/#changing-a-model) with larger context, like GPT-32K, or claude-100K. This solution will be applicable for all the tools.
2) For the `/improve` tool, there is an ['extended' mode](https://pr-action.github.io/Docs-PR-Action/tools/#improve) (`/improve --extended`),
which divides the PR into chunks, and processes each chunk separately. With this mode, regardless of the model, no compression will be done (but for large PRs, multiple model calls may occur)



## Patch Extra Lines

By default, around any change in your PR, git patch provides three lines of context above and below the change.
```
@@ -12,5 +12,5 @@ def func1():
 code line that already existed in the file...
 code line that already existed in the file...
 code line that already existed in the file....
-code line that was removed in the PR
+new code line added in the PR
 code line that already existed in the file...
 code line that already existed in the file...
 code line that already existed in the file...
```

PR-Action will try to increase the number of lines of context, via the parameter:
```
[config]
patch_extra_lines_before=3
patch_extra_lines_after=1
```

Increasing this number provides more context to the model, but will also increase the token budget, and may overwhelm the model with too much information, unrelated to the actual PR code changes.

If the PR is too large (see [PR Compression strategy](https://github.com/Pr-action/pr-action/blob/main/PR_COMPRESSION.md)), PR-Action may automatically set this number to 0, and will use the original git patch.


## Editing the prompts

The prompts for the various PR-Action tools are defined in the `pr_action/settings` folder.
In practice, the prompts are loaded and stored as a standard setting object.
Hence, editing them is similar to editing any other configuration value - just place the relevant key in `.pr_action.toml`file, and override the default value.

For example, if you want to edit the prompts of the [describe](https://github.com/Pr-action/pr-action/blob/main/pr_action/settings/pr_description_prompts.toml) tool, you can add the following to your `.pr_action.toml` file:
```
[pr_description_prompt]
system="""
...
"""
user="""
...
"""
```
Note that the new prompt will need to generate an output compatible with the relevant [post-process function](https://github.com/Pr-action/pr-action/blob/main/pr_action/tools/pr_description.py#L137).

## Integrating with Logging Observability Platforms

Various logging observability tools can be used out-of-the box when using the default LiteLLM AI Handler. Simply configure the LiteLLM callback settings in `configuration.toml` and set environment variables according to the LiteLLM [documentation](https://docs.litellm.ai/docs/).

For example, to use [LangSmith](https://www.langchain.com/langsmith) you can add the following to your `configuration.toml` file:
```
[litellm]
enable_callbacks = true
success_callback = ["langsmith"]
failure_callback = ["langsmith"]
service_callback = []
```

Then set the following environment variables:

```
LANGSMITH_API_KEY=<api_key>
LANGSMITH_PROJECT=<project>
LANGSMITH_BASE_URL=<url>
```

## Ignoring automatic commands in PRs

In some cases, you may want to automatically ignore specific PRs . PR-Action enables you to ignore PR with a specific title, or from/to specific branches (regex matching).

To ignore PRs with a specific title such as "[Bump]: ...", you can add the following to your `configuration.toml` file:

```
[config]
ignore_pr_title = ["\\[Bump\\]"]
```

Where the `ignore_pr_title` is a list of regex patterns to match the PR title you want to ignore. Default is `ignore_pr_title = ["^\\[Auto\\]", "^Auto"]`.


To ignore PRs from specific source or target branches, you can add the following to your `configuration.toml` file:

```
[config]
ignore_pr_source_branches = ['develop', 'main', 'master', 'stage']
ignore_pr_target_branches = ["qa"]
```

Where the `ignore_pr_source_branches` and `ignore_pr_target_branches` are lists of regex patterns to match the source and target branches you want to ignore.
They are not mutually exclusive, you can use them together or separately.
