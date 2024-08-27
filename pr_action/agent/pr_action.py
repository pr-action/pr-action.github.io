import shlex
from functools import partial

from pr_action.algo.ai_handlers.base_ai_handler import BaseAiHandler
from pr_action.algo.ai_handlers.litellm_ai_handler import LiteLLMAIHandler

from pr_action.algo.utils import update_settings_from_args
from pr_action.config_loader import get_settings
from pr_action.git_providers.utils import apply_repo_settings
from pr_action.log import get_logger
from pr_action.tools.pr_add_docs import PRAddDocs
from pr_action.tools.pr_code_suggestions import PRCodeSuggestions
from pr_action.tools.pr_config import PRConfig
from pr_action.tools.pr_description import PRDescription
from pr_action.tools.pr_generate_labels import PRGenerateLabels
from pr_action.tools.pr_help_message import PRHelpMessage
from pr_action.tools.pr_information_from_user import PRInformationFromUser
from pr_action.tools.pr_line_questions import PR_LineQuestions
from pr_action.tools.pr_questions import PRQuestions
from pr_action.tools.pr_reviewer import PRReviewer
from pr_action.tools.pr_similar_issue import PRSimilarIssue
from pr_action.tools.pr_update_changelog import PRUpdateChangelog

command2class = {
    "auto_review": PRReviewer,
    "answer": PRReviewer,
    "review": PRReviewer,
    "review_pr": PRReviewer,
    "reflect": PRInformationFromUser,
    "reflect_and_review": PRInformationFromUser,
    "describe": PRDescription,
    "describe_pr": PRDescription,
    "improve": PRCodeSuggestions,
    "improve_code": PRCodeSuggestions,
    "ask": PRQuestions,
    "ask_question": PRQuestions,
    "ask_line": PR_LineQuestions,
    "update_changelog": PRUpdateChangelog,
    "config": PRConfig,
    "settings": PRConfig,
    "help": PRHelpMessage,
    "similar_issue": PRSimilarIssue,
    "add_docs": PRAddDocs,
    "generate_labels": PRGenerateLabels,
}

commands = list(command2class.keys())


class PRAction:
    def __init__(self, ai_handler: partial[BaseAiHandler,] = LiteLLMAIHandler):
        self.ai_handler = ai_handler  # will be initialized in run_action
        self.forbidden_cli_args = ['enable_auto_approval']

    async def handle_request(self, pr_url, request, notify=None) -> bool:
        # First, apply repo specific settings if exists
        apply_repo_settings(pr_url)

        # Then, apply user specific settings if exists
        if isinstance(request, str):
            request = request.replace("'", "\\'")
            lexer = shlex.shlex(request, posix=True)
            lexer.whitespace_split = True
            action, *args = list(lexer)
        else:
            action, *args = request

        if args:
            for forbidden_arg in self.forbidden_cli_args:
                for arg in args:
                    if forbidden_arg in arg:
                        get_logger().error(
                            f"CLI argument for param '{forbidden_arg}' is forbidden. Use instead a configuration file."
                        )
                        return False
        args = update_settings_from_args(args)

        action = action.lstrip("/").lower()
        if action not in command2class:
            get_logger().debug(f"Unknown command: {action}")
            return False
        with get_logger().contextualize(command=action, pr_url=pr_url):
            get_logger().info("PR-Action request handler started", analytics=True)
            if action == "reflect_and_review":
                get_settings().pr_reviewer.ask_and_reflect = True
            if action == "answer":
                if notify:
                    notify()
                await PRReviewer(pr_url, is_answer=True, args=args, ai_handler=self.ai_handler).run()
            elif action == "auto_review":
                await PRReviewer(pr_url, is_auto=True, args=args, ai_handler=self.ai_handler).run()
            elif action in command2class:
                if notify:
                    notify()

                await command2class[action](pr_url, ai_handler=self.ai_handler, args=args).run()
            else:
                return False
            return True
