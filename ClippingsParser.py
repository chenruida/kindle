import os
import sys
import pandas


def main(f_path):
    clippings_txt = open(f_path, 'r', encoding='utf-8').read()
    clippings_list = get_clippings_list(clippings_txt)
    output = []
    for highlight in clippings_list:
        title, author, page, text = parse_highlight(highlight)
        highlight_df = pandas.DataFrame({
            'title': title,
            'author': author,
            'page': page,
            'text': text,
        }, index=[0])
        output.append(highlight_df)
    output_df = pandas.concat(output, ignore_index=True)
    output_df.dropna()
    output_df.drop_duplicates('text','first',True)
    titles = output_df['title'].unique()
    print(titles.size)


def get_clippings_list(txt):
    return txt.split('==========')


def parse_highlight(highlight):
    parts = highlight.split('\n')
    try:
        title = parts[1].split('(')[0].strip()
        author = format_author(
            parts[1][parts[1].find("(")+1:parts[0].find(")")])
        text = parts[4]

        # If page can not be accessed, leave blank and continue with highlight
        try:
            page = parts[2].split(
                '- Your Highlight on page ')[1].split('|')[0].strip()
        except:
            page = ''
        return title, author, page, text
    except IndexError:
        # Skips any malformed highlights
        print(f'{parts} - Index error, skipping line...')


def format_author(author_str):
    '''
    Author in clippings is in format: LastName, First Name
    Take author name and return it as FirstName LastName
    '''
    author = author_str.replace(',', '').split(' ')
    return ' '.join(reversed(author))


if __name__ == "__main__":
    main("/Users/crd/Code/Python/Kindle/My Clippings.txt")
