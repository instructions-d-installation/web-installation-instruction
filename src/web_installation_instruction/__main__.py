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

from jinja2 import Environment, Template, FileSystemLoader, select_autoescape

from installation_instruction.installation_instruction import InstallationInstruction
from installation_instruction.helpers import _split_string_at_delimiter


def main():
    src_path = os.path.dirname(os.path.realpath(__file__))
    template_path = f"{src_path}/template"

    with open("install.cfg", "r") as f:
        config_string = f.read()

    (_, template) = _split_string_at_delimiter(config_string)

    install = InstallationInstruction(config_string)
    schema = install.parse_schema()

    schema["__web_template__"] = template

    if not os.path.exists("public"):
        os.makedirs("public")
    else:
        if os.path.exists("public/index.html"):
            os.remove("public/index.html")

    env = Environment(
        loader=FileSystemLoader([template_path]),
        autoescape=select_autoescape()
    )

    index = env.get_template("index.html.jinja")

    result = index.render(schema)

    with open("public/index.html", "x") as f:
        f.write(result)


if __name__ == "__main__":
    main()