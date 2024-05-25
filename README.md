## TODO

- query user for athletes to get all the interest athletes
    - athlete can be specified by club membership, or type individualy by ean?

- specify interested competitions
    - type, list, date range, 

- specify criteria
    - viz tabulka

- calculate points

- display table

- export table
    - csv, xls









# Topic of your semestral work


Aplikace vytvořená v streamlit, která získá data o vybraných atletech (zadaných výčtem nebo klubovou příslušností), pomocí scrappování stránky atletika.cz nebo případně pomocí dostupné REST API.

Aplikace data o atletech zpracuje a podle zadaných kritérií vytvoří výslednou tabulku pořadí podle získaných bodů.

Zadaná kritéria pro získání bodů můžou například být: umístění na vybraných závodech, členství v reprezentaci atd.

Výslednou tabulku si bude moct uživatel exportovat do xls nebo csv.

Aplikace bude také obsahovat graf prvních 3 atletů, který zobrazí rozložení získaných bodů.

A dále si bude uživatel moct porovnat n atletů mezi sebou a jejich bodové rozložení zobrazené v grafu.


Describe a function of developed application, necessary dependencies (e.g. utilize requirements.txt), how to start it, and last but not least how to run tests from CLI.



## Sources

https://github.com/streamlit/streamlit/blob/21d5012eeb4741c565dd8f9c819e8761a6b3015b/lib/streamlit/hello/Hello.py
https://streamlit.io/
https://www.atletika.cz/
https://docs.python.org/3/library/datetime.html
https://requests.readthedocs.io/en/latest/
https://docs.python.org/3/library/stdtypes.html#str.format
https://plotly.com/chart-studio-help/stacked-bar-chart/

## TODO

# IMPORTANT TODO: 
Repre body přidat jen aktivní

Start na závodě nezávisle na umístění
Dělené umístění - dočasně přidat varování
Duplicity v rozbězích - dočasně přidat varování

Mosje - pořadí podel bodů - určit bonusové body do grandprix
Za účast v závodě body
Mimo soutěž - přidat tlačítko ignorovat

TODO !!IMPORTANT!! tests
TODO !!IMPORTANT!! report
TODO start v kazdem kole
TODO vyfiltrovat rozbehy, pouze jeden beh na zavod
TODO body za ucast
TODO repre / scm -> atlet api
TODO select athletes
TODO vyber atlety podle jmena
TODO pridat vice kategorii do bodu
TODO nechat uzivatele definovat vlastni kategorie
TODO search for athletes
