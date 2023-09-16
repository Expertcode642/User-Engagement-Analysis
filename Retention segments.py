# Define the retention segments based on number of sessions
def get_retention_segment(row):
    if row['Sessions'] >= 32: # 32 is mean of sessions
        return 'Frequent Users'
    else:
        return 'Occasional Users'

# Create a new column for retention segments
data['Retention Segment'] = data.apply(get_retention_segment, axis=1)

# Print the updated DataFrame
print(data)

# Calculate the average bounce rate for each retention segment
segment_bounce_rates = data.groupby('Retention Segment')['Bounce Rate'].mean().reset_index()

# Create a bar chart to visualize the average bounce rates by retention segment
bar_fig = px.bar(segment_bounce_rates, x='Retention Segment', y='Bounce Rate',
                 title='Average Bounce Rate by Retention Segment',
                 labels={'Retention Segment': 'Retention Segment', 'Bounce Rate': 'Average Bounce Rate'})

bar_fig.show()

# Count the number of users in each retention segment
segment_counts = data['Retention Segment'].value_counts()

# Define the pastel colors
colors = ['#FFB6C1', '#87CEFA']

# Create a pie chart using Plotly
fig = px.pie(segment_counts, 
             values=segment_counts.values, 
             names=segment_counts.index, 
             color=segment_counts.index, 
             color_discrete_sequence=colors,
             title='User Retention Rate')

# Update layout and show the chart
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(showlegend=False)
fig.show()
