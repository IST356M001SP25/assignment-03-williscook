'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''

import streamlit as st
import packaging
import json
from io import StringIO
from pathlib import Path

st.title("Package File Processor")

def process_file(file):
    text = StringIO(file.getvalue().decode("utf-8")).read().splitlines()
    packages = [
        (pkg := packaging.parse_packaging(line.strip())) and 
        st.info(f"{line} ➡️ Total 📦 Size: {packaging.calc_total_units(pkg)} {packaging.get_unit(pkg)}") 
        or pkg for line in text if line.strip()
    ]
    save_path = Path(f"./data/{file.name.replace('.txt', '.json')}")
    save_path.parent.mkdir(parents=True, exist_ok=True)
    save_path.write_text(json.dumps(packages, indent=4))
    st.success(f"Processed {len(packages)} packages. Saved as {save_path.name} 📂")

if (file := st.file_uploader("Upload your package file (TXT format)")):
    process_file(file)
    