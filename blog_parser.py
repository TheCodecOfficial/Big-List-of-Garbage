from lark import Lark, Transformer


def strip_token(token):
    return str(token).strip()


class DocumentTransformer(Transformer):
    # Helper to convert token objects to clean strings
    def _string(self, children):
        return str(children[0]).strip()

    # Handle the text line specifically
    def text_line(self, children):
        return str(children[0]).strip()

    # Metadata creates the base dictionary
    def metadata(self, children):
        if len(children) > 1:
            return {"title": str(children[0]).strip(), "date": str(children[1]).strip()}
        else:
            return {"title": str(children[0]).strip()}

    # Custom tags (using the -> alias in your grammar)
    def chapter(self, children):
        return {"type": "chapter", "content": str(children[0]).strip()}

    def subchapter(self, children):
        return {"type": "subchapter", "content": str(children[0]).strip()}

    # Text blocks collapse multiple lines into one string
    def text_block(self, children):
        return {"type": "text", "content": "\n".join(children)}

    # Multi-argument tags
    def img_tag(self, children):
        return {"type": "image", "src": strip_token(children[0]), "description": strip_token(children[1])}

    def code_tag(self, children):
        return {"type": "code_snippet", "file": strip_token(children[0]), "description": strip_token(children[1])}

    def imgcomp_tag(self, children):
        return {
            "type": "image_comparison",
            "imgs": [strip_token(children[0]), strip_token(children[1])],
            "labels": [strip_token(children[2]), strip_token(children[3])],
            "description": strip_token(children[4]),
        }

    # Special tags
    def codeblock(self, children):
        return {
            "type": "code_block",
            "description": strip_token(children[0]),
            "language": strip_token(children[1]),
            "code": "\n".join(children[2]),
        }

    def code_lines(self, children):
        return [str(c) for c in children]

    def table(self, children):
        # children[0] will be the list of rows from table_rows
        return {"type": "table", "rows": children[0]}

    def table_rows(self, children):
        return children  # Passes the list of table_row outputs up

    def table_row(self, children):
        return [str(c).strip() for c in children]

    # Collapse wrapper rules (block, special_tag, etc)
    def block(self, children):
        return children[0]

    def multi_arg_tag(self, children):
        return children[0]

    def special_tag(self, children):
        return children[0]

    # Final assembly
    def document(self, children):
        data = children[0]  # The metadata dict
        data["blocks"] = children[1:]
        return data

    def start(self, children):
        return children[0]


def parse_blog(string: str) -> dict:
    l = Lark(open("resources/grammar.lark").read())
    tree = l.parse(string)
    return DocumentTransformer().transform(tree)
