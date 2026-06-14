#!/usr/bin/env python3
"""Fix nested page divs in storybooks — each page should be a sibling, not nested."""
import re, sys, os, glob

def fix_file(filepath):
    with open(filepath, 'r') as f:
        text = f.read()

    original = text

    # Find <!-- PAGE X: ... --> comments (full comment, not just opening)
    page_comments = list(re.finditer(r'<!-- PAGE \d+:.*?-->', text))
    if len(page_comments) <= 1:
        return False

    # Find the book div
    book_start = text.find('<div class="book">')
    if book_start == -1:
        return False

    # Build new structure:
    # <div class="book">
    #   <!-- PAGE 1 -->
    #   <div class="page ..."> ... </div>
    #   <!-- PAGE 2 -->
    #   <div class="page ..."> ... </div>
    #   ...
    # </div>

    # Extract the content between <div class="book"> and the final </div> before </body>
    # Find the last </div> before </body>
    body_end = text.rfind('</body>')
    if body_end == -1:
        body_end = text.rfind('</html>')

    # Find all </div> before body end — the book close should be the first one from the end
    # that's at the right nesting level
    book_content_start = book_start + len('<div class="book">')

    # Strategy: extract each page's content by finding the opening page div
    # and the content until the next page comment (or end)
    pages = []
    for i, comment in enumerate(page_comments):
        comment_end = comment.end()
        # Find the page div after this comment
        page_div = re.search(r'<div class="page[^>]*>', text[comment_end:])
        if not page_div:
            continue
        page_start = comment_end + page_div.start()

        # Find where this page ends: at the next page comment (or the book end)
        if i + 1 < len(page_comments):
            next_comment = page_comments[i + 1]
            # Go backwards from the next comment to find the </div> that closes this page
            # The page content ends just before the next PAGE comment
            page_end = next_comment.start()
        else:
            # Last page — find the book closing </div>
            # Go backwards from body_end
            page_end = body_end

        page_html = text[page_start:page_end]
        pages.append((comment.group(), page_html))

    if not pages:
        return False

    # Build the new book content
    before_book = text[:book_start]
    after_book_start = text[book_content_start:]

    # Build new structure
    new_book = '<div class="book">\n\n'
    for comment_text, page_html in pages:
        new_book += f'{comment_text}\n'
        new_book += page_html.rstrip() + '\n</div>\n\n'

    new_book += '</div>\n'

    # Find where the closing </div> of the book is in the original
    # We take everything after </body> (or </html>) as-is
    if body_end != -1:
        after_body = text[body_end:]
    else:
        after_body = ''

    new_text = before_book + new_book + after_body

    if new_text != original:
        with open(filepath, 'w') as f:
            f.write(new_text)
        return True
    return False


def main():
    kids_dir = '/home/alex/Repos/esim-knowledge/docs/articles/kids'
    files = sorted(glob.glob(os.path.join(kids_dir, 'storybook-*.html')))
    fixed = 0
    errors = []

    for fpath in files:
        try:
            if fix_file(fpath):
                fixed += 1
                pages = len(re.findall(r'<!-- PAGE \d+:', open(fpath).read()))
                print(f'FIXED: {os.path.basename(fpath)} ({pages} pages)')
        except Exception as e:
            errors.append(f'{os.path.basename(fpath)}: {e}')

    print(f'\nFixed: {fixed}/{len(files)}')
    if errors:
        print(f'Errors: {len(errors)}')
        for e in errors:
            print(f'  {e}')

if __name__ == '__main__':
    main()
