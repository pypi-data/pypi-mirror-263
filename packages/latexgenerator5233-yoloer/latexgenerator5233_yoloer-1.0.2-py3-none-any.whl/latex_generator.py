def generate_latex_document(table_data, image_path):
    def latex_table(data):
        rows = []
        for row in data:
            row_str = " & ".join(map(str, row)) + " \\\\"
            rows.append(row_str)
        table_str = "\n".join(rows)
        latex_code = "\\begin{tabular}{|c|c|c|c|c|}\n"
        latex_code += "\\hline\n"
        latex_code += table_str + "\n"
        latex_code += "\\hline\n"
        latex_code += "\\end{tabular}"
        return latex_code 

    def latex_image(path):
        latex_code = "\\begin{figure}[h]\n"
        latex_code += "\\raggedright\n"
        latex_code += "\\includegraphics[scale=0.4]{" + path + "}\n"
        latex_code += "\\end{figure}"
        return latex_code 

    table_latex = latex_table(table_data)
    image_latex = latex_image(image_path)

    latex_code = f"""
    \\documentclass{{article}}
    \\usepackage{{graphicx}} % Required for inserting images
    
    \\title{{AP2024\_HW\_2.1}}
    \\author{{Wang Quanyu}}
    \\date{{March 2024}}
    
    \\begin{{document}}
    
    \\maketitle
    
    \\section{{Generate table}}
    {table_latex}
    
    \\section{{Generate image}}
    {image_latex}
    
    \\end{{document}}
    """
    
    return latex_code