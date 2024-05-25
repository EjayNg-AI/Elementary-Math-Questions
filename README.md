# GCE O Level Elementary Mathematics Questions

This project contains questions based on the Singapore-Cambridge GCE O Level ELementary Mathematics syllabus, as approved by Singapore's Ministry of Education (MOE).

The project helps you organize and manage a collection of Elementary Mathematics questions written in LaTeX. It allows you to categorize questions, select a random subset of questions from each category, and generate a LaTeX document that can be compiled into a PDF. The answers to each question are appended at the end of the document, and the numbering of questions and answers is continuous across categories.

## Project Structure

```
Elementary-Math-Questions/
├── data/
│   ├── wordproblems/
│   │   ├── Q1.txt
│   │   ├── Q1ans.txt
│   │   └── ...
│   ├── fractions/
│   │   ├── Q1.txt
│   │   └── ...
│   └── ratios/
│       ├── Q1.txt
│       └── ...
├── templates/
│   └── template.tex
├── output/
│   └── sample_output.pdf
├── categories.yaml
├── generate_questions.py
└── requirements.txt
```

- `data/`: Contains subdirectories for each category of questions. Each question is stored in its own text file with a `.txt` extension (example `Q1.txt`), and each answer is stored in a corresponding file with "ans" appended to the filename (example `Q1ans.txt`). This naming convention must be strictly followed and both question and answer is to be stored in the same subdiectory. Each question and the corresponding answer is typed out in LaTex. If images are used, they are to be referenced using the relative path `data/fractions/imagefilename.png`. For example:
    ```latex
    The figure below shows an empty container. 
    All edges meet at $90^\circ$ angles. 
    When the tap is turned on, water flows into the container at a rate of 2.01 litres per minute. How much time is needed to fill the container completely?
    \begin{figure}[h]
    \centering
    \includegraphics{data/wordproblems/01.png}
    \end{figure}
    ```
  - `fractions/`, `ratios/`, `percentages/`: Subdirectories for different categories of questions.
- `templates/`: Contains the LaTeX template for the output document.
  - `template.tex`: LaTeX template file.
- `output/`: Directory where the generated PDF will be saved.
  - `sample_output.pdf`: Example of a generated PDF file.
- `categories.yaml`: YAML file containing the list of categories and their descriptions.
- `generate_questions.py`: The main script for generating the LaTeX document and compiling it into a PDF.
- `requirements.txt`: Lists the required Python packages.

## Installation

1. Clone the repository:

    ```sh
    # Clone using the web URL. 
    git clone https://github.com/EjayNg-AI/Elementary-Math-Questions.git

    # Use a password-protected SSH key.
    git clone git@github.com:EjayNg-AI/Elementary-Math-Questions.git

    cd Elementary-Math-Questions
    ```

2. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Ensure you have LaTeX installed on your system to compile the `.tex` files to PDF. To ensure that LaTeX is installed on your system, you can follow these steps based on your operating system:

    ### For Windows

    1. **Download and Install MiKTeX**:
       - Go to the [MiKTeX website](https://miktex.org/download) and download the installer for Windows.
       - Run the installer and follow the installation instructions.

    2. **Verify Installation**:
       - Open Command Prompt and type `pdflatex --version`.
       - If LaTeX is installed, you should see the version information.

    ### For macOS

    1. **Download and Install MacTeX**:
       - Go to the [MacTeX website](https://www.tug.org/mactex/mactex-download.html) and download the MacTeX installer.
       - Run the installer and follow the installation instructions.

    2. **Verify Installation**:
       - Open Terminal and type `pdflatex --version`.
       - If LaTeX is installed, you should see the version information.

    ### For Linux

    1. **Install TeX Live**:
       - Open your terminal.
       - On Debian-based distributions (e.g., Ubuntu), use the following command:

         ```sh
         sudo apt-get install texlive-full
         ```

       - On Red Hat-based distributions (e.g., Fedora), use the following command:

         ```sh
         sudo dnf install texlive-scheme-full
         ```

    2. **Verify Installation**:
       - Open Terminal and type `pdflatex --version`.
       - If LaTeX is installed, you should see the version information.

    ### Verifying LaTeX Installation

    Regardless of your operating system, you can verify that LaTeX is installed by running the following command in your terminal or command prompt:

    ```sh
    pdflatex --version
    ```

    You should see output similar to this, which indicates that LaTeX is installed:

    ```
    pdfTeX 3.14159265-2.6-1.40.20 (TeX Live 2019)
    kpathsea version 6.3.1
    Copyright 2019 Peter Breitenlohner (eTeX)/Han The Thanh (pdfTeX).
    There is NO warranty.  Redistribution of this software is covered by the terms of both the pdfTeX copyright and the Lesser GNU General Public License.
    For more information about these matters, see the file named COPYING and the pdfTeX source.
    Primary author of pdfTeX: Han The Thanh (pdfTeX).
    Compiled with libpng 1.6.36; using libpng 1.6.36
    Compiled with zlib 1.2.11; using zlib 1.2.11
    Compiled with xpdf version 4.01
    ```

    If you encounter any issues during installation, refer to the documentation provided by the respective LaTeX distribution (MiKTeX, MacTeX, or TeX Live) for troubleshooting steps.

## Configuration

Create a `categories.yaml` file with the following structure to specify the categories and their descriptions:

```yaml
categories:
  - directory: wordproblems
    description: Word Problems (using calculator)
  - directory: fractions
    description: Fractions
  - directory: ratios
    description: Ratios
```

## Usage

Run the script to generate the PDF:

```sh
python generate_questions.py
```

The script will prompt you to enter the number of questions for each category. You can enter:

- A specific number to select that many questions randomly from the category.
- `all` to select all questions from the category.
- `0` to skip the category.

Example:

```
How many questions from the category 'fractions'? (Enter 'all' to select all questions, or '0' to skip this category): 5
How many questions from the category 'ratios'? (Enter 'all' to select all questions, or '0' to skip this category): all
How many questions from the category 'percentages'? (Enter 'all' to select all questions, or '0' to skip this category): 0
```

The generated PDF will be saved in the `output/` directory with a filename that includes the current date and time, ensuring it is unique and valid on any operating system.

## LaTeX Template

You can customize the LaTeX template used for the output document by modifying `templates/template.tex`. The placeholder `% QUESTIONS_PLACEHOLDER` will be replaced with the selected questions and answers.

Example `template.tex`:

```latex
\documentclass[12pt]{article} 
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}

\begin{document}

\section*{Elementary Mathematics Questions}

% QUESTIONS_PLACEHOLDER

\end{document}
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the CC0-1.0 License. For more details, see the [LICENSE](LICENSE) file.