import sys

def decode_address(address):
    # Add your decoding logic here
    # For now, return dummy values

    # upper 16 indexes rows
    # next 2 bits decide bank
    address_int = int(address, 16)

    # Extract upper 16 bits for row and next 2 bits for bank
    row = (address_int >> 16) & 0xFFFF
    bank = (address_int >> 14) & 0b11
    # print(row, bank)
    return bank, row

def convert_format_A_to_B(line):
    # Split the line into components
    parts = line.strip().split()

    # Extract relevant components
    tick = int(parts[2])
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

     # Convert cacheline data to binary and count the number of 1's
    binary_data = bin(int(cachelinedata, 16))[2:]
    count_ones = binary_data.count('1')

    # Check if inversion is needed based on the condition
    if count_ones > 256:
        inverted_data = hex(int(binary_data, 2) ^ (2**512 - 1))[2:].zfill(128)
        cachelinedata = inverted_data.upper()

    # Construct the line in format B
    new_line = f"{tick},{command},{bank},{row},{cachelinedata}\n"

    # Check if the current interaction is with a new bank,row pair
    # Add activation line for the new bank,row pair
    activation_line = f"{tick-1},ACT,{bank},{row}\n"
    precharge_line = f"{tick+1},PRE,{bank}\n"

    return activation_line + new_line + precharge_line

# Input and output file paths
input_file = "gem5/trace.txt"
output_file = "VAMPIRE/gem5.trace"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    # Track previously activated bank,row pairs
    prev_bank_row = set()

    # Process each line in the input file
    for line in infile:
        # Convert format A to format B
        new_line = convert_format_A_to_B(line)
        # Write the converted line to the output file
        outfile.write(new_line)