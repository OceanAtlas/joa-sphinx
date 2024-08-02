import csv
from pathlib import Path
from itertools import groupby

root_dir = Path(__file__).parent


sep = "\n\n---\n\n"
def file_record(line):
   return "\n".join([
            f":sd2: {line['nodc_sd2']}",
            f":joa: {line['file_name']}",
            f":ship: {line['ship_name']}",
            "",
            line["description"]
        ])

# By Sub_basin
def grouped_writer(group_name, root, files):

    group_out = root / f"_{group_name}"
    sorted_by_group = sorted(files, key=lambda x: x[group_name])
    by_group_data = []
    for group, files in groupby(sorted_by_group, key=lambda x: x[group_name]):
        files = list(files)
        if group == "NULL":
            continue
        if group_name == "ship_name" and files[0]["ship_code"] != "NULL":
            by_group_data.append(f"# {group} ({files[0]["ship_code"]})")
        else:
            by_group_data.append(f"# {group}")
        by_group_data.append(sep.join(file_record(file) for file in files))
    group_out.write_text("\n".join(by_group_data))

reid_root_dir = root_dir / "reid"

with open("_reid_raw_data.csv", encoding="latin1") as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Atlantic
atlantic_data = list(filter(lambda x: x["basin_name"] == "Atlantic", data))
atlantic_root = reid_root_dir / "Atlantic" / "_includes"
atlantic_root.mkdir(parents=True, exist_ok=True)

atlantic_entire = atlantic_root / "_entire"
atlantic_entire.write_text(sep.join([file_record(file) for file in atlantic_data]))

grouped_writer("sub_basin_name", atlantic_root, atlantic_data)
grouped_writer("ship_name", atlantic_root, atlantic_data)
grouped_writer("year", atlantic_root, atlantic_data)

# Indian
indian_data = list(filter(lambda x: x["basin_name"] == "Indian", data))
indian_root = reid_root_dir / "Indian" / "_includes"
indian_root.mkdir(parents=True, exist_ok=True)

indian_entire = indian_root / "_entire"
indian_entire.write_text(sep.join([file_record(file) for file in indian_data]))

grouped_writer("ship_name", indian_root, indian_data)
grouped_writer("year", indian_root, indian_data)

# Pacific
pacific_data = list(filter(lambda x: x["basin_name"] == "Pacific", data))
pacific_root = reid_root_dir / "Pacific" / "_includes"
pacific_root.mkdir(parents=True, exist_ok=True)

pacific_entire = pacific_root / "_entire"
pacific_entire.write_text(sep.join([file_record(file) for file in pacific_data]))

grouped_writer("sub_basin_name", pacific_root, pacific_data)
grouped_writer("ship_name", pacific_root, pacific_data)
grouped_writer("year", pacific_root, pacific_data)