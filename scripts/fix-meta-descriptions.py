#!/usr/bin/env python3
"""Generate missing meta descriptions for articles by extracting the first real paragraph."""
import re, glob, os

docs_dir = '/home/alex/Repos/esim-knowledge/docs/articles'
files = sorted(glob.glob(f'{docs_dir}/**/*.md', recursive=True))

generated = 0
already = 0
skipped = 0

for fpath in files:
    if '/kids/' in fpath:
        continue
    
    with open(fpath) as f:
        original = f.read()
    
    # Skip if already has a proper description (not breadcrumb)
    fm_match = re.match(r'^---\s*\n(.*?)\n---', original, re.DOTALL)
    if not fm_match:
        skipped += 1
        continue
    
    fm = fm_match.group(1)
    existing = re.search(r'^description:\s*"(.+)"', fm, re.MULTILINE)
    if existing:
        # Check if it's a breadcrumb (starts with eUICC.tech > or 🏠)
        d = existing.group(1)
        if not d.startswith('eUICC.tech >') and not d.startswith('🏠'):
            already += 1
            continue
    
    # Find the first real paragraph after the h1
    body = original[fm_match.end():]
    body = re.sub(r'^#\s+.*\n', '', body)  # Remove h1
    
    desc = ''
    for line in body.split('\n'):
        line = line.strip()
        # Skip empty, headings, blockquotes, list items, breadcrumbs, and metadata lines
        if not line:
            continue
        if line.startswith('#'):
            continue
        if line.startswith('>'):
            continue
        if line.startswith('- ') or line.startswith('* '):
            continue
        if 'eUICC.tech' in line and '>' in line:
            continue  # Breadcrumb
        if line.startswith('| '):
            continue  # Table
        if line.startswith('```'):
            continue
        if line.startswith('[') and line.endswith(')'):
            continue  # Pure link
        
        # Clean markdown formatting
        clean = re.sub(r'\*\*(.*?)\*\*', r'\1', line)
        clean = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', clean)
        clean = re.sub(r'`([^`]+)`', r'\1', clean)
        clean = re.sub(r'\{[^}]*\}', '', clean)  # Jekyll Liquid tags
        clean = clean.strip()
        
        if len(clean) > 40:
            if len(clean) > 160:
                clean = clean[:157]
                last_space = clean.rfind(' ')
                if last_space > 80:
                    clean = clean[:last_space] + '…'
            desc = clean
            break
    
    if not desc:
        skipped += 1
        name = fpath.replace(docs_dir + '/', '')
        print(f'SKIP: {name} (no suitable paragraph)')
        continue
    
    # Insert or replace description
    fm_lines = fm.split('\n')
    
    # Remove existing breadcrumb description
    fm_lines = [l for l in fm_lines if not (l.startswith('description:') and ('eUICC.tech >' in l or '🏠' in l))]
    
    # Find insertion point (after title/layout lines)
    insert_pos = 0
    for i, line in enumerate(fm_lines):
        s = line.strip()
        if s.startswith(('layout:', 'title:', 'parent:', 'nav_order:')):
            insert_pos = i + 1
    
    if existing and not (existing.group(1).startswith('eUICC.tech >') or existing.group(1).startswith('🏠')):
        # Has a real description already
        pass  # Shouldn't reach here due to continue above
    else:
        # Insert new description
        fm_lines.insert(insert_pos, f'description: "{desc}"')
    
    new_fm = '\n'.join(fm_lines)
    new_text = original.replace(fm, new_fm)
    
    with open(fpath, 'w') as f:
        f.write(new_text)
    
    name = fpath.replace(docs_dir + '/', '')
    print(f'OK: {name}')
    print(f'    "{desc}"')
    generated += 1

print(f'\nGenerated: {generated} | Already had: {already} | Skipped: {skipped}')
