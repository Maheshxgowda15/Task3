# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/content/netflix_movies.csv'
df = pd.read_csv(file_path)

# Data preparation for pie chart (distribution by type: Movie vs TV Show)
type_count = df['type'].value_counts()

# Data preparation for stacked bar chart (rating distribution by type)
rating_type = df.groupby(['rating', 'type']).size().unstack(fill_value=0)

# Data preparation for line chart (shows by release year)
release_year_count = df['release_year'].value_counts().sort_index()

# Custom Pie Chart for Distribution by Type (Movie vs TV Show)
plt.figure(figsize=(8, 8))
plt.pie(type_count, labels=type_count.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff'], startangle=90, 
        explode=(0.05, 0), shadow=True)
plt.title('Distribution of Netflix Content by Type', fontsize=16, fontweight='bold', color='navy')
plt.tight_layout()
plt.show()

# Stacked Bar Chart for Rating Distribution by Type (Movie vs TV Show)
plt.figure(figsize=(12, 8))
rating_type.plot(kind='bar', stacked=True, color=['#66b3ff','#ff9999'], edgecolor='black', linewidth=1)

# Customizing the stacked bar chart
plt.title('Rating Distribution by Content Type (Movie vs TV Show)', fontsize=18, fontweight='bold', color='navy')
plt.xlabel('Rating', fontsize=14)
plt.ylabel('Number of Shows', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='Type', fontsize=12, title_fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent label overlap
plt.tight_layout()

# Display the stacked bar chart
plt.show()

plt.figure(figsize=(12, 7))
plt.plot(release_year_count.index, release_year_count.values, color='dodgerblue', marker='o', linestyle='-', linewidth=2.5, markersize=8)

# Customizing the line chart with limited x-ticks to avoid overlap
plt.title('Number of Netflix Releases by Year', fontsize=18, fontweight='bold', color='navy')
plt.xlabel('Release Year', fontsize=14, labelpad=15)
plt.ylabel('Number of Releases', fontsize=14, labelpad=15)
plt.xticks(release_year_count.index[::3], rotation=45, fontsize=12)  # Only show every 3rd year to reduce crowding
plt.yticks(fontsize=12)
plt.grid(True, which='both', linestyle='--', alpha=0.7)

# Adding value labels for each data point
for i in range(len(release_year_count)):
    plt.text(release_year_count.index[i], release_year_count.values[i] + 2, str(release_year_count.values[i]), 
             fontsize=10, ha='center', va='bottom', color='black', fontweight='bold')

# Adding legend to the line chart
plt.legend(['Releases per Year'], loc='upper left', fontsize=12)

# Tight layout to ensure everything fits well
plt.tight_layout()

# Display the line chart
plt.show()