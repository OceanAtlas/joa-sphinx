import csv
from pathlib import Path
from itertools import groupby
from tomllib import loads

root_dir = Path(__file__).parent


sep = "\n\n---\n\n"


def file_record(line):
    return "\n".join(
        [
            f":sd2: {line['nodc_sd2']}",
            f":joa: {line['file_name']}",
            f":ship: {line['ship_name']}",
            "",
            line["description"],
        ]
    )


def write_section_data(dp:Path, out_path:Path):
    data = loads(dp.read_text())
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w") as f:
        for section in data["section"]:
            if "years" not in section:
                continue
            if "Maps" in section["title"] or "Guide" in section["title"]:
                continue
            f.write(f"### {section['title']}\n")
            for year in section["years"]:
                f.write(f"#### {year['year']}\n")
                for file in year["files"]:
                    name = file.get("name", "No Files")
                    path = file.get('path')
                    if path is not None:
                        f.write(f"* [{name}]({path})\n")
                    else:
                        f.write(f"* {name}\n")
                f.write("\n")

def write_woa_data(dp: Path, out_path:Path):
    data = loads(dp.read_text())
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w") as f:
        for section in data["section"]:
            f.write(f"### {section['title']}\n")
            for subsection in section["subsections"]:
                f.write(f"#### {subsection['subsection']}\n")
                for file in subsection.get("files", []):
                    name = file.get("name", "No Files")
                    path = file.get('path')
                    if path is not None:
                        f.write(f"* [{name}]({path})\n")
                    else:
                        f.write(f"* {name}\n")
                f.write("\n")

                for subsubsection in subsection.get("subsubsections", []):
                    f.write(f"##### {subsubsection['subsubsection']}\n")
                    for file in subsubsection.get("files", []):
                        name = file.get("name", "No Files")
                        path = file.get('path')
                        if path is not None:
                            f.write(f"* [{name}]({path})\n")
                        else:
                            f.write(f"* {name}\n")
                    f.write("\n")

                    for season in subsubsection.get("seasons", []):
                        f.write(f"###### {season['season']}\n")
                        for file in season.get("files", []):
                            name = file.get("name", "No Files")
                            path = file.get('path')
                            if path is not None:
                                f.write(f"* [{name}]({path})\n")
                            else:
                                f.write(f"* {name}\n")
                        f.write("\n")

write_section_data(root_dir / "_data" / "atlanticdata.toml", root_dir / "_includes" / "_atlantic")
write_section_data(root_dir / "_data" / "pacificdata.toml", root_dir / "_includes" / "_pacific")
write_section_data(root_dir / "_data" / "indiandata.toml", root_dir / "_includes" / "_indian")
write_section_data(root_dir / "_data" / "arcticdata.toml", root_dir / "_includes" / "_arctic")
write_section_data(root_dir / "_data" / "southerndata.toml", root_dir / "_includes" / "_southern")
#write_section_data(root_dir / "_data" / "woadata.toml", root_dir / "_includes" / "_woa")
write_woa_data(root_dir / "_data" / "woadata.toml", root_dir / "_includes" / "_woa")
