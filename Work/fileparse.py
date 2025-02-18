# fileparse.py
import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter = ',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    #deal selecting certain columns and dealing when has no headers
    if select and not has_headers:
        raise RuntimeError ('select argument requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

        # Read the file headers in case there is one
    headers = next(rows) if has_headers else []

        # If a column was chosen
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select   
        
    records = []   
        #enumatering rows
    for rowno, row in enumerate (rows, 1):
            # Skip rows with blanket data
        if not row:    
            continue
            
            # If column indices are selected, pick them out
        if select:
            row = [ row[index] for index in indices]

            # Converting to the correct type
        if types:
                #try and except to 
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                #in case of error is true
                if not silence_errors:
                    print (f"Row {rowno}: Couldn't convert {row}")
                    print (f"Row {rowno}: Reason {e}")
                continue

        # Creating dictionary
        if headers:
            record = dict(zip(headers, row))
        # Creating tuple instead
        else:
            record = tuple(row)
            
        records.append(record)

    return records