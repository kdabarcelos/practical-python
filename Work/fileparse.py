# fileparse.py
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter = ','):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers in case there is one
        headers = next(rows) if has_headers else []

        # If a column was chosen
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select   
        
        records = []   
        for row in rows:
            # Skip rows with blanket data
            if not row:    
                continue
            
            # If column indices are selected, pick them out
            if select:
                row = [ row[index] for index in indices]

            # Converting to the correct type
            if types:
                row = [func(val) for func, val in zip(types, row)]

            # Creating dictionary
            if headers:
                record = dict(zip(headers, row))
            
            # Creating tuple instead
            else:
                record = tuple(row)
            records.append(record)

    return records

