import tkinter as tk
import xml.etree.ElementTree as ET

# Parse the XML data
xml_data = '''
<data>
  <city>Manchester</city>
  <teamname>MCI</teamname>
  <middle_name>Man City</middle_name>
  <venue>Etihad Stadium</venue>
  <!-- ... rest of the XML ... -->
</data>
'''

root = tk.Tk()
root.title("Football Team Information")

# Parse the XML data
root_xml = ET.fromstring(xml_data)

# Create labels and display data
labels = {
    'City': root_xml.find('city').text,
    'Team Name': root_xml.find('teamname').text,
    'Middle Name': root_xml.find('middle_name').text,
    'Venue': root_xml.find('venue').text,
    'Rank': root_xml.find('league_results/rank').text,
    'Played': root_xml.find('league_results/played').text,
    'Won': root_xml.find('league_results/won').text,
    'Drawn': root_xml.find('league_results/drawn').text,
    'Lost': root_xml.find('league_results/lost').text,
    'Goal Difference': root_xml.find('league_results/goal_difference').text,
    'Points': root_xml.find('league_results/points').text,
    'Home Form': ', '.join([match.text for match in root_xml.findall('current_form/home/*')]),
    'Away Form': ', '.join([match.text for match in root_xml.findall('current_form/away/*')])
}

for i, (label_text, value_text) in enumerate(labels.items()):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=5, sticky='w')

    value = tk.Label(root, text=value_text)
    value.grid(row=i, column=1, padx=10, pady=5, sticky='e')

root.mainloop()