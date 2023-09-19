import os
import xml.etree.ElementTree as ET

current_directory = os.getcwd()

nessus_files = [file for file in os.listdir(current_directory) if file.endswith(".nessus")]

if len(nessus_files) == 0:
    print("No file with .nessus extension was found in your directory.")
else:
    combined_results = ET.Element("NessusClientData_v2")

    for file_name in nessus_files:
        tree = ET.parse(file_name)
        root = tree.getroot()

        for report in root.findall(".//Report"):
            combined_results.append(report)

    combined_tree = ET.ElementTree(combined_results)
    combined_tree.write("combined_results.nessus", encoding="utf-8", xml_declaration=True)

    print("All .nessus files have been successfully merged and a new file named combined_results.nessus has been created.")
