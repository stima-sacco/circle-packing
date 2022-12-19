import pandas as pd
import circlify
import matplotlib.pyplot as plt

df = pd.DataFrame(
    {
        'Name':['A', 'B', 'C', 'D', 'E', 'F'],
	'Value': [10,2,23,87,12,65]
    }
)

circles = circlify.circlify(
    df['Value'].tolist(),
    show_enclosure = False,
    target_enclosure=circlify.Circle(x=0, y=0, r=1)
)

fig, ax = plt.subplots(figsize=(10,10))

ax.axis('off')

lim = max(
    max(
        abs(circle.x) + circle.r,
        abs(circle.y) + circle.r
    )
    for circle in circles
)

plt.xlim(-lim, lim)
plt.ylim(-lim, lim)

labels = df['Name']

for circle, label in zip(circles, labels):
    x,y,r = circle
    ax.add_patch(plt.Circle((x,y), r, alpha=0.2, linewidth=2, fill=False))
    plt.annotate(
        label,
        (x,y),
        va='center',
        ha='center'
    )

### print circles
##for circle, label in zip(circles, labels):
##    x, y, r = circle
##    ax.add_patch(plt.Circle((x, y), r*0.7, alpha=0.9, linewidth=2, facecolor="#69b2a3", edgecolor="black"))
##    plt.annotate(label, (x,y ) ,va='center', ha='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round', pad=.5))

plt.savefig('image-2.png')
