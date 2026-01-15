# Big List of Garbage (BLOG)

This is a simple tool to generate blog posts. It uses a simple markup language to define the structure of the blog, including titles, images, chapters, and image comparisons.

## Example

```
!title: This is the Title

!img:
    images/render.png
    Image description

!chapter: Chapter 1

This is some introductory text. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer hendrerit auctor vehicula. Ut non laoreet eros, lacinia tristique erat. Fusce tincidunt, mauris nec euismod accumsan, quam tellus eleifend eros, vel imperdiet ex libero a arcu. Curabitur dapibus pulvinar nibh, quis mattis urna fermentum at. Suspendisse blandit interdum tortor, non sollicitudin urna cursus quis. Vivamus ac tortor a dui congue aliquam vitae in nisl.

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

## TODO

- Add table support
- Add more code block languages
- Add support for code blocks from file
- Add support for lists
- Add text formatting (bold, italic, underline)
- Add support for links
- Add polyring stuff
- Live update while editing blog file