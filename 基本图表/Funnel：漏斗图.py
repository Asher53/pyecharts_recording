from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Funnel, Page


def funnel_sort_ascending() -> Funnel:
    c = (
        Funnel()
            .add(
            "商品",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            sort_="ascending",
            label_opts=opts.LabelOpts(position="inside"),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="Funnel-Sort（ascending）"))
    )
    return c


c = funnel_sort_ascending()
c.render('Funnel.html')
