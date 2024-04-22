# Konwerter JSON do XML

Prosty skrypt napisany w języku Python do konwersji plików JSON na format XML. Skrypt monitoruje określony folder wejściowy w poszukiwaniu plików JSON, konwertuje je na XML i przenosi wynikowe pliki XML do folderu wyjściowego.

## Instrukcja obsługi

### Wymagania

1. Python 3.x z zainstalowanymi modułami `json`, `time`, `shutil`, `xml.etree.ElementTree`.

### Instalacja

1. Sklonuj ten repozytorium na swój lokalny komputer:

    ```
    git clone https://github.com/kadlub/json_to_xml.git
    ```

2. Przejdź do katalogu projektu:

    ```
    cd json_to+xml
    ```

3. Uruchom skrypt, wprowadzając ścieżkę do folderu wejściowego i wyjściowego:

    ```
    python json_to_xml.py
    ```

4. Postępuj zgodnie z instrukcjami wyświetlanymi w konsoli.

### Uwagi

- Upewnij się, że w folderze wejściowym znajdują się tylko pliki JSON do konwersji.
- Skrypt będzie działał w tle, monitorując folder wejściowy i przetwarzając nowe pliki JSON automatycznie.

