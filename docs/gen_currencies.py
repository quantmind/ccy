import mkdocs_gen_files

from ccy import currencydb

with mkdocs_gen_files.open("currencies.md", "w") as f:
    f.write("# Currencies\n\n")
    f.write(
        "This is a list of all currencies currently supported by ccy. You can "
        "add more by contributing to the [currency database](https://github.com/quantmind/ccy).\n\n"
    )

    f.write(
        "<input id='ccy-search' type='text' placeholder='Search by name...' "
        "style='margin-bottom:1em;padding:0.4em 0.6em;width:100%;max-width:400px;"
        "border:1px solid #ccc;border-radius:4px;font-size:0.95em;' />\n\n"
    )

    f.write("<table id='ccy-table'>\n")
    f.write(
        "<thead><tr>"
        "<th>Code</th><th>Name</th><th>ISO</th><th>Country</th>"
        "<th>Order</th><th>Rounding</th><th>Fixed DC</th><th>Float DC</th>"
        "</tr></thead>\n"
    )
    f.write("<tbody>\n")
    for c in sorted(currencydb().values(), key=lambda x: x.code):
        f.write(
            f"<tr>"
            f"<td><code>{c.code}</code></td>"
            f"<td>{c.name}</td>"
            f"<td>{c.isonumber}</td>"
            f"<td>{c.default_country}</td>"
            f"<td>{c.order}</td>"
            f"<td>{c.rounding}</td>"
            f"<td><code>{c.fixeddc}</code></td>"
            f"<td><code>{c.floatdc}</code></td>"
            f"</tr>\n"
        )
    f.write("</tbody>\n</table>\n\n")

    f.write(
        "<script>\n"
        "document.getElementById('ccy-search').addEventListener('input', function() {\n"
        "  var term = this.value.toLowerCase();\n"
        "  document.querySelectorAll('#ccy-table tbody tr').forEach(function(row) {\n"
        "    var code = row.cells[0].textContent.toLowerCase();\n"
        "    var name = row.cells[1].textContent.toLowerCase();\n"
        "    var country = row.cells[3].textContent.toLowerCase();\n"
        "    row.style.display = (code.includes(term) || name.includes(term) || country.includes(term)) ? '' : 'none';\n"
        "  });\n"
        "});\n"
        "</script>\n"
    )
