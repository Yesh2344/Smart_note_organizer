import os
from datetime import datetime
from rich.console import Console
from rich.markdown import Markdown
import re

class SmartNoteOrganizer:
    def __init__(self):
        self.console = Console()
        self.notes_dir = "smart_notes"
        os.makedirs(self.notes_dir, exist_ok=True)

    def create_note(self, subject, content):
        # Clean filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{subject}_{timestamp}.md"
        filepath = os.path.join(self.notes_dir, filename)

        # Extract keywords
        keywords = self._extract_keywords(content)

        # Add metadata
        metadata = f"""---
subject: {subject}
date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
keywords: {', '.join(keywords)}
---

"""
        # Save note with metadata
        with open(filepath, "w") as f:
            f.write(metadata + content)

        self.console.print(f"[green]Note created: {filename}[/green]")
        self._preview_note(filepath)

    def _extract_keywords(self, content):
        # Simple keyword extraction (could be enhanced with NLP)
        words = re.findall(r'\b\w+\b', content.lower())
        # Remove common words
        common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to'}
        keywords = [word for word in words if word not in common_words and len(word) > 3]
        return list(set(keywords))[:5]  # Return top 5 unique keywords

    def _preview_note(self, filepath):
        with open(filepath, "r") as f:
            content = f.read()
        
        self.console.print("\n[yellow]Note Preview:[/yellow]")
        self.console.print(Markdown(content))

    def search_notes(self, keyword):
        found_notes = []
        for filename in os.listdir(self.notes_dir):
            if filename.endswith('.md'):
                filepath = os.path.join(self.notes_dir, filename)
                with open(filepath, 'r') as f:
                    content = f.read()
                    if keyword.lower() in content.lower():
                        found_notes.append(filename)

        if found_notes:
            self.console.print(f"\n[green]Found {len(found_notes)} notes containing '{keyword}':[/green]")
            for note in found_notes:
                self.console.print(f"📝 {note}")
        else:
            self.console.print(f"\n[red]No notes found containing '{keyword}'[/red]")

# Example usage
organizer = SmartNoteOrganizer()

# Create a sample note
sample_note = """# Introduction to Python

Python is a high-level programming language that emphasizes code readability.

## Key Features
- Easy to learn
- Large standard library
- Dynamic typing
- Object-oriented programming

Remember to practice coding regularly!
"""

organizer.create_note("Python_Basics", sample_note)

# Search for notes
organizer.search_notes("programming")