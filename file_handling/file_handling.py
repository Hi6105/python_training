import re

def transform_log_string_corrected(log_string):
    pattern = re.compile(
        # Capture the full IP address (e.g., 192.168.0.1, 10.0.0.5)
        r"^(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
        r"\s-\s-\s"                                     # Matches the fixed " - - " separator
        # Capture the full timestamp (e.g., [02/May/2023:12:34:56 -0400])
        # Flexible for: DD (1 or 2 digits), Mon (3+ letters), YYYY (4 digits),
        # HH:MM:SS (1 or 2 digits per component), Timezone Offset (+/- followed by 4 digits)
        r"\[(?P<timestamp>\d{1,2}/[A-Za-z]{3,}/\d{4}:\d{1,2}:\d{1,2}:\d{1,2}\s[+-]\d{4})]"
        # Matches any quoted request string (e.g., "GET /index.html HTTP/1.1", "POST /api/data HTTP/1.1")
        r'\s"[^"]*"'
        # Capture the 3-digit HTTP Status Code (e.g., 200, 404)
        r"\s(?P<status>\d{3})"
        r"\s\d+$"                                    
    )

    match = pattern.search(log_string)

    if match:
        try:
            ip_address = match.group("ip")
            full_timestamp = match.group("timestamp")
            status_code = match.group("status")
            return f"{ip_address}, {full_timestamp}, {status_code}"
        except IndexError as e:
            # these named groups should exist based on the pattern.
            print(f"Error extracting groups from matched log line: {log_string}. Error: {e}")
            return None
    else:
        return None

input_log_file = "log.txt"
output_log_file = "output.txt"

try:
    with open(input_log_file, "r") as infile, \
         open(output_log_file, "a") as outfile: # Use 'a' for append mode, create if not exists

        for line_num, line in enumerate(infile, 1): # Added line_num for better error reporting
            processed_line = transform_log_string_corrected(line.strip())
            if processed_line:
                outfile.write(processed_line + "\n")
            else:
                # Log lines that couldn't be parsed
                print(f"Warning: Could not parse line {line_num} in '{input_log_file}': {line.strip()}")

except FileNotFoundError:
    print(f"Error: Input file '{input_log_file}' not found.")
except IOError as e: # Catches other I/O related errors like permission issues
    print(f"Error performing file operation: {e}")
except Exception as e: # Catch any other unexpected errors
    print(f"An unexpected error occurred: {e}")
