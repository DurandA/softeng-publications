import argparse
import io
import logging
from hashlib import sha256
from zipfile import ZipFile

import bibtexparser
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

parser = argparse.ArgumentParser()
parser.add_argument("bibtex")
parser.add_argument("--zipfile", help="save bibtex entries")
args = parser.parse_args()

with open(args.bibtex) as bibtex_file:
    parser = BibTexParser(common_strings=True)
    parser.customization = convert_to_unicode
    bib_database = bibtexparser.load(bibtex_file, parser=parser)

#print('<div class="campusviews-timetable">')
zfio = io.BytesIO()
with ZipFile(zfio, mode='w') as zf:
    for entry in bib_database.entries:
        if 'year' not in entry:
            raise Warning("year missing in {}".format(entry['title']))

        db = BibDatabase()
        db.entries.append(entry)

        bibtexio = io.StringIO()
        bibtexparser.dump(db, bibtexio)
        digest = sha256(bibtexio.getvalue().encode('utf-8')).hexdigest()
        filename = digest + '.txt'
        zf.writestr(filename, bibtexio.getvalue())
        bibtexio.close()

        publisher = next(entry[k] for k in ['publisher', 'organization'] if k in entry)
        booktitle = next(entry[k] for k in ['booktitle', 'journal'] if k in entry)

        url = (f"""<div class="col-md-2">
                            <a class="link external" href="{entry['url']}">Link</a>
                        </div>""" if 'url' in entry else '')
        pdf = (f"""<div class="col-md-2">
                            <a class="link download" href="assets/public/files/research/publications/pdf/{entry['pdf']}">PDF</a>
                        </div>""" if 'pdf' in entry else '')

        html_article = (
f"""<article class="agenda--teaser ">
    <div class="agenda--description bg-grey-light">
        <div class="bg-green fac" style="height: 0.31em; width:100%;">&nbsp;</div>
        <div class="box-sides" style="position: relative; padding-left: 1em; padding-right: 1em; padding-bottom: 1em; margin-top: 1em;">
            <div class="title-table">
                <h4>
                    <small>{booktitle} | {publisher} | {entry['year']}</small><br>
                    {entry['title']}
                </h4>
            </div>

            <p class="hidden-xs">
                </p><div class="row">
                    <div class="col-md-6">
                        <span><i class="fa fa-user" style="display: inline-block;width:30px;"></i>{entry['author']}</span>
                    </div>
                    {url}
                    <div class="col-md-2">
                        <a class="link download" href="assets/public/files/research/publications/bibtex/{filename}">Bibtex</a>
                    </div>
                    {pdf}
                </div>
            <p></p>
        </div>
    </div>
</article>""")
        print(html_article)
#print('</div>')

if args.zipfile:
    with open(args.zipfile, "wb") as f: # use `wb` mode
        f.write(zfio.getvalue())
