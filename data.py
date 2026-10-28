"""Document AI & OCR Directory — curated registry.

A catalog of tools for turning documents into text and structure: OCR engines,
document parsers (PDF -> markdown/JSON, including LLM-era parsers), layout/table
extraction, and managed Document AI APIs. Entries are public projects/products
catalogued with links — no third-party code is vendored here.

Each entry records: name, organization, category, whether it is open-source,
license, a short note, and a link. Specs reflect public info at time of writing —
verify against the source. Curation is best-effort and community-correctable via
PRs; if a license is uncertain, the entry is omitted.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Category(Enum):
    ocr_engine = "ocr_engine"
    doc_parser = "doc_parser"
    layout_table = "layout_table"
    managed_api = "managed_api"

    @property
    def label(self) -> str:
        return {
            "ocr_engine": "OCR Engines",
            "doc_parser": "Document Parsers (PDF → Markdown/JSON)",
            "layout_table": "Layout & Table Extraction",
            "managed_api": "Managed Document AI APIs",
        }[self.value]


@dataclass(frozen=True)
class Tool:
    name: str
    org: str
    category: Category
    license: str               # "proprietary" for managed APIs
    open_source: bool = False
    note: str = ""
    repo: str = ""
    homepage: str = ""
    tags: tuple[str, ...] = field(default_factory=tuple)


# ---------------------------------------------------------------------------
# Registry — curated, public document-AI / OCR tools (links only).
# ---------------------------------------------------------------------------
TOOLS: list[Tool] = [
    # --- OCR engines ---
    Tool("Tesseract", "Tesseract OCR", Category.ocr_engine, "Apache-2.0",
         open_source=True, repo="https://github.com/tesseract-ocr/tesseract",
         note="The classic open-source OCR engine (100+ languages).",
         tags=("classic", "multilingual")),
    Tool("PaddleOCR", "PaddlePaddle (Baidu)", Category.ocr_engine, "Apache-2.0",
         open_source=True, repo="https://github.com/PaddlePaddle/PaddleOCR",
         note="Practical OCR toolkit incl. detection, recognition, and structure.",
         tags=("toolkit", "structure")),
    Tool("EasyOCR", "Jaided AI", Category.ocr_engine, "Apache-2.0",
         open_source=True, repo="https://github.com/JaidedAI/EasyOCR",
         note="Ready-to-use OCR for 80+ languages with a simple API.",
         tags=("easy", "multilingual")),
    Tool("docTR", "Mindee", Category.ocr_engine, "Apache-2.0",
         open_source=True, repo="https://github.com/mindee/doctr",
         note="Deep-learning OCR (detection + recognition) in TF/PyTorch.",
         tags=("deep-learning",)),
    Tool("Kraken", "Benjamin Kiessling", Category.ocr_engine, "Apache-2.0",
         open_source=True, repo="https://github.com/mittagessen/kraken",
         note="OCR/HTR for historical and handwritten documents.",
         tags=("handwriting", "historical")),
    Tool("OCRmyPDF", "OCRmyPDF", Category.ocr_engine, "MPL-2.0",
         open_source=True, repo="https://github.com/ocrmypdf/OCRmyPDF",
         note="Adds a searchable text layer to scanned PDFs (Tesseract-based).",
         tags=("pdf", "searchable")),

    # --- Document parsers ---
    Tool("Docling", "IBM", Category.doc_parser, "MIT",
         open_source=True, repo="https://github.com/docling-project/docling",
         note="Parses PDFs/office docs to structured markdown/JSON for AI.",
         tags=("markdown", "tables")),
    Tool("Nougat", "Meta", Category.doc_parser, "MIT",
         open_source=True, repo="https://github.com/facebookresearch/nougat",
         note="Neural OCR for academic PDFs → markdown (math-aware).",
         tags=("academic", "math")),
    Tool("olmOCR", "Allen AI (AI2)", Category.doc_parser, "Apache-2.0",
         open_source=True, repo="https://github.com/allenai/olmocr",
         note="Open toolkit to linearize PDFs for LLM training/RAG.",
         tags=("llm", "linearize")),
    Tool("Unstructured", "Unstructured", Category.doc_parser, "Apache-2.0",
         open_source=True, repo="https://github.com/Unstructured-IO/unstructured",
         note="Preprocess many document types into clean, chunked elements.",
         tags=("ingestion", "rag")),
    Tool("MinerU", "OpenDataLab", Category.doc_parser, "AGPL-3.0",
         open_source=True, repo="https://github.com/opendatalab/MinerU",
         note="High-quality PDF → markdown/JSON (formulas, tables).",
         tags=("pdf", "formulas")),
    Tool("Marker", "Datalab", Category.doc_parser, "GPL-3.0 (commercial avail.)",
         open_source=True, repo="https://github.com/datalab-to/marker",
         note="Fast, accurate PDF → markdown/JSON conversion.",
         tags=("pdf", "fast")),
    Tool("GROBID", "kermitt2", Category.doc_parser, "Apache-2.0",
         open_source=True, repo="https://github.com/kermitt2/grobid",
         note="Extract structured TEI/XML from scholarly PDFs.",
         tags=("scholarly", "tei")),

    # --- Layout & table extraction ---
    Tool("Layout-Parser", "Layout Parser", Category.layout_table, "Apache-2.0",
         open_source=True, repo="https://github.com/Layout-Parser/layout-parser",
         note="Deep-learning document layout analysis toolkit.",
         tags=("layout", "detection")),
    Tool("Camelot", "Atlan", Category.layout_table, "MIT",
         open_source=True, repo="https://github.com/atlanhq/camelot",
         note="Extract tables from text-based PDFs.",
         tags=("tables", "pdf")),
    Tool("pdfplumber", "Jeremy Singer-Vine", Category.layout_table, "MIT",
         open_source=True, repo="https://github.com/jsvine/pdfplumber",
         note="Extract text, tables, and shapes from PDFs precisely.",
         tags=("tables", "text")),
    Tool("Table Transformer", "Microsoft", Category.layout_table, "MIT",
         open_source=True, repo="https://github.com/microsoft/table-transformer",
         note="Detection + structure recognition for tables (DETR-based).",
         tags=("tables", "detr")),

    # --- Managed Document AI APIs ---
    Tool("AWS Textract", "AWS", Category.managed_api, "proprietary",
         note="Managed OCR + forms/tables extraction.",
         homepage="https://aws.amazon.com/textract", tags=("aws", "forms")),
    Tool("Azure AI Document Intelligence", "Microsoft", Category.managed_api, "proprietary",
         note="Managed document parsing (prebuilt + custom models).",
         homepage="https://azure.microsoft.com/products/ai-services/ai-document-intelligence",
         tags=("azure", "custom-models")),
    Tool("Google Document AI", "Google", Category.managed_api, "proprietary",
         note="Managed document parsing/OCR on Google Cloud.",
         homepage="https://cloud.google.com/document-ai", tags=("gcp",)),
    Tool("LlamaParse", "LlamaIndex", Category.managed_api, "proprietary",
         note="GenAI-native parser for complex PDFs/tables.",
         homepage="https://www.llamaindex.ai/llamaparse", tags=("genai", "rag")),
    Tool("Mistral OCR", "Mistral AI", Category.managed_api, "proprietary",
         note="OCR API that returns structured, markdown-friendly output.",
         homepage="https://docs.mistral.ai/capabilities/document", tags=("api", "markdown")),
    Tool("Reducto", "Reducto", Category.managed_api, "proprietary",
         note="High-accuracy document ingestion API for complex docs.",
         homepage="https://reducto.ai", tags=("api", "accuracy")),
    Tool("Mathpix", "Mathpix", Category.managed_api, "proprietary",
         note="OCR specialized for math, science, and tables (to LaTeX/MD).",
         homepage="https://mathpix.com", tags=("math", "latex")),
    Tool("Upstage Document Parse", "Upstage", Category.managed_api, "proprietary",
         note="Document parsing/OCR API with layout preservation.",
         homepage="https://www.upstage.ai", tags=("api", "layout")),
    Tool("LLMWhisperer", "Unstract", Category.managed_api, "proprietary",
         note="Text extraction that preps documents for LLMs.",
         homepage="https://unstract.com/llmwhisperer", tags=("api", "llm-prep")),
    Tool("FastOCR", "FastOCR", Category.managed_api, "proprietary",
         note="Hosted OCR for images and PDFs, with searchable PDF output and a public API.",
         homepage="https://fastocr.org", tags=("ocr", "api", "pdf")),
]
