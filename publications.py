import argparse
import bibtexparser

parser = argparse.ArgumentParser()
parser.add_argument("bibtex")
args = parser.parse_args()

with open(args.bibtex) as bibtex_file:
    bib_database = bibtexparser.bparser.BibTexParser(common_strings=True).parse_file(bibtex_file)

#print('<div class="campusviews-timetable">')
for entry in bib_database.entries:
    if 'year' not in entry:
        print(f"""year missing: {entry['title']}""")
    if 'publisher' not in entry:
        entry['publisher'] = entry['organization']
    if 'booktitle' not in entry:
        entry['booktitle'] = entry['journal']

    url = (f"""<div class="col-md-2">
                        <a class="link external" href="{entry['url']}">Link</a>
                    </div>""" if 'url' in entry else '')
    bibtex = (f"""<div class="col-md-2">
                        <a class="link download" href="{entry['bibtex']}">Bibtex</a>
                    </div>""" if 'bibtex' in entry else '')
    pdf = (f"""<div class="col-md-2">
                        <a class="link download" href="{entry['pdf']}">PDF</a>
                    </div>""" if 'pdf' in entry else '')

    html_article = (
    f"""<article class="agenda--teaser ">
    <div class="agenda--description bg-grey-light">
        <div class="bg-green fac" style="height: 0.31em; width:100%;">&nbsp;</div>
        <div class="box-sides" style="position: relative; padding-left: 1em; padding-right: 1em; padding-bottom: 1em; margin-top: 1em;">
            <div class="title-table">
                <h4>
                    <small>{entry['booktitle']} | {entry['publisher']} | {entry['year']}</small><br>
                    {entry['title']}
                </h4>
            </div>

            <p class="hidden-xs">
                </p><div class="row">
                    <div class="col-md-6">
                        <span><i class="fa fa-user" style="display: inline-block;width:30px;"></i>{entry['author']}</span>
                    </div>
                    {url}
                    {bibtex}
                    {pdf}
                </div>
            <p></p>
        </div>
    </div>
</article>""")
    print(html_article)
#print('</div>')
