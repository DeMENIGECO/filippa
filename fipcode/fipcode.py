from pathlib import Path
import xml.etree.ElementTree as ET

from fipcode.fs_pull_layer import FSPullLayer


XML_FILE = Path(__file__).parent / "fs_meta_resp.xml"


def main():
    category_name = input("Categoria: ")
    prompt_text = input("Prompt: ")

    if not XML_FILE.exists():
        print(f"❌ File non trovato: {XML_FILE}")
        return

    tree = ET.parse(XML_FILE)
    root = tree.getroot()

    category = None

    for cat in root.findall("category"):
        if cat.get("name") == category_name:
            category = cat
            break

    if category is None:
        print(f"❌ Categoria '{category_name}' non trovata.")
        return

    for pull in category.findall("pull"):
        if pull.findtext("prompt") == prompt_text:
            file = pull.findtext("file")
            content = pull.findtext("content")
            output = pull.findtext("out")

            FSPullLayer(file, content)

            print(output)
            return

    print(f"❌ Pull con prompt '{prompt_text}' non trovato.")


if __name__ == "__main__":
    main()
