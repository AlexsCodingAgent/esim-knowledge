#!/usr/bin/env python3
"""Add breadcrumbs and nav links to all 52 articles."""

import os
import re

BASE = "/home/alex/Repos/esim-knowledge/docs/articles"

# Series definitions: folder, section_display, section_path, files in order
SERIES = [
    {
        "folder": "sgp22",
        "section_display": "SGP.22 Consumer RSP",
        "section_path": "/docs/articles/sgp22/",
        "files": [
            "00-sgp22-overview.md",
            "01-rsp-architecture.md",
            "02-inside-the-euicc.md",
            "03-profile-download.md",
            "04-esim-security-pki.md",
            "05-local-profile-management.md",
            "06-developer-interfaces.md",
        ]
    },
    {
        "folder": "sgp32",
        "section_display": "SGP.32 IoT eSIM",
        "section_path": "/docs/articles/sgp32/",
        "files": [
            "07-iot-esim-why.md",
            "08-iot-architecture-im-ipa.md",
            "09-iot-profile-download-packages.md",
            "10-iot-esim-security-dtls.md",
            "11-eim-configuration.md",
            "12-notifications-errors.md",
            "13-iot-device-initialisation.md",
            "14-iot-profile-state-management.md",
            "15-iot-smsds-operations.md",
            "16-iot-functions-reference.md",
        ]
    },
    {
        "folder": "sgp23",
        "section_display": "SGP.23 Test Specifications",
        "section_path": "/docs/articles/sgp23/",
        "files": [
            "17-sgp23-overview.md",
            "18-sgp23-test-infrastructure.md",
            "19-sgp23-lpa-testing.md",
            "20-sgp23-server-testing.md",
            "21-sgp23-certification.md",
        ]
    },
    {
        "folder": "sgp25",
        "section_display": "SGP.25 eUICC Security",
        "section_path": "/docs/articles/sgp25/",
        "files": [
            "22-sgp25-overview.md",
            "23-sgp25-security-requirements.md",
            "24-sgp25-assurance.md",
            "25-sgp25-physical-security.md",
            "26-sgp25-certification.md",
        ]
    },
    {
        "folder": "sgp29",
        "section_display": "SGP.29 EID",
        "section_path": "/docs/articles/sgp29/",
        "files": [
            "27-sgp29-overview.md",
            "28-sgp29-eid-format.md",
            "29-sgp29-assignment.md",
            "30-sgp29-in-protocols.md",
            "31-sgp29-security.md",
        ]
    },
    {
        "folder": "sgp23-1",
        "section_display": "SGP.23-1 eUICC Testing",
        "section_path": "/docs/articles/sgp23-1/",
        "files": [
            "32-sgp23-1-overview.md",
            "33-sgp23-1-architecture.md",
            "34-sgp23-1-test-cases.md",
            "35-sgp23-1-security.md",
            "36-sgp23-1-certification.md",
        ]
    },
    {
        "folder": "sgp26",
        "section_display": "SGP.26 Test Certificates",
        "section_path": "/docs/articles/sgp26/",
        "files": [
            "37-sgp26-overview.md",
            "38-sgp26-hierarchy.md",
            "39-sgp26-profiles.md",
            "40-sgp26-development.md",
            "41-sgp26-crl.md",
        ]
    },
    {
        "folder": "sgp33-3",
        "section_display": "SGP.33 IoT Testing",
        "section_path": "/docs/articles/sgp33-3/",
        "files": [
            "42-sgp33-overview.md",
            "43-sgp33-eim-architecture.md",
            "44-sgp33-eim-test-cases.md",
            "45-sgp33-eim-security.md",
            "46-sgp33-certification.md",
        ]
    },
    {
        "folder": "sgp41",
        "section_display": "SGP.41 In-Factory Provisioning",
        "section_path": "/docs/articles/sgp41/",
        "files": [
            "47-sgp41-overview.md",
            "48-sgp41-architecture.md",
            "49-sgp41-flow.md",
            "50-sgp41-security.md",
            "51-sgp41-practice.md",
        ]
    },
]


def extract_title(content):
    """Extract the article title from the # heading."""
    for line in content.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled"


def make_breadcrumb(title, section_display, section_path):
    """Create the breadcrumb line."""
    return f"**🏠 [eUICC.tech](/) > [{section_display}]({section_path}) > {title}**"


