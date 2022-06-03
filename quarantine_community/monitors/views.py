import io

import pandas as pd
from django.shortcuts import render
import mimetypes

# Create your views here.
from django.utils.encoding import escape_uri_path
from django.views.generic import TemplateView
from utils.stat import water_summary_df, filename_today, get_water_df_formatted
from io import StringIO, BytesIO
import xlsxwriter
from django.http import HttpResponse


class DrinkingWaterView(TemplateView):
    template_name = 'monitors/drinking-water/index.html'

    def get_context_data(self, **kwargs):
        context = super(DrinkingWaterView, self).get_context_data(**kwargs)
        ret_df, chart_x, chart_y = water_summary_df(write=True)
        headers = ret_df.columns
        matrix = ret_df.values.tolist()
        total_needed = sum(chart_y)
        context.update(locals())
        return context


def drinking_water_download_view(request):
    # Create an in-memory output file for the new workbook.
    output = io.BytesIO()

    # Even though the final file will be in memory the module uses temp
    # files during assembly for efficiency. To avoid this on servers that
    # don't allow temp files, for example the Google APP Engine, set the
    # 'in_memory' Workbook() constructor option as shown in the docs.
    # workbook = xlsxwriter.Workbook(output)
    # worksheet = workbook.add_worksheet(name='瓶装水统计')

    # Get some data to write to the spreadsheet.
    ret_df = get_water_df_formatted()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')

    ret_df.to_excel(writer, sheet_name='瓶装水统计', index=False, na_rep='NaN')

    # Auto-adjust columns' width
    for column in ret_df:
        column_width = 18
        col_idx = ret_df.columns.get_loc(column)
        writer.sheets['瓶装水统计'].set_column(col_idx, col_idx, column_width)
    writer.save()
    output.seek(0)

    # Set up the Http response.
    filename = filename_today().name
    # print(filename)
    # filename = 'django-simple.xlsx'
    response = HttpResponse(
        output,
        # content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        content_type=mimetypes.guess_type(filename),
    )

    response['Content-Disposition'] = f"attachment; filename={escape_uri_path(filename)}"
    # return the response
    return response
