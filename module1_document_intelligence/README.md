# MediTrust - Module 1: Document Intelligence & OCR

## Overview

This module handles medical document processing for the MediTrust project.

It accepts medical documents such as PDF and image files, processes them using OCR, cleans the extracted text, and extracts structured medical information.

## Processing Pipeline

```text
Medical Document
       ↓
File Validation
       ↓
File Upload
       ↓
Document Preprocessing
       ↓
OCR using Tesseract
       ↓
OCR Text Cleaning
       ↓
Medical Information Extraction
       ↓
Structured JSON Response