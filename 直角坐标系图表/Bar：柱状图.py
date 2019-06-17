from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar



def bar_xyaxis_name() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-XY 轴名称"),
            yaxis_opts=opts.AxisOpts(name="我是 Y 轴"),
            xaxis_opts=opts.AxisOpts(name="我是 X 轴"),
        )
    )
    return c

c = bar_xyaxis_name()
c.render('tt.html')