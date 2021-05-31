# fileparse.py
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter = ','):
    '''
    Parse a CSV file into a list of records
    '''
    #deal selecting certain columns and dealing when has no headers
    if select and not has_headers:
        raise RuntimeError ('select argument requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers in case there is one
        headers = next(rows) if has_headers else []

        # If a column was chosen
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select   
        
        records = []   
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
                    print (f"Row {rowno}: Couldn't convert {row}")
                    print (f"Row {rowno}: Reason {row}")


            # Creating dictionary
            if headers:
                record = dict(zip(headers, row))
            
            # Creating tuple instead
            else:
                record = tuple(row)
            records.append(record)

    return records

