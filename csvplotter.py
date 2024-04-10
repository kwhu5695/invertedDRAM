import os
import pandas as pd
import matplotlib.pyplot as plt

directory = "VAMPIRE/tests/traces/csvs"

N_values = []
total_energy_values = []

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        # Extract N value from the filename
        N = int(filename.split('-')[0])
        # Read the CSV file and extract the "total energy" parameter
        df = pd.read_csv(os.path.join(directory, filename))
        print(df)
        total_energy_line = df.columns[df.columns.str.contains('total energy', case=False)][0]
        total_energy = float(df[total_energy_line].str.extract(r'(\d+.\d+)')[0].values[0])

        # Append N and total energy values to lists
        N_values.append(N)
        total_energy_values.append(total_energy)

plt.plot(N_values, total_energy_values, marker='o', linestyle='-')
plt.xlabel('N')
plt.ylabel('Total Energy')
plt.title('Total Energy vs N')
plt.grid(True)
plt.show()