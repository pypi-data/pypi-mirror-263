import subprocess
from typing import Iterable, Optional


def latex_scope(name, params=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            func_output = func(*args, **kwargs)
            if params:
                return f"\\begin{{{name}}}{params}\n{func_output}\n\\end{{{name}}}"
            else:
                return f"\\begin{{{name}}}\n{func_output}\n\\end{{{name}}}"

        return wrapper

    return decorator


def gen_document(packages: Optional[Iterable[str]] = None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = []
            res += ["\\documentclass{article}"]
            if packages:
                res += [f"\\usepackage{{{i}}}" for i in packages]
            res += ["\\begin{document}"]
            func_output = func(*args, **kwargs)
            res += [func_output]
            res += ["\\end{document}\n"]
            return '\n'.join(res)

        return wrapper

    return decorator


def generate_latex_table(data):
    return f"\\begin{{tabular}}{{{'c' * len(data[0])}}}\n" + \
        " \\\\\n".join(" & ".join(map(str, row)) for row in data) + " \\\\\n" + \
        f"\\end{{tabular}}"


@latex_scope('figure', '[h]')
def generate_latex_image(image_path, scale=1, caption=None):
    figure_content = f"\\includegraphics[scale={scale}]{{ \"{image_path}\" }}"
    if caption:
        figure_content += f"\\caption{{ {caption} }}"
    return figure_content
