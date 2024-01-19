Steps for instalation:

install wsl on windows  (ubuntu in windows store)

run wsl on command prompt by typing wsl

run following commands:
curl https://ollama.ai/install.sh | sh
ollama pull llama2

go to directory and run (might have to install python and pip first):

python3 -m pip install -r requirements.txt

python3 llama_questions.py





To ask a question, type it on question.txt, you can change the file while running the program to ask different questions