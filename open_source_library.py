import tkinter as tk
import requests
import webbrowser
from tkinter import ttk
from tkinter import messagebox
from tkinter import*
from tkinter import scrolledtext
class BookSearchApp:
    """
    A GUI application for searching books using Google Books API and providing various filtering options.

    Attributes:
        root (tk.Tk): The main application window.
        label1 (tk.Label): Label for the search input.
        suggestions (list): List of suggested book queries.
        entry (ttk.Combobox): Combobox for entering book queries.
        clear_button (tk.Button): Button to clear the search input.
        filter_label (tk.Label): Label for filtering by category.
        category_var (tk.StringVar): Variable to store the selected category.
        category_menu (ttk.Combobox): Combobox for selecting a book category.
        filter_label_lang (tk.Label): Label for filtering by language.
        language_var (tk.StringVar): Variable to store the selected language.
        language_menu (ttk.Combobox): Combobox for selecting a book language.
        button (tk.Button): Button to initiate the book search.
        result_frame (tk.Frame): Frame to display search results.
        result_text (scrolledtext.ScrolledText): Text widget for displaying search results.
    """
    def __init__(self, root):
        """
        Initialize the BookSearchApp.

        Args:
            root (tk.Tk): The main application window.
        """
        self.root = root
        self.root.title("Search Books")
        self.label1 = tk.Label(self.root, text="           Enter Book or Author's Name", font=("straight", 10, "bold"))
        self.label1.grid(row=3, column=0)
        self.suggestions = ["Python Programming", "Machine Learning", "Data Science", "Java Programming","Artificial Intelligence", "Django Framework", "Web Development", "Tamil Literature", "Mathematics"]
        self.entry = ttk.Combobox(self.root, values=self.suggestions)
        self.entry.grid(row=3, column=1)
        self.entry.set("")
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_entry)
        self.clear_button.grid(row=3, column=2)
        self.filter_label = tk.Label(self.root, text="Filter by Category", font=("straight", 10, "bold"))
        self.filter_label.grid(row=3, column=3)
        self.category_var = tk.StringVar()
        self.category_var.set("All") 
        categories = ["All", "Mathematics", "Physics", "Chemistry", "Programming", "Biology",  "Social Science", "Mythology", "Adventure stories", "Crime", "Fairy tales, fables, folks", "Fantasy", "Historical Fiction", "Horror", "Humor and Satire"]
        self.category_menu = ttk.Combobox(self.root, textvariable=self.category_var, values=categories)
        self.category_menu.grid(row=3, column=4)
        self.filter_label_lang = tk.Label(self.root, text="          Filter by Language          ", font=("straight", 10, "bold"))
        self.filter_label_lang.grid(row=3, column=5)
        self.language_var = tk.StringVar()
        self.language_var.set("All")  
        languages = ["All", "Tamil","English","Hindi","Malayalam", "Kannada", "Telugu", "Sanskrit","Marathi", "Spanish", "French", "German", "Chinese", "Russian", "Japanese", "Other"]
        self.language_menu = ttk.Combobox(self.root, textvariable=self.language_var, values=languages)
        self.language_menu.grid(row=3, column=6)
        self.button = tk.Button(self.root, text="Search", command=self.search)
        self.button.grid(row=3, column=7)
        self.result_frame = tk.Frame(self.root)
        self.result_frame.grid(row=5, column=0, columnspan=8, padx=10, pady=10)
        self.result_text = scrolledtext.ScrolledText(self.result_frame, wrap=tk.WORD, width=60, height=20)
        self.result_text.pack(fill='both', expand=True)
        self.button = tk.Button(self.root, text="  AI Assistant  ", command=self.b)
        self.button.grid(row=6, column=1)
        self.button = tk.Button(self.root, text="      Maps      ", command=self.ul)
        self.button.grid(row=6, column=3) 
        self.button = tk.Button(self.root, text="Instruction Manual", command=self.s)
        self.button.grid(row=6, column=5)
        self.label1 = tk.Label(self.root, text="                                Open Source Library", font=("straight", 10, "bold"))
        self.label1.grid(row=0, column=3)
        self.label1 = tk.Label(self.root, text="   ", font=("straight", 10, "bold"))
        self.label1.grid(row=1, column=3)
        self.label1 = tk.Label(self.root, text="    ", font=("straight", 10, "bold"))
        self.label1.grid(row=4, column=0)
        self.label1 = tk.Label(self.root, text="  ", font=("straight", 10, "bold"))
        self.label1.grid(row=7, column=3)
    def s(self):
        """
        Display instructions on how to use the application.
        """
        messagebox.showinfo('Instructions', "This library makes its books available through Google Library API. Search bar can be provided with either book name or author name or both to get expected results. Filter by Category-It helps to filter your search by choosing the types of books you want. Filter by Language-It helps to prefer the language in which the book should be. Result Frame-You can view the available books in it. To view the book, Click the button just below the details of each book. The book, based on the availability, will be given link to the pdf viewer along with its details and rating in the result frame. AI Assistant-If you forgot the name and author of the book just use this AI and enter the details you know about the book. So that it will help you to identify the book. Also, it can be used to a Generate summary of the book. Maps-It help you to find the libraries around you.")
    def b(self):
        """
        Open a web browser to the OpenAI ChatGPT page.
        """
        webbrowser.open('https://chat.openai.com/')
    def ul(self):
        """
        Open a web browser to search for libraries near the user.
        """
        webbrowser.open('https://www.google.com/maps/search/libraries+near+me')
    def clear_entry(self):
        """
        Clear the search input field.
        """
        self.entry.set("")
    def open_preview(self, link):
        """
        Open a web browser to preview a book.

        Args:
            link (str): The URL of the book preview.
        """
        webbrowser.open(link, new=2)
    def search(self):
        """
        Perform a book search based on user inputs and display results.
        """
        book_name = self.entry.get()
        selected_category = self.category_var.get()
        selected_language = self.language_var.get()
        if selected_category == "All" and selected_language == "All":
            query_url = f'https://www.googleapis.com/books/v1/volumes?q={book_name}'
        elif selected_category == "All":
            query_url = f'https://www.googleapis.com/books/v1/volumes?q={book_name}+lang:{selected_language}'
        elif selected_language == "All":
            query_url = f'https://www.googleapis.com/books/v1/volumes?q={book_name}+subject:{selected_category}'
        else:
            query_url = f'https://www.googleapis.com/books/v1/volumes?q={book_name}+subject:{selected_category}+lang:{selected_language}'
        response = requests.get(query_url)
        if response.status_code == 200:
            data = response.json()
            books = data.get('items', [])
            if books:
                self.result_text.delete('1.0', tk.END) 
                for book in books:
                    volume_info = book.get('volumeInfo', {})
                    title = volume_info.get('title', 'Title not available')
                    authors = ', '.join(volume_info.get('authors', ['Author not available']))
                    preview_link = volume_info.get('previewLink', '')
                    book_text = f"\n\nTitle:{title}\nAuthor(s): {authors}\n"
                    book_text += f"Preview Link: {preview_link}\n\n"
                    self.result_text.insert(tk.END, book_text)
                    if preview_link:
                        preview_button = tk.Button(self.result_text, text=f"Open Preview: {title}", command=lambda link=preview_link: self.open_preview(link))
                        self.result_text.window_create(tk.END, window=preview_button)
            else:
                self.result_text.delete('1.0', tk.END)  
                self.result_text.insert(tk.END, "No results found.")
        else:
            self.result_text.delete('1.0', tk.END)  
            self.result_text.insert(tk.END, "Failed to retrieve book information.")
if __name__ == "__main__":
    root = tk.Tk()
    app = BookSearchApp(root)
root.mainloop()