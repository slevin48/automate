# Automate Excel, Word and the Web using Python

## Excel Sheet Splitter [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/slevin48/automate/main/app.py)

Streamlit app to split sheets of Excel files: https://excel-splitter-48.herokuapp.com/

https://user-images.githubusercontent.com/12418115/142772669-d9f2b3bc-2587-4308-a5a6-fd38699ef159.mp4

## Excel automation
https://openpyxl.readthedocs.io/en/stable/

We get the price of real estate in Paris 14 from the following gist: https://gist.github.com/slevin48/05c0d4f348f0f10870a0fa721cfcb1b1

Adding manually a second sheet selecting only the surface and price

```python
workbook = xl.load_workbook('dvf14_chart.xlsx')
sheet_2 = workbook['Sheet2']
```
![immo_chart](dvf14_chart.png)

```python
chart = ScatterChart()
chart.title = "Scatter Chart"
chart.style = 13
chart.y_axis.title = 'Price'
chart.x_axis.title = 'Surface'

xvalues = Reference(sheet_2, min_col = 1, min_row = 2, max_row = sheet_1.max_row)
values = Reference(sheet_2, min_col=2, min_row=1, max_row=mr)
series = Series(values, xvalues,title_from_data=True)
series.marker.symbol = "diamond"
series.marker.graphicalProperties.solidFill = "0000FF" # Marker filling
series.marker.graphicalProperties.line.solidFill = "0000FF" # Marker outline
series.graphicalProperties.line.noFill = True  # hide lines
chart.series.append(series)

sheet_2.add_chart(chart, "D2")
workbook.save('dvf14_chart.xlsx')
```

## Extracting chart

Access Excel through COM

```
pip install pywin32
```
```python
input_file = "C:/Users/.../Book1.xlsx"
output_image = "C:/Users/.../chart.png"
operation = win32com.client.Dispatch("Excel.Application")
operation.Visible = 0
operation.DisplayAlerts = 0
workbook_bis = operation.Workbooks.Open(input_file)
sheet_bis = operation.Sheets(1)
```

And use Pillow to grab image
https://pillow.readthedocs.io/en/stable/index.html
```
pip install pillow
```
iterate over all of the chart objects in the spreadsheet (if there are more than one) and save them in the specified location as such:

```python
for x, chart in enumerate(sheet_bis.Shapes):
    chart.Copy()
    image = ImageGrab.grabclipboard()
    image.save(output_image, 'png')
    pass
workbook_bis.Close(True)
operation.Quit()
```

![chart](immo_chart.png)

## Create Word report
https://python-docx.readthedocs.io/en/latest/

```python
from docx import Document

document = Document()
document.add_heading('Report on Excel and Word automation', 0)

...

document.save('dvf14_report.docx')
```

![report](report.png)

## Scraping web pages with Beautiful Soup

[Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

Example: [web_automate.ipynb](web_automate.ipynb)
```python
import requests as rq
from bs4 import BeautifulSoup

URL = 'https://realpython.github.io/fake-jobs/'
page = rq.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
res = soup.find_all(class_ = "location")
open("location1.txt","w").write(res[0].text)
```

*Next: Web automation with Selenium*

## Resources

- https://automatetheboringstuff.com/2e/chapter13/
- https://realpython.com/beautiful-soup-web-scraper-python/
- https://xkcd.com/1205/

![is_it_worth_the_time](is_it_worth_the_time.png)
