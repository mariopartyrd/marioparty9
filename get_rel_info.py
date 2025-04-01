import os
import subprocess

def sha1_hash(file_path):
    """Calculate the SHA-1 hash of a file using sha1sum."""
    result = subprocess.run(['sha1sum', file_path], capture_output=True, text=True)
    return result.stdout.split()[0]

def generate_output(directory):
    """Generate the output for .rel files in the given directory."""
    output = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.rel'):
                rel_path = os.path.join(root, file)
                rel_name = os.path.splitext(file)[0]
                hash_value = sha1_hash(rel_path)

                # Build the paths
                rel_directory = os.path.basename(root)
                symbols_path = f"config/{rel_directory}/rels/{rel_name}/symbols.txt"
                splits_path = f"config/{rel_directory}/rels/{rel_name}/splits.txt"

                # Create the output dictionary
                output_dict = {
                    "object": rel_path,
                    "hash": hash_value,
                    "symbols": symbols_path,
                    "splits": splits_path,
                    "links": []
                }
                output.append(output_dict)

    return output

def main():
    directory = input("Enter the directory to parse for .rel files: ")
    output = generate_output(directory)
    for item in output:
        print("- object:", item["object"])
        print("  hash:", item["hash"])
        print("  symbols:", item["symbols"])
        print("  splits:", item["splits"])
        print("  links:", item["links"])
        print()

if __name__ == "__main__":
    main()
