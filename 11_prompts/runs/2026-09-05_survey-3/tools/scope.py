"""Shared scope for survey-3 tools: the in-scope file list from `git ls-files`."""
import subprocess, re
EXCL = re.compile(r'^(\.github/|\.claude/|\.impeccable/|11_prompts/runs/|\.gitignore$|\.gitattributes$)|\.DS_Store$')
def files():
    out = subprocess.run(['git','ls-files'],capture_output=True,text=True,check=True).stdout.split('\n')
    return sorted(f for f in out if f and not EXCL.search(f))
def md_files(): return [f for f in files() if f.endswith('.md')]
def html_files(): return [f for f in files() if f.endswith('.html')]
FOLDER = lambda f: (f.split('/')[0][:2] if f[:2].isdigit() else 'ROOT')
