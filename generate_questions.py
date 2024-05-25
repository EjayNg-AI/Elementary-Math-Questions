import os
import random
import datetime
import yaml

def get_current_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def list_question_files(category):
    questions_dir = f'data/{category["directory"]}'
    if not os.path.exists(questions_dir):
        print(f"Warning: The category directory '{category['directory']}' does not exist.")
        return []
    
    question_files = [filename for filename in os.listdir(questions_dir) if filename.endswith('.txt') and not filename.endswith('ans.txt')]
    if not question_files:
        print(f"Warning: The category directory '{category['directory']}' is empty.")
    return question_files

def load_file_content(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def pick_random_files(files, num_files=None):
    if num_files is None:
        return files
    return random.sample(files, num_files)

def generate_latex_document(questions_by_category):
    with open('templates/template.tex', 'r') as f:
        template_content = f.read()
    
    questions_text = ""
    answers_text = "\n\\newpage\n\\section*{Answers}\\small\n\\begin{enumerate}\n"
    question_number = 1
    
    for category, questions in questions_by_category.items():
        if questions:  # Only add sections with questions
            questions_text += f"\n\\subsection*{{{category}}}\n\\begin{{enumerate}}\n"
            for question in questions:
                questions_text += f"    \\item[Q{question_number}.] {question['content']}\n"
                answers_text += f"    \\item[Q{question_number}.] {question['answer']}\n"
                question_number += 1
            questions_text += "\\end{enumerate}\n"
    
    answers_text += "\\end{enumerate}\n"
    latex_document = template_content.replace('% QUESTIONS_PLACEHOLDER', questions_text + answers_text)
    return latex_document

def save_latex_document(content, filename):
    with open(filename, 'w') as f:
        f.write(content)

def compile_latex_to_pdf(latex_filename, output_filename):
    os.system(f'pdflatex -output-directory=output {latex_filename}')
    os.rename(f'{latex_filename.replace(".tex", ".pdf")}', f'output/{output_filename}')

def load_categories_from_yaml(yaml_file):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    return data['categories']

"""
Line Break
"""

def main():
    categories = load_categories_from_yaml('categories.yaml')
    questions_by_category = {}
    
    for category in categories:
        question_files = list_question_files(category)
        
        if not question_files:
            continue
        
        user_input = input(f"How many questions from the category '{category['description']}'? (Enter 'all' to select all questions, or '0' to skip this category): ")
        if user_input.lower() == 'all':
            selected_files = pick_random_files(question_files)
        elif user_input == '0':
            print(f"Skipping category '{category['description']}'")
            continue
        else:
            try:
                num_files = int(user_input)
                if num_files > len(question_files):
                    print(f"Warning: Requested number of questions exceeds available questions in '{category['description']}'. Selecting all available questions.")
                    num_files = len(question_files)
                selected_files = pick_random_files(question_files, num_files)
            except ValueError:
                print(f"Error: Invalid input for the number of questions in category '{category['description']}'. Skipping this category.")
                continue
        
        selected_questions = []
        for file in selected_files:
            question_content = load_file_content(os.path.join(f'data/{category["directory"]}', file))
            answer_file = file.replace('.txt', 'ans.txt')
            answer_content = load_file_content(os.path.join(f'data/{category["directory"]}', answer_file)) if os.path.exists(os.path.join(f'data/{category["directory"]}', answer_file)) else "No answer available"
            selected_questions.append({'content': question_content, 'answer': answer_content})
        
        questions_by_category[category['description']] = selected_questions
    
    if not questions_by_category:
        print("No questions selected. Exiting.")
        return

    latex_content = generate_latex_document(questions_by_category)
    latex_filename = 'output/questions.tex'
    timestamp = get_current_timestamp()
    output_filename = f'questions_{timestamp}.pdf'
    save_latex_document(latex_content, latex_filename)
    compile_latex_to_pdf(latex_filename, output_filename)
    print(f"PDF generated successfully: output/{output_filename}")

if __name__ == "__main__":
    main()