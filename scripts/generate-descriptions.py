#!/usr/bin/env python3
"""Generate missing meta descriptions for articles without them."""
import re, glob, os

docs_dir = '/home/alex/Repos/esim-knowledge/docs/articles'
files = sorted(glob.glob(f'{docs_dir}/**/*.md', recursive=True))

generated = 0
already_had = 0
skipped = 0

for fpath in files:
    if '/kids/' in fpath:
        continue
    
    with open(fpath, 'r') as f:
        text = f.read()
    
    # Already has description?
    if re.search(r'^description:\s*', text, re.MULTILINE):
        already_had += 1
        continue
    
    # Extract frontmatter
    fm_match = re.match(r'^(---\s*\n)(.*?)(\n---)', text, re.DOTALL)
    if not fm_match:
        skipped += 1
        continue
    
    before_fm = fm_match.group(1)
    fm_content = fm_match.group(2)
    after_fm = fm_match.group(3) + text[fm_match.end():]
    
    # Find first substantive paragraph after frontmatter
    body = text[fm_match.end():]
    body = re.sub(r'^#\s+.*\n', '', body)  # Remove h1
    
    desc = ''
    for line in body.split('\n'):
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('>'):
            continue
        if line.startswith('- ') or line.startswith('* '):
            continue
        # Clean markdown
        clean = re.sub(r'\*\*(.*?)\*\*', r'\1', line)
        clean = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', clean)
        clean = re.sub(r'`([^`]+)`', r'\1', clean)
        clean = clean.strip()
        if len(clean) > 30:
            if len(clean) > 160:
                clean = clean[:157]
                last_space = clean.rfind(' ')
                if last_space > 100:
                    clean = clean[:last_space] + '…'
            desc = clean
            break
    
    if not desc:
        skipped += 1
        print(f'SKIP (no paragraph): {fpath}')
        continue
    
    # Insert description into frontmatter after title/layout lines
    fm_lines = fm_content.split('\n')
    insert_pos = 0
    for i, line in enumerate(fm_lines):
        s = line.strip()
        if s.startswith('layout:') or s.startswith('title:') or s.startswith('parent:') or s.startswith('nav_order:'):
            insert_pos = i + 1
    
    fm_lines.insert(insert_pos, f'description: "{desc}"')
    new_fm = '\n'.join(fm_lines)
    new_text = before_fm + new_fm + after_fm
    
    with open(fpath, 'w') as f:
        f.write(new_text)
    
    short = fpath.replace(docs_dir + '/', '')
    print(f'OK: {short}')
    print(f'    "{desc}"')
    generated += 1

print(f'\nGenerated: {generated} | Already had: {already_had} | Skipped: {skipped}')
