import os

# Function to replace the last N 0s with F
def replace_last_N_zeros_with_F(data, N):
    # Split data into fields
    fields = data.split(',')

    # If the 4th and 5th fields are 'WR', modify the last N zeros
    if fields[1] == 'WR':
        # Replace the last N zeros with F
        fields[-1] = 'F' * N + fields[-1][N:]

    # Join fields back into a string
    return ','.join(fields)

# Read original file
with open('0-wr.trace', 'r') as f:
    original_content = f.readlines()

# Create directory to store new files
if not os.path.exists('modified_files'):
    os.makedirs('modified_files')

# Iterate over N from 1 to 127
for N in range(1, 129):
    # Generate modified content
    modified_content = [replace_last_N_zeros_with_F(line.strip(), N) for line in original_content]

    # Write modified content to new file
    filename = '{}-wr.trace'.format(N)
    with open(os.path.join('modified_files_wr', filename), 'w') as f:
        f.write('\n'.join(modified_content))

    # print(f'File {filename} created successfully.')

    print('File created successfully.', filename )
