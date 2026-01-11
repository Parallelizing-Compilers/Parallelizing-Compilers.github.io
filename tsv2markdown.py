import os
import sys

def tsv_to_markdown(tsv_file, markdown_file):
    """Convert TSV file to Markdown table format."""
    with open(tsv_file, 'r') as f:
        lines = f.readlines()
    
    if not lines:
        return
    
    # Parse TSV lines
    rows = []
    for line in lines:
        row = [cell.strip() for cell in line.strip().split('\t')]
        if not any(cell for cell in row):
            continue  # Skip empty rows
        rows.append(row)
        
    
    # Generate Markdown
    markdown_lines = []
    
    if rows:
        # Header row
        markdown_lines.append('| ' + ' | '.join(rows[0]) + ' |')
        
        # Separator row
        markdown_lines.append('|' + '|'.join([' --- ' for _ in rows[0]]) + '|')
        
        # Data rows
        for row in rows[1:]:
            markdown_lines.append('| ' + ' | '.join(row) + ' |')
    
    # Write to markdown file
    with open(markdown_file, 'w') as f:
        f.write('\n'.join(markdown_lines))
    
    print(f"Converted {tsv_file} to {markdown_file}")


if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Usage: python tsv2markdown.py <tsv_file>")
        sys.exit(1)
    
    tsv_file = sys.argv[1]
    markdown_file = os.path.splitext(tsv_file)[0] + '.md'
    tsv_to_markdown(tsv_file, markdown_file)
