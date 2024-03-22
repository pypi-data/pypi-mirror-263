import ast
import io
import re

import black
from rich.console import Console
from rich.pretty import pprint

from servicefoundry import Application


def extract_class_names(code):
    tree = ast.parse(code)

    # Function to extract keywords from the AST
    def extract_class_names_from_ast_tree(node):
        keywords = set()
        for child_node in ast.iter_child_nodes(node):
            if isinstance(child_node, ast.Call):
                keywords.add(child_node.func.id)
            keywords.update(extract_class_names_from_ast_tree(child_node))
        return keywords

    # Get keywords from the main body of the code
    main_keywords = extract_class_names_from_ast_tree(tree)
    return main_keywords


def filter_enums(raw_str):
    # required to replace enums of format <AppProtocol.HTTP: 'http'> with 'http'
    pattern = r'<([a-zA-Z0-9_]+).[a-zA-Z0-9_]+: [\'"]([a-zA-Z0-9_]+)[\'"]>'
    replacement = r"'\2'"

    result = re.sub(pattern, replacement, raw_str)
    return result


def remove_none_type_fields(code):
    lines = code.split("\n")
    new_lines = [
        line
        for line in lines
        if not (line.endswith("=None") or line.endswith("=None,"))
    ]
    formatted_code = "\n".join(new_lines)
    return formatted_code


def remove_type_field(code):
    lines = code.split("\n")
    new_lines = [re.sub(r'^[ \t]*type="[^"]*",', "", line) for line in lines]
    return "\n".join(new_lines)


def add_deploy_line(code, workspace_fqn, application_type):
    deploy_line = f"{application_type}.deploy('workspace_fqn={workspace_fqn}')"
    return code + "\n" + deploy_line


def expand_to_str(obj):
    stream = io.StringIO()
    console = Console(file=stream, no_color=True, highlighter=None)
    pprint(obj, expand_all=True, console=console, indent_guides=False)
    return stream.getvalue()


def convert_deployment_config_to_python(workspace_fqn: str, deployment_config: dict):
    """
    Convert a deployment config to a python file that can be used to deploy to a workspace
    """
    application = Application.parse_obj(deployment_config)
    application_type = application.__root__.type

    # find raw str
    raw_str = expand_to_str(application.__root__)

    raw_str = f"{application_type} = " + raw_str

    # remove enums and replace them with values
    raw_str = filter_enums(raw_str)

    # add import statement of classes
    keywords = extract_class_names(raw_str)
    import_str = (
        "import logging\nfrom servicefoundry import "
        + ", ".join(keywords)
        + "\n"
        + "logging.basicConfig(level=logging.INFO)\n"
    )
    raw_str = import_str + "\n" + raw_str
    # remove None type fields
    formatted_str = remove_none_type_fields(raw_str)

    # remove type field
    formatted_str = remove_type_field(formatted_str)

    # add deploy line
    formatted_str = add_deploy_line(formatted_str, workspace_fqn, application_type)

    final_code_str = black.format_str(formatted_str, mode=black.FileMode())

    return final_code_str
