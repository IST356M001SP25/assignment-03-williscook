'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''

import streamlit as st
import packaging

# Input field with emoji
pkg = st.text_input("👉 Enter package data:")

if pkg:
    # Parse the package data
    parsed_pkg = packaging.parse_packaging(pkg)
    total = packaging.calc_total_units(parsed_pkg)
    unit = packaging.get_unit(parsed_pkg)
    
    # Display parsed package data
    st.subheader("📦 Parsed Package Data:")
    st.text(parsed_pkg)
    
    # Display each item with an arrow emoji
    for item in parsed_pkg:
        name = list(item.keys())[0]
        size = list(item.values())[0]
        st.info(f"{name} ➡️ {size}")
    
    # Display total size with a box and checkmark emoji
    st.success(f"📦✔️ Total Package Size: {total} {unit}")