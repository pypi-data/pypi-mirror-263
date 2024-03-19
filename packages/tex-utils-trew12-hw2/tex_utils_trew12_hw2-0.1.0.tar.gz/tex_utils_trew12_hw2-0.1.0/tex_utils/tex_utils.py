def generate_latex_table(data):
    latex_table = '\\begin{tabular}{' + '|c' * len(data[0]) + '|}\n\\hline\n'
    for row in data:
        latex_table += ' & '.join(map(str, row)) + '\\\\\n\\hline\n'
    latex_table += '\\end{tabular}'
    return latex_table


def generate_latex_image(image_path):
    return f'\\includegraphics[width=\\textwidth]{{{image_path}}}'


def generate_latex_document(*args):
    content = '\n'.join(args)
    return '\\documentclass{article}\n\\usepackage{graphicx}\n\\begin{document}\n' + content + '\n\\end{document}'
