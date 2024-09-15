
After [installation](https://pr-action.khulnasoft.com/installation/), there are three basic ways to invoke KhulnaSoft PR-Action:

1. Locally running a CLI command
2. Online usage - by [commenting](https://github.com/Pr-action/pr-action/pull/229#issuecomment-1695021901) on a PR
3. Enabling PR-Action tools to run automatically when a new PR is opened


Specifically, CLI commands can be issued by invoking a pre-built [docker image](https://pr-action.khulnasoft.com/installation/locally/#using-docker-image), or by invoking a [locally cloned repo](https://pr-action.khulnasoft.com/installation/locally/#run-from-source).

For online usage, you will need to setup either a [GitHub App](https://pr-action.khulnasoft.com/installation/github/#run-as-a-github-app) or a [GitHub Action](https://pr-action.khulnasoft.com/installation/github/#run-as-a-github-action) (GitHub), a [GitLab webhook](https://pr-action.khulnasoft.com/installation/gitlab/#run-a-gitlab-webhook-server) (GitLab), or a [BitBucket App](https://pr-action.khulnasoft.com/installation/bitbucket/#run-using-khulnasoft-hosted-bitbucket-app) (BitBucket).
These platforms also enable to run PR-Action specific tools automatically when a new PR is opened, or on each push to a branch.

