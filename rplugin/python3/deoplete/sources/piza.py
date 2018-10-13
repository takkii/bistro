import re
import base64
from deoplete.source.base import Base


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'Bistro'
        self.filetypes = ['html']
        self.mark = '[bistro_dictionary]'
        regexmatch = [r'[<a-zA-Z(?: .+?)?>.*?<\/a-zA-Z>]']
        self.input_pattern = regexmatch
        self.rank = 500

    def get_complete_position(self, context):
        m = re.search('[a-zA-Z0-9_?!]*$', context['input'])
        return m.start() if m else -1

    def gather_candidates(self, context):
        html = ["<!-- -->", "<!doctype>", "</a>", "</abbr>", "</acronym>", "</address>", "</applet>", "</area>", "</b>",
                "</base>", "</basefont>", "</bdo>", "</bgsound>", "</big>", "</blink>", "</blockquote>", "</body>",
                "</br>", "</button>", "</caption>", "</center>", "</cite>", "</code>", "</col>", "</colgroup>",
                "</comment>", "</dd>", "</del>", "</dfn>", "</dir>", "</div>", "</dl>", "</dt>", "</em>", "</embed>",
                "</fieldset>", "</font>", "</form>", "</frame>", "</frameset>", "</head>", "</hr>", "</html>", "</i>",
                "</iframe>", "</ilayer>", "</img>", "</input>", "</ins>", "</isindex>", "</kbd>", "</label>",
                "</layer>",
                "</legend>", "</li>", "</link>", "</listing>", "</map>", "</marquee>", "</menu>", "</meta>",
                "</multicol>", "</nobr>", "</nobr>", "</noembed>", "</noframes>", "</nolayer>", "</noscript>",
                "</object>", "</ol>", "</optgroup>", "</option>", "</p>", "</param>", "</plaintext>", "</pre>", "</q>",
                "</rb>", "</rp>", "</rt>", "</ruby>", "</s>", "</samp>", "</script>", "</select>", "</small>",
                "</spacer>", "</span>", "</strike>", "</strong>", "</style>", "</sub>", "</sup>", "</table>",
                "</tbody>",
                "</td>", "</textarea>", "</tfoot>", "</th>", "</thead>", "</title>", "</tr>", "</tt>", "</u>", "</ul>",
                "</var>", "</wbr>", "</xmp>", "<a>", "<abbr>", "<acronym>", "<address>", "<applet>", "<area>", "<b>",
                "<base>", "<basefont>", "<bdo>", "<bgsound>", "<big>", "<blink>", "<blockquote>", "<body>", "<br>",
                "<button>", "<caption>", "<center>", "<cite>", "<code>", "<col>", "<colgroup>", "<comment>", "<dd>",
                "<del>", "<dfn>", "<dir>", "<div>", "<dl>", "<dt>", "<em>", "<embed>", "<fieldset>", "<font>", "<form>",
                "<frame>", "<frameset>", "<h1>", "<h6>", "<head>", "<hr>", "<html>", "<i>", "<iframe>", "<ilayer>",
                "<img>", "<input>", "<ins>", "<isindex>", "<kbd>", "<label>", "<layer>", "<legend>", "<li>", "<link>",
                "<listing>", "<map>", "<marquee>", "<menu>", "<meta>", "<multicol>", "<nobr>", "<nobr>", "<noembed>",
                "<noframes>", "<nolayer>", "<noscript>", "<object>", "<ol>", "<optgroup>", "<option>", "<p>", "<param>",
                "<plaintext>", "<pre>", "<q>", "<rb>", "<rp>", "<rt>", "<ruby>", "<s>", "<samp>", "<script>",
                "<select>",
                "<small>", "<spacer>", "<span>", "<strike>", "<strong>", "<style>", "<sub>", "<sup>", "<table>",
                "<tbody>", "<td>", "<textarea>", "<tfoot>", "<th>", "<thead>", "<title>", "<tr>", "<tt>", "<u>", "<ul>",
                "<var>", "<wbr>", "<xml", "<xmp>", "align", "alt", "background", "background-attachment",
                "background-color", "background-image", "background-position", "background-position-x",
                "background-position-y", "background-repeat", "behavior", "border", "border-bottom",
                "border-bottom-color", "border-bottom-style", "border-bottom-width", "border-collapse", "border-color",
                "border-left", "border-left-color", "border-left-style", "border-left-width", "border-right",
                "border-right-color", "border-right-style", "border-right-width", "border-spacing", "border-style",
                "border-top", "border-top-color", "border-top-style", "border-top-width", "border-width", "bottom",
                "caption-side", "cellpadding", "cellspacing", "class", "clear", "clip", "color", "content", "content",
                "cursor", "direction", "display", "dlight-color", "empty-cells", "filter", "float", "font",
                "font-family", "font-size", "font-style", "font-variant", "font-weight", "height", "href", "http-equiv",
                "id=", "ime-mode", "include-source", "layer-background-color", "layer-background-image", "layout-grid",
                "layout-grid-char", "layout-grid-line", "layout-grid-mode", "layout-grid-type", "left",
                "letter-spacing",
                "line-break", "line-height", "list-style", "list-style-image", "list-style-position", "list-style-type",
                "margin", "margin-bottom", "margin-left", "margin-right", "margin-top", "max-height", "max-width",
                "min-height", "min-width", "name", "nowrap", "onblur", "onclick", "onkeydown", "onkeyup", "onsubmit",
                "outline", "outline-color", "outline-style", "outline-width", "overflow", "overflow-x", "overflow-y",
                "padding", "padding-bottom", "padding-left", "padding-right", "padding-top", "page-break-after",
                "page-break-before", "position", "quotes", "right", "ruby-align", "ruby-overhang", "ruby-position",
                "scrollbar-arrow-color", "scrollbar-base-color", "scrollbar-darkshadow-color", "scrollbar-face-color",
                "scrollbar-highlight-color", "scrollbar-shadow-color", "src", "table-layout", "text-align",
                "text-autospace", "text-decoration", "text-indent", "text-justify", "text-transform",
                "text-underline-position", "title", "top", "type", "unicode-bidi", "value", "vertical-align",
                "visibility", "white-space", "width", "word-break", "word-spacing", "word-wrap", "writing-mode",
                "z-index", "zoom"]
        dic = html
        dic.sort(key=lambda dic: dic[0])
        return dic
