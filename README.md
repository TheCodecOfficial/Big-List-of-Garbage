# Big List of Garbage (BLOG)

This is a simple tool to generate blog posts. It uses a simple markup language to define the structure of the blog, including titles, images, chapters, and image comparisons.

## Example

```
!title: This is the Title

!img:
    images/render.png
    Image description

!chapter: Chapter 1

This is some introductory text. Lorem ipsum dolor sit amet.

!subchapter: Subchapter 1.1

LaTeX is supported $e^{i\pi} + 1 = 0$.

Multiline math works too:
$$
L_o = L_e + \int_\Omega f_r L_i (\omega_i) \cos\theta d\omega_i
$$

!chapter: Chapter 2

Image comparisons example:

To make it more readable, you can indent the parameters. Any indentation is ignored.

!imgcomp:
    images/no_tonemap.png
    images/bloom.png
    No Tonemapping
    With Tonemapping
    Comparison description

This is some code:

!codeblock:
Code Description
python
def func(x: int) -> int:
    return x**2
!endcode
```

## Syntax

It follows a simple EBNF grammar:

```lark
start: document

document: metadata block*

metadata: "!title: " _string "\n"+ ("!date: " /\d{2}\.\d{2}\.\d{4}/ "\n"+)?

block: single_arg_tag
    | multi_arg_tag
    | special_tag
    | text_block

text_block: (text_line "\n"+)+

text_line: /(?!!)[^\n]+/

single_arg_tag: "!chapter: " _string "\n"+ -> chapter
    | "!subchapter: " _string "\n"+ -> subchapter

multi_arg_tag: img_tag
    | code_tag
    | imgcomp_tag

img_tag: "!img:\n" _string "\n" _string "\n"+

code_tag: "!code:\n" _string "\n" _string "\n"+

imgcomp_tag: "!imgcomp:\n" _string "\n" _string "\n" _string "\n" _string "\n" _string "\n"+

special_tag: codeblock_tag
    | table_tag

codeblock_tag: "!codeblock:\n" _string "\n" _string "\n" code_lines "!endcode" "\n"+ -> codeblock

code_lines: (_string "\n")*

table_tag: "!table:\n" table_rows "!endtable" "\n"+ -> table

table_rows: (table_row "\n")*

table_row: /[^\n|]+/ ("|" /[^\n|]+/)*

_string: /[^\n]+/
```


## TODO

- Add table support
- Add more code block languages
- Add support for code blocks from file
- Add support for lists
- Add text formatting (bold, italic, underline)
- Add support for links
- Add polyring stuff
- Live update while editing blog file