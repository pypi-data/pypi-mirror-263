import os

from komodo.framework.komodo_tool import KomodoTool


class SampleTool(KomodoTool):
    shortcode = "sample_tool"
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
                    },
                    "function_call": {
                        "type": "string",
                        "description": "Function that the tool should call."
                    }
                },
                "required": ["filename", "function_call"]
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
            with open(path, 'r') as file:
                file.seek(start)
                contents = file.read()
                if args["function_call"] == "hello_world":
                    return hello_world(contents)
                return KomodoTool.to_base64(contents)
        except Exception:
            return "Failed to read file: " + args["filename"]


def hello_world(contents: str):
    return "Hello World! Length: " + str(len(contents))


if __name__ == "__main__":
    from komodo.testdata.config import TestConfig

    tool = SampleTool(TestConfig.path("dir1"))
    print(tool.definition)
    print(tool.action({"filename": "hello.txt", "function_call": "hello_world"}))
