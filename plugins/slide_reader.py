from pelican.readers import MarkdownReader
from pelican.utils import pelican_open
from pelican import readers, signals
from markdown import Markdown

class SlideReader(MarkdownReader):
    enabled = True

    file_extensions = ["slide"]

    def read(self, source_path):
        """Parse metadata of markdown files, do not modify content"""
        self._source_path = source_path

        with pelican_open(source_path) as text:
            md_extensions = {'markdown.extensions.meta': {},
                             'markdown.extensions.codehilite': {}}
            self._md = Markdown(extensions=md_extensions.keys(),
                          extension_configs=md_extensions)
            content = self._md.convert(text)
            content = ""
            is_metadata = True
            for line in text.split("\n"):
                if not is_metadata:
                    content += line + "\n"
                elif line == "":
                    is_metadata = False
        if hasattr(self._md, 'Meta'):
            metadata = self._parse_metadata(self._md.Meta)
        else:
            metadata = {}
        return content, metadata

def add_reader(readers):
    readers.reader_classes['slide'] = SlideReader

def register():
    signals.readers_init.connect(add_reader)
