def generate_latex_table(data):
    latex_table = "\\documentclass{article}\n"
    latex_table += "\\begin{document}\n"
    latex_table += "\\begin{tabular}{|" + "c|"*len(data[0]) + "}\n"
    latex_table += "\\hline\n"
    for row in data:
        latex_table += " & ".join(str(item) for item in row) + "\\\\ \\hline\n"
    latex_table += "\\end{tabular}\n"
    latex_table += "\\end{document}"
    return latex_table

def generate_latex_figure(image_path, caption=""):
    latex_figure = "\\begin{figure}[h]\n"
    latex_figure += "\\centering\n"
    latex_figure += "\\includegraphics[width=0.5\\textwidth]{" + image_path + "}\n"
    if caption:
        latex_figure += "\\caption{" + caption + "}\n"
    latex_figure += "\\end{figure}"
    return latex_figure