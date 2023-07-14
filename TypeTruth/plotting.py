import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def plot_bar_chart(df):
    # Create a list of paragraph labels
    para_labels = [f"Paragraph {i+1}" for i in range(len(df))]

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 3))
    bars = plt.bar(para_labels, df['AI Generated Probability'], color='skyblue')
    ax.bar_label(bars)

    plt.xlabel('Paragraphs')
    plt.ylabel('AI Generated Probability (%)')
    plt.title('AI Generated Probability Across Paragraphs')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_stacked_bar_chart(df):
    # Create a list of paragraph labels
    para_labels = [f"Paragraph {i+1}" for i in range(len(df))]
    
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 3.5))
    
    bar1 = plt.bar(para_labels, df['AI Generated Probability'], color='skyblue')
    bar2 = plt.bar(para_labels, df['Human Written Probability'], bottom=df['AI Generated Probability'], color='salmon')

    ax.bar_label(bar1, label_type='center', color='black')
    ax.bar_label(bar2, label_type='center', color='black')

    plt.xlabel('Paragraphs')
    plt.ylabel('Probability (%)')
    plt.title('AI Generated and Human Written Probability Across Paragraphs')
    plt.xticks(rotation=45)
    plt.legend([bar1, bar2], ['AI Generated', 'Human Written'], bbox_to_anchor=(1.05, 1))
    plt.tight_layout()
    plt.show()

def plot_heatmap(df):
    # Replace full sentences with first two words followed by '...'
    df['Content'] = df['Content'].apply(lambda x: ' '.join(x.split()[:2]) + '...')

    # Transpose the dataframe to form a matrix for heatmap
    heatmap_data = df[['Content', 'AI Generated Probability', 'Human Written Probability']].set_index('Content').transpose()

    plt.figure(figsize=(15, 3))
    sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu")
    plt.title('Heatmap of AI Generated and Human Written Probability')
    plt.show()
