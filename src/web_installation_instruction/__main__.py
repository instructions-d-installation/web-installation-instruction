# Copyright 2024 Adam McKellar, Kanushka Gupta, Timo Ege

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
from typing_extensions import Annotated

from jinja2 import Environment, Template, FileSystemLoader, select_autoescape
import typer

from installation_instruction.installation_instruction import InstallationInstruction
from installation_instruction.helpers import _split_string_at_delimiter


def main(
    input: Annotated[str, typer.Option("--input", "-i" , help="Path to config file.")] = "./install.cfg",
    output: Annotated[str, typer.Option("--output", "-o", help="Path to output directory.")] = "./public",
):
    src_path = os.path.dirname(os.path.realpath(__file__))
    template_path = f"{src_path}/template"

    with open(input, "r") as f:
        config_string = f.read()

    (_, template) = _split_string_at_delimiter(config_string)

    install = InstallationInstruction(config_string)
    schema = install.parse_schema()

    schema["__web_template__"] = template

    if not os.path.exists(output):
        os.makedirs(output)
    else:
        if os.path.exists(f"{output}/index.html"):
            os.remove(f"{output}/index.html")

    env = Environment(
        loader=FileSystemLoader([template_path]),
        autoescape=select_autoescape()
    )

    index = env.get_template("index.html.jinja")

    result = index.render(schema)

    with open(f"{output}/index.html", "x") as f:
        f.write(result)

def run_cli():
    typer.run(main)

if __name__ == "__main__":
    run_cli()