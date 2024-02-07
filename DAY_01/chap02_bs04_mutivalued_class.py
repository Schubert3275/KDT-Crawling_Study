"""
class 속성 예제
"""
from bs4 import BeautifulSoup

tr = """
<table>
    <tr class="passed a b c" id="row1 example"><td>t1</td></tr>
    <tr class="failed" id="row2"><td>t2</td></tr>
</table>
"""

table = BeautifulSoup(tr, "html.parser")
for row in table.find_all('tr'):  # find_all('tag'): 해당 tag를 모두 찾아서 리스트로 리턴
    print(row.attrs)
