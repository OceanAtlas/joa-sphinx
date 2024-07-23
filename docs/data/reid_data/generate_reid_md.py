import csv

atlantic_sections = []
indian_sections = []
pacific_sections = []
with open("query_result.csv", encoding="latin1") as f:
    reader = csv.DictReader(f)
    for line in reader:
        content = "\n".join([
            f":sd2: {line['nodc_sd2']}",
            f":joa: {line['file_name']}",
            f":ship: {line['ship_name']}",
            "",
            line["description"]
        ])
        match line['basin_name']:
            case "Atlantic":
                atlantic_sections.append(content)
            case "Indian":
                indian_sections.append(content)
            case "Pacific":
                pacific_sections.append(content)

sep = "\n\n---\n\n"
with open("_reid_atlantic.md", "w") as f:
    f.write(sep.join(atlantic_sections))
with open("_reid_indian.md", "w") as f:
    f.write(sep.join(indian_sections))
with open("_reid_pacific.md", "w") as f:
    f.write(sep.join(pacific_sections))