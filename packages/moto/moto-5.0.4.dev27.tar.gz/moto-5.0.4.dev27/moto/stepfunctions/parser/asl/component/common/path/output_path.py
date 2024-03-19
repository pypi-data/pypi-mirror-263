from typing import Final, Optional

from moto.stepfunctions.parser.asl.component.eval_component import EvalComponent
from moto.stepfunctions.parser.asl.eval.environment import Environment
from moto.stepfunctions.parser.asl.utils.json_path import JSONPathUtils


class OutputPath(EvalComponent):
    DEFAULT_PATH: Final[str] = "$"

    output_path: Final[Optional[str]]

    def __init__(self, output_path: Optional[str]):
        self.output_path = output_path

    def _eval_body(self, env: Environment) -> None:
        if self.output_path is None:
            env.inp = dict()
        else:
            current_output = env.stack.pop()
            state_output = JSONPathUtils.extract_json(self.output_path, current_output)
            env.inp = state_output
