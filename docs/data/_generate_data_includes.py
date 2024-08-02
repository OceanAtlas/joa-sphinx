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


pre_woce_root = root_dir / "other" / "_includes"
pre_woce_root.mkdir(parents=True, exist_ok=True)

# file list taken from old rails controller code
atlantic_pre_woce = {
    'satl.1983-84.6N.1W.joa',
    'satl.1983-84.6N.45S_34S.joa',
    'natl.1983.6N-OC.11N_13N.joa',
    'satl.1983.OC.11S.joa',
    'natl.1983.OC.11N.joa',
    'natl.1981.AN.26N.joa',
    'satl.1983.OC.23S.joa',
    'satl.1988-89.8M-OC.28W.joa',
    'natl.1983.6N.38W.joa',
    'natl.1981.AN.37N.joa',
    'natl.1957.DS.47N.joa',
    'natl.1982.HU.48N.joa',
    'natl.1983.OC.52W.joa',
    'natl.1962.ER.53N.joa',
    'natl.1962.ER.59N.joa',
    'natl.1985.EV.64W.joa',
    'natl.1989.OC.8N.joa',
    'satl.1990.MT.68W_63W.joa',
    'satl.1987.6N.10S_5N.joa',
    'satl.1989.8M.41W.joa',
    'satl.1987-88.6N.14S.joa',
    'satl.1987.6N.10S_2N.joa',
    'satl.1988-89.6N-8M.26S.joa',
    'satl.1990.MT.63S_35S.joa',
    'natl.1981.6N.51N.joa',
    'natl.1981.6N.58N.joa',
    'natl.1981-82.6N.55W.joa',
    'natl.1982.6N.4N_17N.joa',
    'satl.1983.6N.34W_17W.joa',
    'natl.1972.6N.44N_74N.joa',
    'satl.1972-73.6N.66W_1W.joa',
    'satl.1973.6N.58S.joa',
    'satl.1973.6N.67W_19E.joa',
}
pre_woce_al_files = list(filter(lambda x: x["file_name"] in atlantic_pre_woce, data))
pre_woce_atl = pre_woce_root / "_pre_woce_atl"
pre_woce_atl.write_text(sep.join([file_record(file) for file in pre_woce_al_files]))

indian_pre_woce = {
    'ind.1976.AN.18S.joa',
    'ind.1979.9W.12S.joa',
    'ind.1987.AB.30-33S.joa',
}
pre_woce_ind_files = list(filter(lambda x: x["file_name"] in indian_pre_woce, data))
pre_woce_ind = pre_woce_root / "_pre_woce_ind"
pre_woce_ind.write_text(sep.join([file_record(file) for file in pre_woce_ind_files]))

pacific_pre_woce = {
        'npac.1974.RY.130E.joa',
        'npac.1974.RY.136E.joa',
        'npac.1984.WT.152W.joa',
        'npac.1985.TT.24N.joa',
        'npac.1985.TT.47N.joa',
        'npac.1989.MW.9N.joa',
        'spac.1967.ET.28S.joa',
        'spac.1967.ET.43S.joa',
        'spac.1968.ET.117E.joa',
        'spac.1968.ET.120W.joa',
        'spac.1968.ET.128E.joa',
        'spac.1970.ET.120E.joa',
        'spac.1970.HH.170W.joa',
        'spac.1971.HH.146W.joa',
}
pre_woce_pacific_files = list(filter(lambda x: x["file_name"] in pacific_pre_woce, data))
pre_woce_pac = pre_woce_root / "_pre_woce_pac"
pre_woce_pac.write_text(sep.join([file_record(file) for file in pre_woce_pacific_files]))