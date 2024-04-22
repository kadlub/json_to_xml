import os
import json
import time
import shutil
import xml.etree.ElementTree as ET


def json_to_xml(json_data, parent):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            elem = ET.SubElement(parent, key)
            json_to_xml(value, elem)
    elif isinstance(json_data, list):
        for item in json_data:
            json_to_xml(item, parent)
    else:
        parent.text = str(json_data)


def convert_json_to_xml(input_file, output_folder):
    # Odczytaj dane z pliku JSON
    with open(input_file, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    # Stwórz strukturę XML
    root_elem = ET.Element(os.path.splitext(os.path.basename(input_file))[0])
    json_to_xml(json_data, root_elem)

    # Zapisz dane do pliku XML
    output_file = os.path.join(
        output_folder, os.path.basename(input_file).replace(".json", ".xml")
    )
    tree = ET.ElementTree(root_elem)
    tree.write(output_file, encoding="utf-8", xml_declaration=True)

    return output_file


def process_files(input_folder, output_folder):
    while True:
        # Sprawdź pliki w folderze wejściowym
        files = [f for f in os.listdir(input_folder) if f.endswith(".json")]

        for file in files:
            input_file = os.path.join(input_folder, file)

            # Upewnij się, że plik został już w całości zapisany
            while True:
                try:
                    with open(input_file, "r", encoding="utf-8") as f:
                        json.load(f)
                    break
                except json.JSONDecodeError:
                    time.sleep(1)

            # Przetwórz plik JSON na XML
            try:
                output_file = convert_json_to_xml(input_file, output_folder)
                print(
                    f"Plik {file} został przekonwertowany do XML i przeniesiony do folderu {output_folder}."
                )
            except Exception as e:
                print(f"Błąd podczas konwersji pliku {file}: {e}")

            # Przenieś przetworzony plik do innego folderu
            try:
                xml_file = os.path.basename(output_file)
                shutil.move(output_file, os.path.join(output_folder, xml_file))
                print(
                    f"Plik {xml_file} został przeniesiony do folderu {output_folder}."
                )
            except Exception as e:
                print(f"Błąd podczas przenoszenia pliku {xml_file}: {e}")

        time.sleep(5)  # Odczekaj przed kolejnym sprawdzeniem plików


if __name__ == "__main__":
    input_folder = input("Podaj ścieżkę do folderu wejściowego: ")
    output_folder = input("Podaj ścieżkę do folderu wyjściowego: ")

    process_files(input_folder, output_folder)
