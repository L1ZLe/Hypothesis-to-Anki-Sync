#!/usr/bin/env python3
import fitz  # PyMuPDF
import pandas as pd
import sys

def extract_highlights(pdf_path):
    doc = fitz.open(pdf_path)
    flashcards = []
    
    for page in doc:
        annotations = page.annots()
        if annotations:
            for annot in annotations:
                if annot.type[0] == 8:  # Highlight type
                    highlight_text = page.get_text("text", clip=annot.rect)
                    comment = annot.info.get("content", "").strip()
                    flashcards.append({
                        "Front": highlight_text.strip(),
                        "Back": comment if comment else None
                    })
    
    return flashcards

def save_to_csv(flashcards, output_file):
    df = pd.DataFrame(flashcards)
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"Saved {len(df)} flashcards to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 pdf_to_anki.py input.pdf output.csv")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    output_csv = sys.argv[2]
    
    flashcards = extract_highlights(pdf_path)
    save_to_csv(flashcards, output_csv)
