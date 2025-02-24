'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''

import streamlit as st
import packaging
import json
from io import StringIO
from pathlib import Path

st.title("Package File Processor")

for key in ["summaries", "total_files", "total_lines"]:
    st.session_state.setdefault(key, 0 if key != "summaries" else [])

if file := st.file_uploader("Upload a package file:"):
    json_filename = file.name.replace(".txt", ".json")
    packages = [packaging.parse_packaging(line.strip()) for line in StringIO(file.getvalue().decode()).read().splitlines() if line.strip()]

    Path("./data").mkdir(parents=True, exist_ok=True)
    Path(f"./data/{json_filename}").write_text(json.dumps(packages, indent=4))

    st.session_state.summaries.append(f"{len(packages)} packages saved in {json_filename} 📂")
    st.session_state.total_files = st.session_state.total_files + 1
    st.session_state.total_lines = st.session_state.total_lines + len(packages)

    st.info("\n".join(st.session_state.summaries))
    st.success(f"Processed {st.session_state.total_files} files, {st.session_state.total_lines} total packages 📦")
