from typing import Any, List, Optional
from math import ceil, floor

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    
    max_column_length = [] #list for the maximum length of a column
    
    if not labels is None: #add label length to the maximum length
        for i in labels:
            max_column_length.append(len(str(i)))
    else: #add 0 as label length
        for i in range(len(rows[0])):
            max_column_length.append(0)
            
    for j in range(len(rows[0])): #add the length of a row item if it is longer than the label length or another leangth of a row
        for i in rows:
            if len(str(i[j])) > max_column_length[j]:
                max_column_length[j] = len(str(i[j]))
    
    #top and bot line creation
    #top line
    top_line = "┌─"    
    for j in max_column_length:
        for i in range(j):
            top_line += "─"
        top_line += "─┬─"
    top_line = top_line[:-2] + "┐\n"

    #bot line
    bot_line = "└─"
    for j in max_column_length:
        for i in range(j):
            bot_line += "─"
        bot_line += "─┴─"
    bot_line = bot_line[:-2] + "┘\n"
    
    #table header
    table_header = ""
    if not labels is None:
        table_header += "│ "
        for i in labels:
            if not centered:
                table_header += i + "".join(' ' for l in range(max_column_length[labels.index(i)] - len(str(i)))) + " │ "
            elif centered:
                table_header += "".join(' ' for l in range(int(floor((max_column_length[labels.index(i)] - len(str(i)))/2)))) + str(i) + "".join(' ' for l in range(int(ceil((max_column_length[labels.index(i)] - len(str(i)))/2)))) +  " │ "
        table_header = table_header[:-1] + "\n"
        table_header += "├─"    
        for j in max_column_length:
            for i in range(j):
                table_header += "─"
            table_header += "─┼─"
        table_header = table_header[:-2] + "┤\n"
    
    #table body
    table_body = ""
    for j in rows:
        for i in range(len(j)):
            if not centered:
                table_body += "│ " + str(j[i]) + "".join(' ' for l in range(max_column_length[i] - len(str(j[i])) + 1))
            elif centered:
                table_body += "│ " + "".join(' ' for l in range(int(floor((max_column_length[i] - len(str(j[i])))/2)))) + str(j[i]) + "".join(' ' for l in range(int(ceil((max_column_length[i] - len(str(j[i])))/2)) + 1))
        table_body += "│\n"
    
    return top_line + table_header + table_body + bot_line
