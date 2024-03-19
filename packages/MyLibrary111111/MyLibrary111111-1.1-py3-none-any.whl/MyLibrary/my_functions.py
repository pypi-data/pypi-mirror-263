def generate_latex_row(row: str) -> str:
    return " & ".join(map(str, row)) + " \\\\\n"


def generate_latex_table(array: list) -> str:
    if not array:
        return ""

    num_rows = len(array)
    num_cols = len(array[0])

    if num_rows == 0 or num_cols == 0:
        return ""

    return ("\\begin{tabular}{|" + "|".join([" c "] * num_cols) + "|}\n"
            + "\\hline\n"
            + "".join(map(generate_latex_row, array))
            + "\\hline\n"
            + "\\end{tabular}\n"
            )


def generate_image(img_path: str, scale: float) -> str:
    return ("\\begin{center}"
            f"\\includegraphics[scale={scale}]{{{img_path}}}\n"
            "\\end{center}\n"
            )


def generate_header(title: str, author: str, data: str) -> str:
    return (
        "\\documentclass{article}\n"
        "\\usepackage[utf8]{inputenc}\n"
        "\\usepackage{graphicx}\n\n"
        f"\\title{{{title}}}\n"
        f"\\author{{{author}}}\n"
        f"\\date{{{data}}}\n"
        "\\begin{document}\n\n"
        "\\maketitle\n\n"
    )


def generate_footer() -> str:
    return "\\end{document}"
