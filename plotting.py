from bokeh.models.annotations import Tooltip
from motion_detector import df
from bokeh.plotting import figure, output_file, show
import pandas
from bokeh.models import HoverTool, ColumnarDataSource


df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnarDataSource()

p = figure(
    x_axis_type="datetime",
    height=300,
    width=500,
    sizing_mode="stretch_width",
    title="Motion Graph",
)

p.yaxis.minor_tick_line_color = None
p.yaxis[0].ticker.desired_num_ticks = 1
hover = HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
p.add_tools(hover)

q = p.quad(left="Start", right="End", bottom=0, top=1, color="green", source=df)

output_file("Graph.html")
show(p)
