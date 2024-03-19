def generation_document(data):
    BEGIN_DOCUMENT = "\\documentclass{article}\n\\usepackage{{graphicx}}\n\\begin{document}\n"
    END_DOCUMENT = "\\end{document}\n"

    return BEGIN_DOCUMENT + data + END_DOCUMENT


def generation_table(data):
    if len(data) == 0:
        return ""
    header = data[0]
    data = data[1:]

    c = "|" + "c|" * len(data[0])
    begin_tabular = "\\begin{tabular}{" + c + "}\n"
    end_tabular = "\\end{tabular}\n"
    headers = " & ".join(str(h) for h in header) + " \\\\\n"
    hline = "\\hline\n"

    rows = ""
    for row in data:
        rows += " & ".join(str(r) for r in row) + " \\\\\n"

    return begin_tabular + hline + headers + hline + rows + hline + end_tabular


def generation_picture(data):
    return "\n\\includegraphics[width=1" + "\\linewidth]{" + data + "}\n"
