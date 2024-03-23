import os

from komodo.framework.komodo_tool import KomodoTool


class FileReader(KomodoTool):
    shortcode = "komodo_file_reader"
    name = "File Reader"
    purpose = "Reads data files and returns contents as base64 encoded string. You must decode the results."

    definition = {
        "type": "function",
        "function": {
            "name": shortcode,
            "description": purpose,
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "Name of file to read"
                    },
                    "start": {
                        "type": "integer",
                        "description": "Start position in file"
                    },
                    "bytes": {
                        "type": "integer",
                        "description": "Number of bytes to read. Defaults to 2048."
                    }
                },
                "required": ["filename"]
            }
        }
    }

    def __init__(self, path):
        super().__init__(shortcode=self.shortcode,
                         definition=self.definition,
                         action=self.action)
        self.path = path

    def action(self, args):
        try:
            path = os.path.join(self.path, args["filename"])
            start = args.get("start", 0)
            bytes = args.get("bytes", 2048)
            with open(path, 'rb') as file:
                file.seek(start)
                contents = file.read(bytes)
                return KomodoTool.to_base64(contents)
        except Exception:
            return "Failed to read file: " + args["filename"]


if __name__ == "__main__":
    from komodo.testdata.config import TestConfig

    tool = FileReader(TestConfig.path("dir1"))
    print(tool.definition)
    print(tool.action({"filename": "hello.txt"}))
