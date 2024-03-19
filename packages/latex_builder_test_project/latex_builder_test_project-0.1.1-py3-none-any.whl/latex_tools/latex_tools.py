def generate_latex_table(matrix):
    table_begin = "\\begin{tabular}{|" + "l|" * len(matrix[0]) + "}\n\\hline\n"
    table_body = ""
    for row in matrix:
        table_body += " & ".join(map(str, row)) + " \\\\\n\\hline\n"
    table_end = "\\end{tabular}\n"
    return table_begin + table_body + table_end


def generate_latex_image(image_path, caption="Image", label="fig:image"):
    return f"""
\\begin{{figure}}[ht]
\\centering
\\includegraphics[width=0.8\\textwidth]{{{image_path}}}
\\caption{{{caption}}}
\\label{{{label}}}
\\end{{figure}}
"""


def generate_latex(matrix, image_path):
    preamble = """
\\documentclass{article}
\\usepackage[T2A]{fontenc}
\\usepackage[utf8]{inputenc}
\\usepackage[russian]{babel}
\\usepackage{graphicx}
\\begin{document}
"""
    table_code = generate_latex_table(matrix)
    image_code = generate_latex_image(image_path, "Пример изображения", "fig:example")
    end_document = "\\end{document}"
    
    return preamble + table_code + image_code + end_document