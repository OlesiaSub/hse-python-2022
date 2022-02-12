import logging
import os
from functools import reduce


def generate_latex_string(inp) -> str:
    def check():
        return reduce(lambda a, b: a & b, map(lambda x: len(x) == len(inp[0]), inp))

    def get_col_data() -> str:
        return ''.join(map(lambda _: "c ", [''] * len(inp[0])))

    def convert_to_string() -> str:
        def concat_list(cur):
            return reduce(lambda a, b: a + " & " + b, cur)

        return ''.join(map(lambda cur: concat_list(cur) + " \\\\\n", inp))

    def create_latex_with_env() -> str:
        return "\\documentclass{article}\n" \
               "\\usepackage[utf8]{inputenc}\n" \
               "\\usepackage[a4paper,top=2cm,bottom=2cm,left=3cm,right=3cm,marginparwidth=1.75cm]{geometry}\n" \
               "\\usepackage{graphicx}\n" \
               "\\title{Python-course}\n" \
               "\\begin{document}\n" \
               "\\maketitle\n" \
               "\\begin{center}\n" \
               f"\\begin{{tabular}}{{{get_col_data()}}}\n" \
               f"{convert_to_string()}\n" \
               "\\end{tabular}\n" \
               "\\end{center}\n" \
               "\\end{document}\n"

    if not check():
        logging.error("Incorrect input")
        os.system(exit(1))

    return create_latex_with_env()


def write_to_file(data):
    f = open("artifacts/hw2.tex", "w")
    f.write(data)
    f.close()


def create_latex():
    input_list = [
        ["first", "second", "third"],
        ["4", "fifth", "sixth"],
        ["seventh", "eighth", "9"],
        ["10", "11", "12"]
    ]
    write_to_file(generate_latex_string(input_list))
    os.system("pdflatex -halt-on-error -output-directory artifacts artifacts/hw2.tex")
    os.system("rm artifacts/hw2.aux artifacts/hw2.log")


if __name__ == '__main__':
    create_latex()