def make_nav_block(prev_title, prev_path, next_title, next_path):
    """Create the navigation block."""
    lines = ["", "---", "", '<div align="center">', ""]
    
    if prev_title:
        lines.append(f'← Previous: [{prev_title}]({prev_path}) · [🏠 Home](/)')
    else:
        lines.append('[🏠 Home](/)')
    
    lines.append("")
    
    if next_title:
        lines.append(f'Next: [{next_title}]({next_path}) →')
    
    lines.extend(["", "</div>"])
    return "\n".join(lines)


def process_series(series):
    folder = series["folder"]
    section_display = series["section_display"]
    section_path = series["section_path"]
    files = series["files"]
    
    # First, read all files and extract titles
    titles = {}
    for fname in files:
        fpath = os.path.join(BASE, folder, fname)
        with open(fpath, "r") as f:
            content = f.read()
        titles[fname] = extract_title(content)
    
    # Now process each file
    for i, fname in enumerate(files):
        fpath = os.path.join(BASE, folder, fname)
        with open(fpath, "r") as f:
            content = f.read()
        
        title = titles[fname]
        
        # Determine prev/next
        prev_title = None
        prev_path = None
        next_title = None
        next_path = None
        
        if i > 0:
            prev_fname = files[i - 1]
            prev_title = titles[prev_fname]
            prev_path = f"{section_path}{prev_fname.replace('.md', '')}"
        
        if i < len(files) - 1:
            next_fname = files[i + 1]
            next_title = titles[next_fname]
            next_path = f"{section_path}{next_fname.replace('.md', '')}"
        
        breadcrumb = make_breadcrumb(title, section_display, section_path)
        nav_block = make_nav_block(prev_title, prev_path, next_title, next_path)
        
        # --- MODIFICATION 1: Add breadcrumb after the # heading ---
        # Find the # heading line. It may or may not have frontmatter before it.
        lines = content.split("\n")
        heading_idx = None
        for j, line in enumerate(lines):
            if line.startswith("# ") and not line.startswith("## "):
                heading_idx = j
                break
        
        if heading_idx is None:
            print(f"WARNING: No # heading found in {fpath}")
            continue
        
        # Check if breadcrumb already exists (skip if so)
        already_has_breadcrumb = False
        for j in range(heading_idx + 1, min(heading_idx + 4, len(lines))):
            if "eUICC.tech" in lines[j] and ">" in lines[j]:
                already_has_breadcrumb = True
                break
        
        if already_has_breadcrumb:
            print(f"SKIP (already has breadcrumb): {fpath}")
            continue
        
        # Insert breadcrumb after heading + any blank line immediately after heading
        insert_idx = heading_idx + 1
        # If there's a blank line right after the heading, put breadcrumb after it
        if insert_idx < len(lines) and lines[insert_idx] == "":
            lines.insert(insert_idx + 1, breadcrumb)
        else:
            lines.insert(insert_idx, "")
            lines.insert(insert_idx + 1, breadcrumb)
        
        # --- MODIFICATION 2: Add navigation before the final --- separator ---
        # Find the last --- that precedes the source citation
        # Pattern: last line is "*Based on GSMA ...", second to last is "---"
        # We want to insert nav_block BEFORE the "---"
        
        # Check if nav already exists
        already_has_nav = False
        for j in range(max(0, len(lines) - 15), len(lines)):
            if "Previous:" in lines[j] or "Next:" in lines[j]:
                # Check this isn't part of existing content
                if "align=\"center\"" in "\n".join(lines[max(0,j-3):j+3]):
                    already_has_nav = True
                    break
        
        if already_has_nav:
            print(f"SKIP (already has nav): {fpath}")
            continue
        
        # Find the last --- line
        last_sep_idx = None
        for j in range(len(lines) - 1, -1, -1):
            if lines[j].strip() == "---":
                last_sep_idx = j
                break
        
        if last_sep_idx is None:
            print(f"WARNING: No '---' separator found in {fpath}")
            # Try to find end of content
            last_sep_idx = len(lines)
        
        # Insert the nav block before the separator
        nav_lines = nav_block.split("\n")
        for k, nav_line in enumerate(nav_lines):
            lines.insert(last_sep_idx + k, nav_line)
        
        # Write back
        new_content = "\n".join(lines)
        with open(fpath, "w") as f:
            f.write(new_content)
        
        print(f"OK: {fpath}")


def main():
    for series in SERIES:
        process_series(series)
    print("\nDone!")


if __name__ == "__main__":
    main()
