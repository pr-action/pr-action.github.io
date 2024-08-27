FROM python:3.12.3 AS base

WORKDIR /app
ADD pyproject.toml .
ADD requirements.txt .
RUN pip install . && rm pyproject.toml requirements.txt
ENV PYTHONPATH=/app

FROM base AS github_app
ADD pr_action pr_action
CMD ["python", "-m", "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "pr_action/servers/gunicorn_config.py", "--forwarded-allow-ips", "*", "pr_action.servers.github_app:app"]

FROM base AS bitbucket_app
ADD pr_action pr_action
CMD ["python", "pr_action/servers/bitbucket_app.py"]

FROM base AS bitbucket_server_webhook
ADD pr_action pr_action
CMD ["python", "pr_action/servers/bitbucket_server_webhook.py"]

FROM base AS github_polling
ADD pr_action pr_action
CMD ["python", "pr_action/servers/github_polling.py"]

FROM base AS gitlab_webhook
ADD pr_action pr_action
CMD ["python", "pr_action/servers/gitlab_webhook.py"]

FROM base AS azure_devops_webhook
ADD pr_action pr_action
CMD ["python", "pr_action/servers/azuredevops_server_webhook.py"]

FROM base AS test
ADD requirements-dev.txt .
RUN pip install -r requirements-dev.txt && rm requirements-dev.txt
ADD pr_action pr_action
ADD tests tests

FROM base AS cli
ADD pr_action pr_action
ENTRYPOINT ["python", "pr_action/cli.py"]
