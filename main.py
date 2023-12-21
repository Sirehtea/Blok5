import os
import filecmp
import re
from jinja2 import Environment, FileSystemLoader, select_autoescape

def compare_files(path1, path2):
    return filecmp.cmp(path1, path2)

def extract_comments(file_path): #reguliere expressie om single-line comments te vinden
    with open(file_path, "r",) as file:
        content = file.read()
        comments = re.findall(r'#(.+?)(?=\n|$)', content)
        return comments

def should_compare(author1, author2, matrix_opmerkingen):
    return author1 != author2 and not matrix_opmerkingen[author2][author1]

def build_matrix(directory):
    authors = sorted(os.listdir(directory))
    matrix_opmerkingen = {author: {other_author: [] for other_author in authors} for author in authors}

    for i, author1 in enumerate(authors):
        for j, author2 in enumerate(authors):
            if should_compare(author1, author2, matrix_opmerkingen):
                file1_path = os.path.join(directory, author1, os.listdir(os.path.join(directory, author1))[0])
                file2_path = os.path.join(directory, author2, os.listdir(os.path.join(directory, author2))[0])

                if os.path.basename(file1_path) == os.path.basename(file2_path) and compare_files(file1_path, file2_path):
                    matrix_opmerkingen[author1][author2].append("identieke file en naam " + os.path.basename(file1_path))
                elif os.path.basename(file1_path) == os.path.basename(file2_path):
                    matrix_opmerkingen[author1][author2].append("identieke naam " + os.path.basename(file1_path))
                elif compare_files(file1_path, file2_path):
                    matrix_opmerkingen[author1][author2].append("identieke file " + os.path.basename(file1_path))

                comments1 = extract_comments(file1_path)
                comments2 = extract_comments(file2_path)
                identical_comments = set(comments1) & set(comments2)

                if identical_comments:
                    matrix_opmerkingen[author1][author2].append("identieke comments: " + ", ".join(identical_comments))

    return authors, matrix_opmerkingen

def generate_html_output(authors, matrix_opmerkingen, output_filename):
    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape()
    )

    template = env.get_template("outputtemplate.html")
    output_html = template.render(authors=authors, matrix_opmerkingen=matrix_opmerkingen)

    output_filepath = f"{output_filename}.html"
    with open(output_filepath, "w") as output_file:
        output_file.write(output_html)

    print(f"HTML file generated: {output_filepath}")

def main():
    directory_path = input("Enter the path to the analysis directory: ")
    output_filename = input("Enter the desired filename for the HTML output (without extension): ")

    authors, matrix_opmerkingen = build_matrix(directory_path)
    generate_html_output(authors, matrix_opmerkingen, output_filename)

if __name__ == "__main__":
    main()
