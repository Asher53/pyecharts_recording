from example.commons import  Faker
from pyecharts.charts import Line
from pyecharts.charts import Bar
import pyecharts.options as opts



def overlap_line_scatter() -> Bar:
    x = Faker.choose()
    bar = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Overlap-line+scatter"))
    )
    line = (
        Line()
        .add_xaxis(x)
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
    )
    bar.overlap(line)
    return bar

overlap_line_scatter().render('tt.html')