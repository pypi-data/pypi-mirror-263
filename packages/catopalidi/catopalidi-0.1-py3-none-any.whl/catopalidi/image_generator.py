def generate_latex_image(path, caption="Image"):
    return f"\\begin{{figure}}[h!]\n\\centering\n\\includegraphics{{ {path} }}\n\\caption{{ {caption} }}\n\\end{{figure}}"

