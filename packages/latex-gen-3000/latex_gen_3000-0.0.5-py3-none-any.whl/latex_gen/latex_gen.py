import typing as tp

def generate_latex_document(latex_code: str):
    return """
\\documentclass{{article}}
\\begin{{document}}
{latex_code}
\\end{document}
""".format(latex_code=latex_code)


def generate_latex_table(data: tp.List[tp.List[str]]):
    num_cols = max(len(row) for row in data)

    latex_code = "\\begin{tabular}{|" + "|".join(["c"] * num_cols) + "|}\n"

    for row in data:
        latex_code += " & ".join(str(cell) for cell in row)
        latex_code += " \\\\\n"

    latex_code += "\\end{tabular}\n"

    return latex_code


def generate_latex_image(image_path: str):
    return "\\includegraphics{" + image_path + "}"
