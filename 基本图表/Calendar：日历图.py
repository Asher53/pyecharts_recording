import datetime
import random

from pyecharts import options as opts
from pyecharts.charts import Calendar

import numpy as np


def calendar_base() -> Calendar:
    begin = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 12, 31)

    # [['2017-01-01', 3109], ['2017-01-02', 15849], ['2017-01-03'
    data = [
        [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
        for i in range((end - begin).days + 1)
    ]

    # print(np.shape(data))
    # print(data)

    c = (
        Calendar()
        .add("2017", data, calendar_opts=opts.CalendarOpts(range_="2017"))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Calendar-2017年微信步数情况"),
            visualmap_opts=opts.VisualMapOpts(
                max_=20000,
                min_=500,
                orient="horizontal",  # 图标是横放还是竖放
                is_piecewise=True,  # 拆不拆分图标
                pos_top="230px",
                pos_left="100px",
            ),
        )
    )
    return c

c = calendar_base()
c.render('Calendar.html')