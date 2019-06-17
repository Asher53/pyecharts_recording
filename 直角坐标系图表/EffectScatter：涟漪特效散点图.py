from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import EffectScatter
from pyecharts.globals import SymbolType


def effectscatter_base() -> EffectScatter:
    c = (
        EffectScatter()
        .add_xaxis(Faker.choose())
        .add_yaxis("", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="EffectScatter-基本示例"))
    )
    return c


c = effectscatter_base()
c.render('tt.html')