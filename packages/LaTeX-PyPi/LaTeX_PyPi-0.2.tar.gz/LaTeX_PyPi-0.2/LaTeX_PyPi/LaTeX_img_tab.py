def latex_table_generator(data):
    n_columns = len(data[0])
    table = "\documentclass[12pt, letterpaper]{article}\n" + "\\begin{document}\n" + "\\begin{tabular}{|" + "|".join(["c"] * n_columns) + "|}\n" + "\hline\n"

    for row in data:
        table += "& ".join(str(cell) for cell in row) + "\\\\\n"
        table += "\hline\n"
    
    table += "\end{tabular}\n" + "\end{document}"

    return table

def latex_image_generator(path_to_folder_with_img, selected_img_in_folder):
    preamble = "\\documentclass{article}\n" + "\\usepackage{graphicx}\n" + "\\graphicspath{" + "{" + path_to_folder_with_img + "}\n"
    body = preamble + "\\begin{document}\n" + "\\includegraphics" + "{" + selected_img_in_folder + "}\n" + "\\end{document}"
    
    return body
