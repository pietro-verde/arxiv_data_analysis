
def barplot(ax, labels, width, title, barsize, font_size, invert_y=False):
    for index, value in enumerate(width):
        ax.text(value, index, " "+str(value),va='center',size=font_size)
    if invert_y:
        ax.invert_yaxis()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.barh(labels,width,height=barsize)
    ax.set_title(title)
    ax.set(xticklabels=[])
    ax.set_xticks([])
