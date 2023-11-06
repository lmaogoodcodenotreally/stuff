## Pour fix l'input dans le proxy checker

input_string = ## l'input envoyer par l'utilisateur

if "\\" in input_string or ":" in input_string or "/" in input_string:  ## path checks
    is_filepath = True
else:
    is_filepath = False
    if not input_string.endswith(".txt"):  ## detect txt
        input_string += ".txt"


