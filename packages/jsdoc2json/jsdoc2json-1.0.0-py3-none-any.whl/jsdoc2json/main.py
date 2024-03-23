import argparse
import json
import os
from colorama import init, Fore, Style
from .modules import lexical_parser, syntax_parser

def process_file(file_path, output_path, debug):
    try:
        # Open file in read mode
        with open(file_path, 'r', encoding='utf-8') as file:
            print(f"Processing file: {Fore.BLUE}{file_path}{Style.RESET_ALL}")

            # Check format (.gml)
            if not file_path.endswith('.gml'):
                print(f"File '{file_path}' is not a .gml file.")
                return

            # Read file
            content = file.read()
            
            # LEXICAL ANALYSIS
            lexical_parsing = lexical_parser.analysis(content)

            if lexical_parsing:
                print(f"\t{Fore.GREEN}Lexical analysis done successfully.{Style.RESET_ALL}")
            else:
                print(f"\t{Fore.YELLOW}No JSDoc found in the file.{Style.RESET_ALL}\n")
                return

            # SYNTAXIC ANALYSIS
            try:
                document_data = syntax_parser.analysis(lexical_parsing)
                print(f"\t{Fore.GREEN}Syntax analysis done successfully.{Style.RESET_ALL}")

                if debug:
                    print(repr(document_data))

                # Create output folder if it doesn't exist
                if not os.path.exists(output_path):
                    os.makedirs(output_path)

                # Write JSON
                with open(os.path.join(output_path, os.path.basename(file_path).replace(".gml", ".json")), "w", encoding='utf-8') as file:
                    json.dump(document_data.to_dict(), file, indent=4, ensure_ascii=False)

            except lexical_parser.WrongTokenError as e:
                print(f"\t{Fore.RED}{e}{Style.RESET_ALL}")

            print()

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error processing file '{file_path}': {e}")

def process_folder(folder_path, output_path, debug):
    try:
        # Recursively process all files in the folder
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                # Check format (.gml)
                if filename.endswith('.gml'):
                    process_file(file_path, output_path, debug)

    except FileNotFoundError:
        print(f"Folder '{folder_path}' not found.")
    except Exception as e:
        print(f"Error processing folder '{folder_path}': {e}")

def convert(file_or_folder_path, output_path, debug=False):
    if os.path.isfile(file_or_folder_path):
        print("\nFile conversion begins...\n")
        process_file(file_or_folder_path, output_path, debug)
    elif os.path.isdir(file_or_folder_path):
        print("\nFile conversion begins...\n")
        process_folder(file_or_folder_path, output_path, debug)
    else:
        print(f"File or folder '{file_or_folder_path}' not found.")

    print("End of conversion.\n")

def convert_command_line():
    # Argument parsing
    parser = argparse.ArgumentParser(description='JSdoc to JSON converter for GML files.')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-file', dest='file_path', help='Input file path')
    group.add_argument('-folder', dest='folder_path', help='Folder path containing input files')

    parser.add_argument('-output', dest='output_path', help='Output folder path containing JSON exports', required=True)
    parser.add_argument('-debug', dest='debug', action='store_true', help='Debug mode')

    args = parser.parse_args()

    if args.file_path:
        print("\nFile conversion begins...\n")
        process_file(args.file_path, args.output_path, args.debug)
    elif args.folder_path:
        print("\nFolder conversion begins...\n")
        process_folder(args.folder_path, args.output_path, args.debug)

    print("End of conversion.\n")

def main():
    convert_command_line()

if __name__ == "__main__":
    main()
