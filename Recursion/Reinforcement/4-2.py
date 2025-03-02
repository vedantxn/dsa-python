import matplotlib.pyplot as plt
import matplotlib.patches as patches

'''
 Draw the recursion trace for the computation of power(2,5), usingthe
 traditional function implemented in Code Fragment 4.11.
'''
#code fragment:
def power(x, n):
    # Compute the value x**n for integer n.
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

# List of recursive calls in order from the initial call to the base case
calls = ["power(2,5)", "power(2,4)", "power(2,3)", "power(2,2)", "power(2,1)", "power(2,0)"]

# Set up the plot
plt.figure(figsize=(4,8))
ax = plt.gca()
ax.set_xlim(0, 10)
ax.set_ylim(0, 70)
ax.axis('off')

# Box dimensions and initial position
box_width = 8
box_height = 5
x = 1
y_start = 60
vertical_spacing = 10  # Space between boxes

# Draw each recursive call as a rectangle with text
for i, call in enumerate(calls):
    y = y_start - i * vertical_spacing
    # Draw the rectangle (box) for this recursive call
    rect = patches.Rectangle((x, y), box_width, box_height, 
                             linewidth=1, edgecolor="black", facecolor="lightblue")
    ax.add_patch(rect)
    
    # Add the text inside the rectangle
    plt.text(x + box_width/2, y + box_height/2, call,
             ha="center", va="center", fontsize=12)
    
    # Draw an arrow to the next box (except for the last box)
    if i < len(calls) - 1:
        # Arrow from bottom center of current box to top center of next box
        plt.annotate("", 
                     xy=(x + box_width/2, y - 2), 
                     xytext=(x + box_width/2, y), 
                     arrowprops=dict(arrowstyle="->", lw=2))

# Add a title
plt.title("Recursion Trace for power(2,5)", fontsize=14)
plt.show()
