from calcs import Calculate
from summary import compute_summary
import pandas as pd
import plotly.express as px
import math
from sample_variance import mean
from summary import compute_percentile
from statistics import *

nums = sorted([-22.0, -20.0, -19.5, -16.5, -14.0, -11.5, -5.5, -1.0, -0.5, 0.5, 2.0, 3.0, 5.0, 6.5, 7.0, 8.0, 8.5, 16.5, 17.5, 22.0])

df = pd.DataFrame(nums)

print(nums)
print(compute_summary(nums))
print(compute_percentile(nums))

########### functionality for box plot ###########
#
d_f = pd.DataFrame(dict(
    linear=nums,
)).melt(var_name="quartilemethod")

fig = px.box(d_f, y="value", facet_col="quartilemethod", boxmode="overlay", points='all')

fig.update_traces(quartilemethod="linear", jitter=0, col=1)

fig.show()


