def generate_latex_table(data):
    header = data[0]
    body = data[1:]
    latex = "\\begin{table}[h!]\n\\centering\n\\begin{tabular}{" + "l" * len(header) + "}\n\\hline\n"
    latex += " & ".join(header) + " \\\\\\hline\n"
    for row in body:
        latex += " & ".join(row) + " \\\\\\hline\n"
    latex += "\\end{tabular}\n\\end{table}"
    return latex

