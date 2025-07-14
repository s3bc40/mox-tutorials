# conf.py - Minimal Sphinx configuration

project = 'Mox tutorials'
author = 's3bc40'
release = '0.1'

extensions = []
templates_path = ['_templates']
exclude_patterns = [
    '.venv',
    '.venv/**',
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '.git',
    '.git/**',
    '**/.pytest_cache',
    '**/__pycache__'
]

html_theme = "shibuya"
html_theme_options = {
    "accent_color": "orange",
}

master_doc = "docs/index"