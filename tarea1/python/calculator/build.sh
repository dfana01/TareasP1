pip3 install -r requirements.txt
echo "#!/usr/bin/env python3" > calculator
cat main.py >> calculator
chmod +x calculator