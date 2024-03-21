import sys


def columnize(columnize_data, display_width=80):
    """
    Display a list of strings as a compact set of columns.

    Each column is only as wide as necessary.
    Columns are separated by two spaces (one was not legible enough).

    :param columnize_data: a list of list
    :type columnize_data: list
    :param display_width: the maximum allowed size
    :type display_width: int
    """
    if not columnize_data:
        sys.stdout.write("<empty>\n")
        return

    non_strings = [i for i in range(len(columnize_data)) if not isinstance(columnize_data[i], str)]
    if non_strings:
        sys.stderr.write("list[i] not a string for i in %s" % ", ".join(map(str, non_strings)))
        return
    size = len(columnize_data)
    if size == 1:
        sys.stdout.write("%s\n" % str(columnize_data[0]))
        return
    # Try every row count from 1 upwards
    for num_rows in range(1, len(columnize_data)):
        num_cols = (size + num_rows - 1) // num_rows
        col_widths = []
        tot_width = -2
        for col in range(num_cols):
            colwidth = 0
            for row in range(num_rows):
                i = row + num_rows * col
                if i >= size:
                    break
                x = columnize_data[i]
                colwidth = max(colwidth, len(x))
            col_widths.append(colwidth)
            tot_width += colwidth + 2
            if tot_width > display_width:
                break
        if tot_width <= display_width:
            break
    else:
        num_rows = len(columnize_data)
        num_cols = 1
        col_widths = [0]
    for row in range(num_rows):
        texts = []
        for col in range(num_cols):
            i = row + num_rows * col
            if i >= size:
                x = ""
            else:
                x = columnize_data[i]
            texts.append(x)
        while texts and not texts[-1]:
            del texts[-1]
        for col, _ in enumerate(texts):
            texts[col] = "%-*s" % (col_widths[col], texts[col])
        sys.stdout.write("%s\n" % str("  ".join(texts)))
