# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:56:12 2024

@author: mysticmarks
"""

import sys
import tkinter as tk
from tkinter import messagebox
from vectara_cli.commands import (
    create_corpus,
    nerdspan_upsert_folder,
    index_text,
    index_document,
    query,
    delete_corpus,
    span_enhance_folder,
    upload_document,
    upload_enriched_text,
    span_text,
    rebel_upsert_folder,
    upload_folder
)
from vectara_cli.utils.create_ui import create_ui
from vectara_cli.utils.config_manager import ConfigManager
from vectara_cli.utils.utils import get_vectara_client, set_api_keys as set_api_keys_main
from vectara_cli.helptexts.help_text import main_help_text

def get_command_mapping():
    command_mapping = {
        "index-document": index_document.main,
        "query": query.main,
        "create-corpus" : create_corpus.main,
        "delete-corpus": delete_corpus.main,
        "span-text": span_text.main,
        "span-enhance-folder": span_enhance_folder.main,
        "upload-document": upload_document.main,
        "upload-enriched-text": upload_enriched_text.main,
        "nerdspan-upsert-folder": nerdspan_upsert_folder.main,
        "rebel-upsert-folder": rebel_upsert_folder.main,
        "index-text": index_text.main,
        "create-ui":create_ui,
        "upload-folder": upload_folder.main
    }
    return command_mapping

def execute_command(command, args):
    try:
        vectara_client = get_vectara_client()
        command_mapping = get_command_mapping()
        if command in command_mapping:
            command_mapping[command](args, vectara_client)
        else:
            messagebox.showerror("Error", f"Unknown command: {command}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def set_api_keys():
    customer_id = customer_id_entry.get()
    api_key = api_key_entry.get()
    if customer_id and api_key:
        set_api_keys_main(customer_id, api_key)
        messagebox.showinfo("Success", "API keys set successfully.")
    else:
        messagebox.showerror("Error", "Both customer ID and API key are required.")

def execute_cli_command():
    cli_command = cli_entry.get()
    if cli_command:
        command_parts = cli_command.split()
        command = command_parts[0]
        args = command_parts[1:]
        execute_command(command, args)
    else:
        messagebox.showerror("Error", "Please enter a CLI command.")

def save_config():
    customer_id = customer_id_entry.get()
    api_key = api_key_entry.get()
    ConfigManager.save_config(customer_id, api_key)
    messagebox.showinfo("Success", "Configuration saved successfully.")

def load_config():
    config = ConfigManager.load_config()
    if config:
        customer_id, api_key = config
        customer_id_entry.insert(0, customer_id)
        api_key_entry.insert(0, api_key)
        messagebox.showinfo("Success", "Configuration loaded successfully.")
    else:
        messagebox.showwarning("Warning", "No saved configuration found.")

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("help", "--help", "-h"):
        main_help_text
        return

    command = sys.argv[1]
    args = sys.argv[2:]
    if command == "set-api-keys":
        if len(args) != 2:
            print("Error: set-api-keys requires exactly 2 arguments: customer_id and api_key.")
            sys.exit(1)
        set_api_keys_main(*args) 
    else:
        execute_command(command, args)

# Create GUI
root = tk.Tk()
root.title("Vectara CLI GUI")

# API Keys Entry
tk.Label(root, text="Customer ID:").grid(row=0, column=0)
customer_id_entry = tk.Entry(root)
customer_id_entry.grid(row=0, column=1)

tk.Label(root, text="API Key:").grid(row=1, column=0)
api_key_entry = tk.Entry(root)
api_key_entry.grid(row=1, column=1)

api_keys_button = tk.Button(root, text="Set API Keys", command=set_api_keys)
api_keys_button.grid(row=2, columnspan=2)

# Configuration Management
save_config_button = tk.Button(root, text="Save Config", command=save_config)
save_config_button.grid(row=3, column=0)

load_config_button = tk.Button(root, text="Load Config", command=load_config)
load_config_button.grid(row=3, column=1)

# Command Execution
tk.Label(root, text="Command:").grid(row=4, column=0)
command_entry = tk.Entry(root)
command_entry.grid(row=4, column=1)

args_entry = tk.Entry(root)
args_entry.grid(row=5, column=1)

def execute_command_from_gui():
    command = command_entry.get()
    args = args_entry.get().split()
    execute_command(command, args)

execute_button = tk.Button(root, text="Execute Command", command=execute_command_from_gui)
execute_button.grid(row=6, columnspan=2)

# CLI Command Entry
tk.Label(root, text="CLI Command:").grid(row=7, column=0)
cli_entry = tk.Entry(root)
cli_entry.grid(row=7, column=1)

cli_button = tk.Button(root, text="Execute CLI Command", command=execute_cli_command)
cli_button.grid(row=8, columnspan=2)

root.mainloop()

if __name__ == "__main__":
    main()
