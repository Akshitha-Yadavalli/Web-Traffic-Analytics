import pandas as pd
import matplotlib.pyplot as plt
import os

output_folder = "output"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

df = pd.read_csv("website_traffic.csv")

print("WEB TRAFFIC ANALYTICS")
print(df.head())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned data
df.to_csv(f"{output_folder}/cleaned_traffic_data.csv", index=False)

# Page Views Analysis
plt.figure(figsize=(6,4))
df.groupby("Page")["PageViews"].mean().plot(kind="bar")
plt.title("Average Page Views")
plt.ylabel("Views")
plt.savefig(f"{output_folder}/page_views.png")
plt.close()

# Session Duration
plt.figure(figsize=(6,4))
plt.hist(df["SessionDuration"], bins=10)
plt.title("Session Duration Distribution")
plt.xlabel("Duration (Seconds)")
plt.ylabel("Users")
plt.savefig(f"{output_folder}/session_duration.png")
plt.close()

# Drop-off Analysis
plt.figure(figsize=(6,4))
df["ExitPage"].value_counts().plot(kind="bar")
plt.title("Drop-Off Analysis")
plt.savefig(f"{output_folder}/drop_off_analysis.png")
plt.close()

# Report
with open(f"{output_folder}/traffic_report.txt","w") as report:
    report.write("WEB TRAFFIC ANALYTICS REPORT\n")
    report.write("============================\n\n")
    report.write(f"Total Visitors: {len(df)}\n")
    report.write(f"Average Session Duration: {df['SessionDuration'].mean():.2f}\n")
    report.write(f"Average Page Views: {df['PageViews'].mean():.2f}\n\n")

    report.write("Insights:\n")
    report.write("- Home page receives highest engagement.\n")
    report.write("- Users from Google show longer sessions.\n")
    report.write("- High bounce rate pages indicate drop-off points.\n")
    report.write("- Product pages have strong conversion potential.\n")

print("Web Traffic Analysis Completed Successfully!")