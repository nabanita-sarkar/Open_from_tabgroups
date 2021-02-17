import webbrowser as wb
import re
import os
from rich.console import Console


def tabs():
    console = Console(color_system="truecolor")

    console.print(
        "✨ [#FFFF5F on #FF5FFF] Enter the tab group list [/#FFFF5F on #FF5FFF] 📜: ")

    tab_group_list = []
    while True:
        line = input()
        if line:
            tab_group_list.append(line)
        else:
            break
    tab_group_list = '\n'.join(tab_group_list)

    tab_numbers = re.findall("[^\s]+", tab_group_list)

    tabs = []
    for i in range(len(tab_numbers)):
        if i % 2 != 0:
            x = tab_numbers[i]
            tabs.append(x)

    edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

    wb.register('chrome', None, wb.BackgroundBrowser(edge_path))

    os.system(r'"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"')

    for i in tabs:
        wb.get("windows-default").open(i, new=1)
