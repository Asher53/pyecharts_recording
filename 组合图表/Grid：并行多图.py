'''
Grid-上下布局
'''
from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Scatter


def grid_vertical() -> Grid:
    bar = (
        Bar()
            .add_xaxis(Faker.choose())
            .add_yaxis("商家A", Faker.values())
            .add_yaxis("商家B", Faker.values())
            .set_global_opts(title_opts=opts.TitleOpts(title="Grid-Bar"))
    )
    line = (
        Line()
            .add_xaxis(Faker.choose())
            .add_yaxis("商家A", Faker.values())
            .add_yaxis("商家B", Faker.values())
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Grid-Line", pos_top="48%"),
            legend_opts=opts.LegendOpts(pos_top="48%"),
        )
    )

    grid = (
        Grid()
            .add(bar, grid_opts=opts.GridOpts(pos_bottom="60%"))
            .add(line, grid_opts=opts.GridOpts(pos_top="60%"))
    )
    return grid


'''
Grid-左右布局
'''


def grid_horizontal() -> Grid:
    scatter = (
        Scatter()
            .add_xaxis(Faker.choose())
            .add_yaxis("商家A", Faker.values())
            .add_yaxis("商家B", Faker.values())
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Grid-Scatter"),
            legend_opts=opts.LegendOpts(pos_left="20%"),
        )
    )
    line = (
        Line()
            .add_xaxis(Faker.choose())
            .add_yaxis("商家A", Faker.values())
            .add_yaxis("商家B", Faker.values())
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Grid-Line", pos_right="5%"),
            legend_opts=opts.LegendOpts(pos_right="20%"),
        )
    )

    grid = (
        Grid()
            .add(scatter, grid_opts=opts.GridOpts(pos_left="55%"))
            .add(line, grid_opts=opts.GridOpts(pos_right="55%"))
    )
    return grid


c = grid_horizontal()
c.render('tt.html')
