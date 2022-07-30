FROM fuzzers/atheris:1.0.3-python3.8
WORKDIR /
COPY . /
RUN pip install -r requirements-dev.txt
RUN chmod +rwx fuzz-parse.py