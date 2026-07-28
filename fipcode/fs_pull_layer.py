from pathlib import Path


class FSPullLayer:
    def __init__(self, file, content):
        self.file = Path(file)
        self.content = content

        self.file.write_text(
            self.content,
            encoding="utf-8"
        )
