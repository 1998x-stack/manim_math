apt-get update -qq && apt-get install -y -qq libpango1.0-dev libcairo2-dev ffmpeg texlive texlive-latex-extra texlive-fonts-extra texlive-latex-recommended texlive-science fonts-noto-cjk 2>&1 | tail -5
pip install manim --break-system-packages 2>&1 | tail -5

# Install cairo and pkg-config (required for pycairo)
brew install cairo pkg-config

# Install FFmpeg (required for video rendering)
brew install ffmpeg

brew install pango scipy
brew install ninja

brew install --cask basictex

# Add to PATH
echo 'export PATH=/Library/TeX/texbin:$PATH' >> ~/.zshrc
source ~/.zshrc

# Install additional packages needed by Manim
sudo tlmgr update --self
sudo tlmgr install collection-fontsrecommended
sudo tlmgr install standalone preview doublestroke mnsymbol setspace rsfs relsize ragged2e fundus-calligra wasysym physics dvisvgm jknapltx wasy cm-super babel-english

# Verify
which latex

pip3 install manim --break-system-packages