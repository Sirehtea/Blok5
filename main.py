from jinja2 import Environment, FileSystemLoader, select_autoescape

auteurs = ["Vincent", "Jos", "Yllias"]

alias_mapping = {auteur: f"student_{i}" for i, auteur in enumerate(auteurs)}

matrix_opmerkingen = {auteur: {andere_auteur: [] for andere_auteur in auteurs} for auteur in auteurs}

matrix_opmerkingen["Vincent"]["Jos"] = ["dezelfde verdachte fout"]
matrix_opmerkingen["Jos"]["Yllias"] = ["vergelijkbare spellingsfouten"]

env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape()
)

template = env.get_template("outputtemplate.html")

output_file_name = input("Hoe moet je output file heten? (zonder extensie) ")

with open(output_file_name + ".html", "w") as output_file:
    output_file.write(template.render(auteurs=alias_mapping.values(), matrix_opmerkingen=matrix_opmerkingen, alias_mapping=alias_mapping))

print(f"De HTML-output is opgeslagen in {output_file_name}")
