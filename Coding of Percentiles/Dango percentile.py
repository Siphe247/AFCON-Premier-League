from mplsoccer import Radar, FontManager, grid
import matplotlib.pyplot as plt
from highlight_text import fig_text
from PIL import Image, ImageDraw, ImageOps  # add these
from mplsoccer import PyPizza, add_image, FontManager

#Parameters list
params=['Non-Penalty Goals','Non-Penalty xG','Assists','xAG','Shot-Creating\n Actions',
        'Pass Completion\n (%)','Progressive\n Passes','Progressive\n Carries','Successful\n Take-Ons','Progressive Passes\n Received',
        'Tackles','Interceptions','Blocks','Clearances','Aerials\n Won']

#Value list
#Taken from FBREF site
ouattara_values=[67,80,9,18,7,1,9,37,33,53,28,96,87,99,98]

# color for the slices and text
slice_colors = ["#1A78CF"] * 5 + ["#FF9300"] * 5 + ["#D70232"] * 5
text_colors = ["#000000"] * 10 + ["#F2F2F2"] * 5


# instantiate PyPizza class
baker = PyPizza(
    params=params,                  # list of parameters
    background_color="#222222",     # background color
    straight_line_color="#000000",  # color for straight lines
    straight_line_lw=1,             # linewidth for straight lines
    last_circle_color="#000000",    # color for last line
    last_circle_lw=1,               # linewidth of last circle
    other_circle_lw=0,              # linewidth for other circles
    inner_circle_size=20            # size of inner circle
)

# plot pizza
fig, ax = baker.make_pizza(
    ouattara_values,                          # list of values
    figsize=(8, 8.5),                # adjust the figsize according to your need
    color_blank_space="same",        # use the same color to fill blank space
    slice_colors=slice_colors,       # color for individual slices
    value_colors=text_colors,        # color for the value-text
    value_bck_colors=slice_colors,   # color for the blank spaces
    blank_alpha=0.4,                 # alpha for blank-space colors
    kwargs_slices=dict(
        edgecolor="#000000", zorder=2, linewidth=1
    ),                               # values to be used when plotting slices
    kwargs_params=dict(
        color="#F2F2F2", fontsize=11,
        va="center"
    ),                               # values to be used when adding parameter labels
    kwargs_values=dict(
        color="#F2F2F2", fontsize=11,
        zorder=3,
        bbox=dict(
            edgecolor="#000000", facecolor="cornflowerblue",
            boxstyle="round,pad=0.2", lw=1
        )
    )                                #Values to be used when adding parameter-values labels
)

#Add title
fig_text(
    0.515, 1.01, "Dango Ouattara - Brentford",
    size=16, fig=fig,
    ha="center",color="#F2F2F2"
)

#Add Subtitle
fig_text(
    0.5, 0.98,
    "Percentile Rank vs League Wingers | Season 2025-26",
    size=13, fig=fig,
    ha="center", color="#F2F2F2"
)

#Add credits
CREDIT_1="Data: FBREF"
CREDIT_2="Viz: Siphe247"

fig_text(
    0.99, 0.02, f"{CREDIT_1}\n{CREDIT_2}", size=9,
    color="#FFFFFF",
    ha="right"
)

# add text
fig.text(
    0.33, 0.93, "Attacking        Possession          Defending", size=14,
    color="#F2F2F2"
)

# add rectangles
fig.patches.extend([
    plt.Rectangle(
        (0.302, 0.9299), 0.025, 0.021, fill=True, color="#1a78cf",
        transform=fig.transFigure, figure=fig
    ),
    plt.Rectangle(
        (0.482, 0.9299), 0.025, 0.021, fill=True, color="#ff9300",
        transform=fig.transFigure, figure=fig
    ),
    plt.Rectangle(
        (0.679, 0.9299), 0.025, 0.021, fill=True, color="#d70232",
        transform=fig.transFigure, figure=fig
    ),
])

#Add Dango Ouattara image
ax1 = fig.add_axes([0.4478, 0.4315, 0.13, 0.13])  # make width & height equal for a circle
ax1.axis('off')

# open and make circular
img = Image.open('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/AFCON/Dango Ouattara/Dango.png')

# choose final size of the circular thumb (adjust as needed)
size = (400, 400)

# fit image to square and create circular mask
img = ImageOps.fit(img, size, centering=(0.5, 0.5))  # square crop [web:20][web:23]
mask = Image.new("L", size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, size[0], size[1]), fill=255)

# apply mask as alpha channel
img.putalpha(mask)

# show RGBA image in axes so background outside circle is transparent
ax1.imshow(img)


#Add Brentford badge
ax8=fig.add_axes([0.90,0.89,0.1,0.13])
ax8.axis('off')
img=Image.open('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/AFCON/Dango Ouattara/brentford_logo.png')
ax8.imshow(img)

plt.savefig('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/AFCON/Dango Ouattara/Dango percentile.png', dpi=300, bbox_inches='tight')

