import math
import random

from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Page, Polar


def polar_scatter0() -> Polar:
    data = [(i, random.randint(1, 100)) for i in range(101)]
    c = (
        Polar()
        .add("", data, type_="scatter", label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Polar-Scatter0"))
    )
    return c



c = polar_scatter0()
c.render('tt.html')