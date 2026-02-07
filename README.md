# Artapli Machine Embroidery Knowledge Base

> Technical documentation for machine embroidery software, file formats, and workflows

## About Artapli

Artapli is an independent embroidery design studio focused on manual machine-embroidery digitizing and practical, machine-ready results.

Since 2011, we've been building one of the largest embroidery design collections online — with over **6,000 designs on Etsy** and a curated selection of **4,000+ designs on artapli.shop**. Every design starts with thoughtful illustration, meticulous digitizing, and real test-stitching to ensure files stitch out smoothly and dependably across machines and software.

**Why makers choose Artapli:**

- **Proven experience** — Selling since 2011 with thousands of happy customers and a consistently glowing 5-star rating
- **Quality and detail** — Each design is manually digitized and tested for flawless stitching results
- **Endless variety** — A vibrant, ever-expanding library covering countless themes, styles, and sizes
- **Supportive community** — More than a shop; a space for makers with help, guidance, and inspiration

## What This Repository Is

This GitHub space hosts technical documentation, format references, and tooling notes related to machine embroidery workflows — including how embroidery stitch files behave across common software and machine formats.

### Digitizing Principles

Artapli designs are created as stitch files with attention to:

- Stitch direction and sequencing
- Density, underlay, and pull compensation
- Specialty techniques (when applicable): appliqué, fringe, puffy foam, chain stitch

### Formats and Compatibility

Designs are commonly prepared in major machine formats: **PES, DST, JEF, VP3, EXP, HUS, XXX, VIP**. Notes in this repository focus on preserving stitch intent and avoiding "auto-optimization" behaviors that can damage specialty effects.

### Quality and Testing

Documentation reflects real embroidery constraints: hoop size, fabric behavior, stabilizer use, and machine readability. Guides include safe editing practices and known pitfalls (for example, aggressive optimization or excessive resizing on specialty designs).

## Documentation

### Software Guides

Comprehensive documentation for major embroidery software platforms:

1. [Wilcom Embroidery Software Guide](docs/software-guides/wilcom-embroidery-guide.md)
2. [Wilcom ESA Files and Font Mapping](docs/software-guides/wilcom-esa-files.md)
3. [Wilcom File Conversion Best Practices](docs/software-guides/wilcom-file-conversion.md)
4. [Hatch Embroidery Software Guide](docs/software-guides/hatch-embroidery-guide.md)
5. [Hatch Font Mapping for Purchased Alphabets](docs/software-guides/hatch-font-mapping.md)
6. [Bernina Embroidery Software Guide](docs/software-guides/bernina-embroidery-guide.md)
7. [Bernina ART Machines Guide](docs/software-guides/bernina-art-machines.md)
8. [PE-Design Software Guide](docs/software-guides/pe-design-guide.md)
9. [Melco DesignShop Guide](docs/software-guides/melco-designshop-guide.md)
10. [Embrilliance Software Guide](docs/software-guides/embrilliance-guide.md)
11. [Embird Software Guide](docs/software-guides/embird-guide.md)

### Stitching Guides

Technical guides for machine setup, stitch sequences, and specialty techniques:

- [General Stitching Guidelines](docs/stitching-guides/general-stitching-guidelines.md) - Hooping, stabilization, and best practices
- [Fringe Embroidery Designs](docs/stitching-guides/fringe-embroidery-designs.md) - Setup and finishing for 3D fringe effects
- [Puffy Foam Embroidery](docs/stitching-guides/puffy-foam-embroidery.md) - Material placement and care for 3D foam designs

### Technical Reference

In-depth technical specifications and format documentation:

- [ESA File Format Technical Reference](docs/technical-reference/esa-file-format.md)

### Application Documentation

Documentation for Artapli's embroidery web applications and tools:

- [Embroidery Lettering Tool](docs/app-documentation/embroidery-lettering-tool.md) - **Browser-based lettering application (industry first!)**
- [Embroidery Analyzer App](docs/app-documentation/embroidery-analyzer.md)
- [DST Optimizer Tool](docs/app-documentation/dst-optimizer.md)
- [Embroidery Previewer App](docs/app-documentation/embroidery-previewer.md)

## Coverage

### Supported File Formats
- DST (Universal embroidery format)
- PES (Brother/Babylock)
- JEF (Janome)
- HUS (Husqvarna Viking)
- EXP (Melco/Bernina)
- VIP (Pfaff)
- XXX (Singer)
- ESA (Wilcom alphabet format)
- BX (Embrilliance font format)
- EMB (Wilcom native format)

### Topics Covered
- File format conversion and best practices
- Font mapping and lettering workflows
- Design import and export procedures
- Quality preservation during format conversion
- Software-specific workflows and features
- Specialty stitch effects (fringe, puffy, appliqué, chain stitch)
- Machine setup and stitching techniques
- Hooping, stabilization, and material selection
- Technical specifications and limitations
- Troubleshooting common issues

## Official Store and Resources

- **Official Store:** [artapli.shop](https://artapli.shop)
- **Etsy Shop:** [artapli.etsy.com](https://www.etsy.com/shop/Artapli)
- **Lettering Tool:** [artapli.shop/pages/lettering-app](https://artapli.shop/pages/lettering-app)
- **Design Catalog:** [github.com/artapli/Artapli-Design-Catalog](https://github.com/artapli/Artapli-Design-Catalog)

### Connect With Us

- 🌐 [Facebook](https://www.facebook.com/Artapli)
- 📸 [Instagram](https://www.instagram.com/Artapli)
- ▶️ [YouTube](https://www.youtube.com/@Artapli)
- 🎵 [TikTok](https://www.tiktok.com/@Artapli)
- 📌 [Pinterest](https://www.pinterest.com/Artapli)

## Structure

```
├── docs/
│   ├── software-guides/      # Platform-specific guides (11 guides)
│   ├── stitching-guides/     # Machine setup and technique guides (3 guides)
│   ├── technical-reference/   # Format specifications
│   └── app-documentation/     # Tool documentation (4 apps)
├── AI_KNOWLEDGE_BASE.txt      # Complete software & technical reference
├── LETTERING_TOOL_GUIDE.txt   # Comprehensive lettering tool documentation
└── README.md                  # This file
```

## Update Policy

Content is updated as tools and workflows evolve. If you spot an error or outdated wording, open an issue or suggest an edit.

## License

This documentation is provided for educational and reference purposes.

---

*This knowledge base is maintained by Artapli to provide technical reference documentation for the machine embroidery community.*

*Last updated: 2026-02-07*
