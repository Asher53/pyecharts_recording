import json
import os

from pyecharts import options as opts
from pyecharts.charts import Page, Sankey


def sankey_base() -> Sankey:
    nodes = [
        {"name": "category1"},
        {"name": "category2"},
        {"name": "category3"},
        {"name": "category4"},
        {"name": "category5"},
        {"name": "category6"},
    ]

    links = [
        {"source": "category1", "target": "category2", "value": 10},
        {"source": "category2", "target": "category3", "value": 15},
        {"source": "category3", "target": "category4", "value": 20},
        {"source": "category5", "target": "category6", "value": 25},
    ]
    c = (
        Sankey()
        .add(
            "sankey",
            nodes,
            links,
            linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
            label_opts=opts.LabelOpts(position="right"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Sankey-基本示例"))
    )

    return c


c = sankey_base()
c.render('tt.html')