# SEOMaker

## Overview
SEOMaker is a tool designed to simplify and accelerate the process of creating SEO-optimized product descriptions for e-commerce team at my company. It provides a GUI interface to structure descriptions, paraphrase content, and generate HTML templates.  This tool sped up the process of generating descriptions by over 80%.

---

## Features
- **GUI Interface**: Intuitive tabs for creating new descriptions, manual paraphrasing, and API-powered paraphrasing.
- **SEO Content Generation**: Quickly generate structured HTML templates for product descriptions.
- **Paraphrasing Tools**:
  - Extract and refine text from HTML.
  - Replace or modify paragraphs while maintaining proper formatting.
- **Customizable Templates**:
  - Multiple layout options (center, left-aligned, mini).
  - Automatic image filename generation based on product names.
- **User-Friendly Design**: Includes separators, headers, and polished HTML structure.

---

## How It Works
1. **Input Product Description**: Write or paste the product details into the input field.
2. **Select Template**: Choose from predefined layouts to structure your description.
3. **Generate HTML**: Fill the template with content, automatically generate image filenames, and output polished HTML code.
4. **Paraphrase Content**: Use manual or API-based tools to paraphrise your descriptions.

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
   - Connect with external paraphrasing APIs (e.g., Claude) for automated text modification.

---


## Example Interaction

1. Input product description:
   ```text
   Logitech Mouse
   This wireless mouse offers ergonomic design and long battery life.
   ```
2. Select layout (e.g., center).
3. Generated HTML:
   ```html
   <div class="col-3-3 m-center">
       <p>
           This wireless mouse offers ergonomic design and long battery life.
       </p>
       <img src="https://media.komputronik.pl/pl-komputronik/img/opisy_produktow/content/SEO/logitech-mouse-1.jpg" alt=""/>
   </div>
   ```

---

## TODO
- Batch Paraphrase Generation: Automatically generate multiple paraphrases based on product features and export to excel.
- Add Tests: Cover core functionalities such as text processing, template generation, and API integration.
- Graceful Handling of Missing API Key: Allow the application to run normally when the API key file is missing and display a message indicating the absence of connection instead of raising an error.

---

