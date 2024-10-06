import pandas as pd

# Data
nodes = ["node1.chaitu.net", "node2.chaitu.net", "node3.chaitu.net", "node5.chaitu.net", "node4.chaitu.net"]
status = ["insync", "insync", "insync", "insync", "insync"]
health = ["drifted", "insync", "insync", "insync", "fine"]

# Creating the DataFrame
df = pd.DataFrame({"nodes": nodes, "status_app": status, "health_app": health})

# Filtering rows where 'status_app' and 'health_app' are drifted
status_app_drifted = df[df["status_app"] != "insync"]
print("status dataframe")
print(status_app_drifted)
health_app_drifted = df[df["health_app"] != "insync"]

for index, row  in status_app_drifted.iterrows():
    print(f" {index} {row['nodes']}  {row['status_app']}")

# print(health_app_drifted)
# Printing the DataFrame
# print(df)

# Writing to text file in a consolidated format
# with open('consolidated_drifted.txt', 'w') as f:
#     f.write("status_app\n")
#     f.write("---------------------------\n")
#     for _, row in status_app_drifted.iterrows():
#         f.write(f"{row['nodes']}  {row['status_app']}\n")
#
#     f.write("\nhealth_app\n")
#     f.write("---------------------------\n")
#     for _, row in health_app_drifted.iterrows():
#         f.write(f"{row['nodes']}  {row['health_app']}\n")

# print("Consolidated drifted values written to 'consolidated_drifted.txt'")
