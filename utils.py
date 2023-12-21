import matplotlib.patches as patches
import seaborn as sns

def plot_policy(ax, _policy, num_rows=4, num_cols=4):

    size = 0.2

    # outer rectangle of the GridWorld
    rect = patches.Rectangle((0, 1), num_rows, num_cols, linewidth=1, edgecolor='k', facecolor='none')   
    ax.add_patch(rect)

    for row in range(num_rows):
        for col in range(num_cols):

            state = row * num_rows + col
            _directions = _policy[state]

            # rectangle for each square
            if state in [5, 7, 11, 12, 15]:
                rect = patches.Rectangle((col, num_rows-row), 1, 1, linewidth=0.5, edgecolor='k', facecolor='gray', alpha=0.3) 
            else:
                rect = patches.Rectangle((col, num_rows-row), 1, 1, linewidth=0.5, edgecolor='k', facecolor='none') 

            ax.add_patch(rect)  

            if 0 in _directions:
                ax.arrow(col+0.5, num_rows-row+0.5, -size,    0, head_width=0.05, edgecolor='b') # left
            if 1 in _directions:
                ax.arrow(col+0.5, num_rows-row+0.5,    0, -size, head_width=0.05, edgecolor='b') # down
            if 2 in _directions:
                ax.arrow(col+0.5, num_rows-row+0.5,  size,    0, head_width=0.05, edgecolor='b') # right
            if 3 in _directions:
                ax.arrow(col+0.5, num_rows-row+0.5,    0,  size, head_width=0.05, edgecolor='b') # up

def plot_values(ax, _values, num_rows=4, num_cols=4):

    _values_2d = _values.reshape(num_rows, num_cols)
    sns.heatmap(_values_2d, ax=ax, cmap="flare", annot=_values_2d, annot_kws={'fontsize': 10}, fmt='.3f', cbar=False)

def format_plot(ax):

    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)