#!/usr/bin/env python3
"""
Script to split AI_KNOWLEDGE_BASE.txt into organized markdown files
"""

import re
import os

# Article definitions
ARTICLES = {
    1: {"title": "Wilcom Embroidery Software Guide", "folder": "software-guides", "filename": "wilcom-embroidery-guide.md"},
    2: {"title": "Wilcom ESA Files and Font Mapping", "folder": "software-guides", "filename": "wilcom-esa-files.md"},
    3: {"title": "Wilcom File Conversion Best Practices", "folder": "software-guides", "filename": "wilcom-file-conversion.md"},
    4: {"title": "Hatch Embroidery Software Guide", "folder": "software-guides", "filename": "hatch-embroidery-guide.md"},
    5: {"title": "Hatch Font Mapping for Purchased Alphabets", "folder": "software-guides", "filename": "hatch-font-mapping.md"},
    6: {"title": "Bernina Embroidery Software Guide", "folder": "software-guides", "filename": "bernina-embroidery-guide.md"},
    7: {"title": "Bernina ART Machines Guide", "folder": "software-guides", "filename": "bernina-art-machines.md"},
    8: {"title": "PE-Design Software Guide", "folder": "software-guides", "filename": "pe-design-guide.md"},
    9: {"title": "Melco DesignShop Guide", "folder": "software-guides", "filename": "melco-designshop-guide.md"},
    10: {"title": "Embrilliance Software Guide", "folder": "software-guides", "filename": "embrilliance-guide.md"},
    11: {"title": "Embird Software Guide", "folder": "software-guides", "filename": "embird-guide.md"},
    12: {"title": "ESA File Format Technical Reference", "folder": "technical-reference", "filename": "esa-file-format.md"},
    13: {"title": "Embroidery Analyzer App Documentation", "folder": "app-documentation", "filename": "embroidery-analyzer.md"},
    14: {"title": "DST Optimizer Tool Documentation", "folder": "app-documentation", "filename": "dst-optimizer.md"},
    15: {"title": "Embroidery Previewer App Documentation", "folder": "app-documentation", "filename": "embroidery-previewer.md"},
    16: {"title": "Design Combiner Tool Documentation", "folder": "app-documentation", "filename": "design-combiner.md"},
}

def read_knowledge_base():
    """Read the knowledge base file"""
    with open('AI_KNOWLEDGE_BASE.txt', 'r', encoding='utf-8') as f:
        return f.read()

def extract_article(content, article_num):
    """Extract a single article from the knowledge base"""
    # Find the article section
    separator = "=" * 80

    # Split by major separators
    sections = content.split(separator)

    # Article starts with number. (e.g., "1. WILCOM")
    pattern = f"\n{article_num}\\. "

    article_text = ""
    for i, section in enumerate(sections):
        if re.search(pattern, section):
            # Found the start - get this section and the next one (the content)
            if i + 1 < len(sections):
                article_text = sections[i] + separator + sections[i + 1]
                break

    return article_text.strip()

def convert_to_markdown(article_text, article_info):
    """Convert article to markdown with artapli.shop links"""

    # Header
    markdown = f"""# {article_info['title']}

> **Part of the [Artapli Machine Embroidery Knowledge Base](https://artapli.shop)**
> Professional embroidery fonts, designs, and resources

---

"""

    # Process the content
    lines = article_text.split('\n')

    for line in lines:
        # Skip the separator lines and article number
        if line.startswith('=') or re.match(r'^\d+\. [A-Z]', line.strip()):
            continue

        # Convert section headers (ALL CAPS followed by colon)
        if line.strip() and line.strip().isupper() and ':' in line:
            markdown += f"\n## {line.strip().replace(':', '')}\n\n"
        # Keep other lines as-is
        elif line.strip():
            markdown += line + '\n'
        else:
            markdown += '\n'

    # Footer with links
    markdown += f"""

---

## 📚 Additional Resources

- **Visit our store**: [artapli.shop](https://artapli.shop)
- **Browse embroidery fonts**: [artapli.shop/collections/embroidery-fonts](https://artapli.shop/collections/embroidery-fonts)
- **View all guides**: [Back to Knowledge Base](../../README.md)

---

*Last updated: 2026-02-07*
*Questions? Contact us through [artapli.shop](https://artapli.shop)*
"""

    return markdown

def main():
    """Main function to split and convert all articles"""
    print("Reading AI_KNOWLEDGE_BASE.txt...")
    content = read_knowledge_base()

    print(f"Processing {len(ARTICLES)} articles...\n")

    for article_num, article_info in ARTICLES.items():
        print(f"Processing Article {article_num}: {article_info['title']}...")

        # Extract article
        article_text = extract_article(content, article_num)

        if not article_text:
            print(f"  ⚠️  Warning: Could not extract article {article_num}")
            continue

        # Convert to markdown
        markdown = convert_to_markdown(article_text, article_info)

        # Write to file
        output_path = f"docs/{article_info['folder']}/{article_info['filename']}"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"  ✓ Created: {output_path}")

    print("\n✅ All articles processed successfully!")

if __name__ == "__main__":
    main()
