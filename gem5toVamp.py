def decode_address(address):
    # Add your decoding logic here
    # For now, return dummy values
    bank = 0
    row = 0
    return bank, row

def convert_format_A_to_B(line):
    # Split the line into components
    parts = line.strip().split()
    print(parts)
    # Extract relevant components
    tick = parts[2]
    command = parts[1]
    cachelinedata = parts[3]

    # Convert command from format A to format B
    if command == "READ":
        command = "RD"
    elif command == "WRITE":
        command = "WR"

    # Decode address into bank and row
    address = parts[0]
    bank, row = decode_address(address)

    # Remove "0x" prefix from cachelinedata
    cachelinedata = cachelinedata[2:]

    # Construct the line in format B
    new_line = f"{tick},{command},{bank},{row},{cachelinedata}\n"
    return new_line

# Input and output file paths
input_file = "gem5/trace.txt"
output_file = "VAMPIRE/gem5.trace"

# Open input and output files
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    # Process each line in the input file
    for line in infile:
        # Convert format A to format B
        new_line = convert_format_A_to_B(line)
        # Write the converted line to the output file
        outfile.write(new_line)
