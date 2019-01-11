import argparse
import bibtexparser

parser = argparse.ArgumentParser()
parser.add_argument("bibtex")
args = parser.parse_args()

with open(args.bibtex) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

#print('<div class="campusviews-timetable">')
for entry in bib_database.entries:
    if 'publisher' not in entry:
        entry['publisher'] = entry['organization']
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
                    <div class="col-md-6">
                        <a class="link external" href="{entry['url']}">Link</a>
                    </div>
                </div>
            <p></p>
        </div>
    </div>
</article>""")
    print(html_article)
#print('</div>')
