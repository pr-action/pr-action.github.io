# Makefile for running pr-action

# Variables
IMAGE_NAME = khulnasoft/pr-action
VERSION = latest
GITHUB_TOKEN ?= <your token>
GITLAB_TOKEN ?= <your token>
BITBUCKET_TOKEN ?= <your token>
OPENAI_KEY ?= <your key>
GITLAB_URL ?= <your gitlab instance url>
PR_URL ?= <pr_url>
ISSUE_URL ?= <issue_url>
GIT_PROVIDER ?= github

# Docker commands
DOCKER_CMD = docker run --rm -it -e OPENAI.KEY=$(OPENAI_KEY) \
		-e GITHUB.USER_TOKEN=$(GITHUB_TOKEN) \
		-e CONFIG.GIT_PROVIDER=$(GIT_PROVIDER) \
		-e GITLAB.PERSONAL_ACCESS_TOKEN=$(GITLAB_TOKEN) \
		-e BITBUCKET.BEARER_TOKEN=$(BITBUCKET_TOKEN) \
		-e GITLAB.URL=$(GITLAB_URL) \
		$(IMAGE_NAME):$(VERSION) --pr_url $(PR_URL)

# Targets
all: review

review:
	$(DOCKER_CMD) review

ask:
	$(DOCKER_CMD) ask $(QUESTION)

describe:
	$(DOCKER_CMD) describe

improve:
	$(DOCKER_CMD) improve

add_docs:
	$(DOCKER_CMD) add_docs

generate_labels:
	$(DOCKER_CMD) generate_labels

similar_issue:
	$(DOCKER_CMD) similar_issue --issue_url $(ISSUE_URL)

# Run from source
run_from_source:
	git clone https://github.com/KhulnaSoft/pr-action.git
	cd pr-action && pip install -e .
	cp pr_action/settings/.secrets_template.toml pr_action/settings/.secrets.toml
	chmod 600 pr_action/settings/.secrets.toml
	@echo "Edit .secrets.toml file with your credentials."

cli:
	python3 -m pr_action.cli --pr_url $(PR_URL) review
	python3 -m pr_action.cli --pr_url $(PR_URL) ask $(QUESTION)
	python3 -m pr_action.cli --pr_url $(PR_URL) describe
	python3 -m pr_action.cli --pr_url $(PR_URL) improve
	python3 -m pr_action.cli --pr_url $(PR_URL) add_docs
	python3 -m pr_action.cli --pr_url $(PR_URL) generate_labels
	python3 -m pr_action.cli --issue_url $(ISSUE_URL) similar_issue

# Note: Add the pr_action folder to your PYTHONPATH if running from source
export_pythonpath:
	@echo "Add the pr_action folder to your PYTHONPATH"
	@echo "export PYTHONPATH=$$PYTHONPATH:$(CURDIR)/pr-action"

# Clean up
clean:
	rm -rf pr-action
