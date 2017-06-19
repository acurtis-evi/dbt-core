from __future__ import print_function

from dbt.logger import GLOBAL_LOGGER as logger
from dbt.runner import RunManager
from dbt.utils import NodeType
from dbt.node_runners import ModelRunner

import dbt.ui.printer


class RunTask:
    def __init__(self, args, project):
        self.args = args
        self.project = project

    def run(self):
        runner = RunManager(
            self.project, self.project['target-path'], self.args
        )

        query = {
            "include": self.args.models,
            "exclude": self.args.exclude,
            "resource_types": [NodeType.Model],
            "tags": set()
        }

        results = runner.run(query, ModelRunner)

        if results:
            dbt.ui.printer.print_run_end_messages(results)
