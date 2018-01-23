#!/usr/bin/env bash


apt-get install -y chromium-chromedriver
export PATH=$PATH:/usr/lib/chromium-browser/
pip install -U selenium
pip install pyvirtualdisplay
pip install -U pytest
cd Tests
python ./demo_test.py