# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 12:13:44 2024

@author: mysticmarks
"""
import tkinter as tk
from tkinter import ttk, messagebox
import json
from vectara_cli.core import VectaraClient

class VectaraGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Vectara Client GUI")
        self.geometry("600x500")
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style(self)
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TEntry", font=("Arial", 12))

        # Customer ID
        self.customer_id_var = tk.StringVar()
        ttk.Label(self, text="Customer ID:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.customer_id_var).grid(row=0, column=1, padx=5, pady=5)

        # API Key
        self.api_key_var = tk.StringVar()
        ttk.Label(self, text="API Key:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.api_key_var).grid(row=1, column=1, padx=5, pady=5)

        # Corpus ID
        self.corpus_id_var = tk.StringVar()
        ttk.Label(self, text="Corpus ID:").grid(row=2, column=0, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.corpus_id_var).grid(row=2, column=1, padx=5, pady=5)

        # File Path
        self.file_path_var = tk.StringVar()
        ttk.Label(self, text="File Path:").grid(row=3, column=0, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.file_path_var).grid(row=3, column=1, padx=5, pady=5)

        # Document ID
        self.document_id_var = tk.StringVar()
        ttk.Label(self, text="Document ID:").grid(row=4, column=0, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.document_id_var).grid(row=4, column=1, padx=5, pady=5)

        # Metadata
        self.metadata_var = tk.StringVar()
        ttk.Label(self, text="Metadata (JSON):").grid(row=5, column=0, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.metadata_var).grid(row=5, column=1, padx=5, pady=5)

        # Buttons
        ttk.Button(self, text="Set API Keys", command=self.set_api_keys).grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        ttk.Button(self, text="Upload Document", command=self.upload_document).grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        ttk.Button(self, text="Delete Corpus", command=self.delete_corpus).grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        ttk.Button(self, text="Index Document", command=self.index_document).grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        ttk.Button(self, text="Create Corpus", command=self.create_corpus).grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        ttk.Button(self, text="Query", command=self.query).grid(row=11, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    def set_api_keys(self):
        customer_id = self.customer_id_var.get()
        api_key = self.api_key_var.get()
        if not all((customer_id, api_key)):
            messagebox.showerror("Error", "Both Customer ID and API Key are required.")
            return
        messagebox.showinfo("Success", "API Keys set successfully.")

    def upload_document(self):
        customer_id = self.customer_id_var.get()
        api_key = self.api_key_var.get()
        corpus_id = self.corpus_id_var.get()
        file_path = self.file_path_var.get()
        document_id = self.document_id_var.get()
        metadata_str = self.metadata_var.get()

        if not all((customer_id, api_key, corpus_id, file_path)):
            messagebox.showerror("Error", "Customer ID, API Key, Corpus ID, and File Path are required.")
            return

        try:
            metadata = json.loads(metadata_str)
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid JSON format for metadata.")
            return

        try:
            vectara_client = VectaraClient(customer_id, api_key)
            response = vectara_client.upload_document(corpus_id, file_path, document_id, metadata)
            messagebox.showinfo("Success", f"Upload successful: {response}")
        except Exception as e:
            messagebox.showerror("Error", f"Upload failed: {str(e)}")

    def delete_corpus(self):
        customer_id = self.customer_id_var.get()
        api_key = self.api_key_var.get()
        corpus_id = self.corpus_id_var.get()

        if not all((customer_id, api_key, corpus_id)):
            messagebox.showerror("Error", "Customer ID, API Key, and Corpus ID are required.")
            return

        try:
            vectara_client = VectaraClient(customer_id, api_key)
            response, success = vectara_client.delete_corpus(corpus_id)
            if success:
                messagebox.showinfo("Success", "Corpus deleted successfully.")
            else:
                messagebox.showerror("Error", f"Failed to delete corpus: {response}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete corpus: {str(e)}")

    def index_document(self):
        customer_id = self.customer_id_var.get()
        api_key = self.api_key_var.get()
        corpus_id = self.corpus_id_var.get()
        document_id = self.document_id_var.get()
        metadata_str = self.metadata_var.get()

        if not all((customer_id, api_key, corpus_id, document_id)):
            messagebox.showerror("Error", "Customer ID, API Key, Corpus ID, and Document ID are required.")
            return

        try:
            metadata = json.loads(metadata_str)
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid JSON format for metadata.")
            return

        try:
            vectara_client = VectaraClient(customer_id, api_key)
            response, success = vectara_client.index_document(corpus_id, document_id, metadata)
            if success:
                messagebox.showinfo("Success", "Document indexed successfully.")
            else:
                messagebox.showerror("Error", f"Document indexing failed: {response}")
        except Exception as e:
            messagebox.showerror("Error", f"Document indexing failed: {str(e)}")

    def create_corpus(self):
        customer_id = self.customer_id_var.get()
        api_key = self.api_key_var.get()
        corpus_id = self.corpus_id_var.get()
        metadata_str = self.metadata_var.get()

        if not all((customer_id, api_key, corpus_id)):
            messagebox.showerror("Error", "Customer ID, API Key, and Corpus ID are required.")
            return

        try:
            metadata = json.loads(metadata_str)
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid JSON format for metadata.")
            return

        try:
            vectara_client = VectaraClient(customer_id, api_key)
            response = vectara_client.create_corpus(corpus_id, metadata)
            messagebox.showinfo("Success", f"Corpus created successfully: {response}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create corpus: {str(e)}")

    def query(self):
        customer_id = self.customer_id_var.get()
        api_key = self.api_key_var.get()
        corpus_id = self.corpus_id_var.get()
        query_text = self.file_path_var.get()

        if not all((customer_id, api_key, corpus_id, query_text)):
            messagebox.showerror("Error", "Customer ID, API Key, Corpus ID, and Query Text are required.")
            return

        try:
            vectara_client = VectaraClient(customer_id, api_key)
            response = vectara_client.query(query_text, corpus_id)
            messagebox.showinfo("Query Results", f"Query Response: {response}")
        except Exception as e:
            messagebox.showerror("Error", f"Query failed: {str(e)}")

def main():
    gui = VectaraGUI()
    gui.mainloop()

if __name__ == "__main__":
    main()
