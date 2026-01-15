from blog_parser import parse_blog
import datetime

html_files = ["body", "chapter", "code_block", "head", "image_comparison", "image", "subchapter", "text_block"]
components = {k: open(f"resources/components/{k}.html").read() for k in html_files}

blog_file = "test.blog"


def generate_content(blocks):
    content = ""
    for block in blocks:
        match block["type"]:
            case "chapter":
                content += components["chapter"].replace("CHAPTER", block["content"])
            case "subchapter":
                content += components["subchapter"].replace("SUBCHAPTER", block["content"])
            case "text":
                content += components["text_block"].replace("TEXT", block["content"])
            case "code_block":
                language = block.get("language", "plaintext")
                content += (
                    components["code_block"]
                    .replace("CODE", block["code"])
                    .replace("DESCRIPTION", block["description"])
                    .replace("LANGUAGE", language)
                )
            case "image":
                content += components["image"].replace("SRC", block["src"]).replace("DESCRIPTION", block["description"])
            case "image_comparison":
                src1, src2 = block["imgs"]
                label1, label2 = block["labels"]
                image_comparison = (
                    components["image_comparison"]
                    .replace("SRC1", src1)
                    .replace("LABEL1", label1)
                    .replace("SRC2", src2)
                    .replace("LABEL2", label2)
                    .replace("DESCRIPTION", block["description"])
                )
                content += image_comparison
    return content


def main():
    with open(blog_file) as f:
        blog_content = f.read()

    blog_content += "\n"

    blog_data = parse_blog(blog_content)

    html = components["head"].replace("TITLE", blog_data["title"])
    date = datetime.date.today().strftime("%d.%m.%Y")
    body = components["body"].replace("TITLE", blog_data["title"]).replace("DATE", blog_data.get("date", date))
    html += body.replace("CONTENT", generate_content(blog_data["blocks"]))

    with open("generated_blog.html", "w") as f:
        f.write(html)


if __name__ == "__main__":
    main()
