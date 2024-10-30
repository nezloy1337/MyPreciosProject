FROM python:3.13
WORKDIR Pet
COPY . Pet
EXPOSE 8000
RUN pip install -r Pet/requirements.txt
CMD ["python", "manage.py", "runserver"]





