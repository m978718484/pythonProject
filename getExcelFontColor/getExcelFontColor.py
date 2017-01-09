import xlrd, xlutils
from xlrd import open_workbook
from xlutils.copy import copy
from xlutils.filter import process,XLRDReader,XLWTWriter

def copy2(wb):
    w = XLWTWriter()
    process(
        XLRDReader(wb,'unknown.xls'),
        w
        )
    return w.output[0][1], w.style_list

inBook = xlrd.open_workbook(r"Book1.xls", formatting_info=True, on_demand=True)
inSheet = inBook.sheet_by_index(0)

# Copy the workbook, and get back the style
# information in the `xlwt` format
outBook, outStyle = copy2(inBook)

# Get the style of _the_ cell:    
xf_index = inSheet.cell_xf_index(0, 0)
saved_style = outStyle[xf_index]

saved_style.font.colour_index = 11

#Update the cell, using the saved style as third argument of `write`:
outBook.get_sheet(0).write(0,0,'changed!', saved_style)
outBook.save(r"Book2.xls")