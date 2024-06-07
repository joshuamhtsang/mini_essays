# Compiling Latex (pdflatex) in VS Code on Ubuntu

1. **Install Latex-Workshop Extension**:

   Inside VS Code, install the extension 'LaTeX-Workshop' by James Yu:
   [https://github.com/James-Yu/LaTeX-Workshop]
   
   (just search for it in VS Code Extensions Pane)

2. **Install TexLive for 'pdflatex'**:
   
   Install TexLive to get the 'pdflatex' tool:

   `$ sudo apt install texlive-latex-base`

   After this you should get the 'pdflatex' tool available
   in your terminal.  Check this tool is in the path:
   
   ```
   $ which pdflatex
   /usr/bin/pdflatex
   ```

3. **Set up 'latex-workshop' compile recipe**:
   
   `Ctrl + Shift + P` to open command palette.

   Search for 'User Settings' to get 'Preferences: User Settings (JSON)'.  
   This will open 'settings.json' for editing.
   Add the following JSON into 'settings.json':

   ```
   "latex-workshop.latex.recipes": [
        {
            "name": "Josh own build",
            "tools": [
                "pdflatex"
            ]
        },
   ]
   ```
   You can just begin typing 'latex-workshop.*' and let VS Code
   autocomplete autofill a JSON structure for you.

   Ensure the above simple 'pdflatex' build is the first item, so it's the first thing attempted when you build/compile.

4. To compile your *.tex document, just do a regular save:
   ```
   Ctrl + S
   ```
   or do the key-combination:
   ```
   Ctrl + Alt + B
   ```


