# SEOMaker

## Overview
SEOMaker is a tool designed to simplify and accelerate the process of creating SEO-optimized product descriptions for e-commerce team at my company. It provides a GUI interface to structure descriptions, paraphrase content, and generate HTML templates.  This tool sped up the process of generating descriptions by over 80%.

---

## Features
- **GUI Interface**: Intuitive tabs for creating new descriptions, manual paraphrasing, and API-powered paraphrasing.
- **Template Generation**: Quickly generate structured HTML templates for product descriptions.
- **Paraphrasing Tools**:
  - Extract text from HTML.
  - Replace or modify paragraphs manually or automatically with LLM.
- **Flexibility**:
  - Multiple layout options (center, left-aligned, mini).
  - Automatic image filename generation based on product names.


---

## Installation

Download the most recent release.

---

## Usage

### Tabs:
1. **New Description**:
   - Input description given by the copywriter.
   - Select a template layout.
   - Generate HTML.
2. **Paraphrase Manual**:
   - Extract text from HTML.
   - Modify content and reinsert it into the structure.
3. **Paraphrase API**:
   - Send the message to Anthropic Claude for automated text modification.

---


## Example Interaction

[screenshots] 
---

## TODO
- Batch Paraphrase Generation: Automatically generate multiple paraphrases based on product features and export to excel.
- Add Tests: Cover core functionalities such as text processing, template generation, and API integration.
- Graceful Handling of Missing API Key: Allow the application to run normally when the API key file is missing and display a message indicating the absence of connection instead of raising an error.

---

