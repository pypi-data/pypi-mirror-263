def tabulate(tabular_data, headers, tablefmt, colalign):
    """
    :param tabular_data: a list of list
    :type tabular_data: list
    :param headers: a list
    :type headers: list
    :param tablefmt: totaly ignored
    :type tablefmt: str
    :param colalign: a tuple
    :type colalign: tuple
    """
    value_to_return = []
    if tablefmt is None:
        tablefmt = None

    columns_info = {}
    # prepare
    if headers:
        tabular_data.insert(0, headers)
    for line in tabular_data:
        for index_col, cell_value in enumerate(line):
            columns_info[index_col] = {}
            columns_info[index_col]["data"] = []
            columns_info[index_col]["text"] = []
            columns_info[index_col]["size"] = 0
            columns_info[index_col]["colalign"] = None

    # insert data
    for line in tabular_data:
        for index_col, cell_value in enumerate(line):
            columns_info[index_col]["data"].append(cell_value)
            columns_info[index_col]["text"].append(cell_value)
            if colalign:
                columns_info[index_col]["colalign"] = colalign[index_col]

            if len(str(cell_value)) > columns_info[index_col]["size"]:
                columns_info[index_col]["size"] = len(str(cell_value))

    # justify
    for _, value in columns_info.items():
        for index, item in enumerate(value["data"]):
            value["text"][index] = str(value["text"][index])
            if len(str(item)) < value["size"]:
                if value["colalign"].lower() == "right":
                    spacing = " " * int(value["size"] - len(str(item)))
                    value["text"][index] = "%s%s" % (spacing, value["text"][index])
                elif value["colalign"].lower() == "center":
                    spacing = " " * int(int(value["size"] - len(str(item))) / 2)
                    value["text"][index] = "%s%s" % (spacing, value["text"][index])
                    while len(value["text"][index]) < value["size"]:
                        value["text"][index] = "%s " % value["text"][index]
                else:
                    spacing = " " * int(value["size"] - len(str(item)))
                    value["text"][index] = "%s%s" % (value["text"][index], spacing)

    # output
    line_to_append = ""
    spacing = " "
    for line, line_value in enumerate(tabular_data):
        for col, _ in enumerate(line_value):
            line_to_append += "%s%s" % (columns_info[col]["text"][line], spacing)
        value_to_return.append(line_to_append.strip(" "))
        line_to_append = ""

    return "\n".join(value_to_return)
