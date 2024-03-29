import pyecharts.options as opts
from example.commons import  Faker
from pyecharts.charts import Line


def line_base() -> Line:
    c = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Line-基本示例"))
    )
    return c

c = line_base()
c.render('tt.html')