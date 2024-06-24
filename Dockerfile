FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt ${LAMBDA_TAST_ROOT}

RUN pip install pysqlite3-binary

RUN pip install -r requirements.txt --upgrade

EXPOSE 8000

ENV IS_USING_IMAGE_RUNTIME=True

COPY src/* ${LAMBDA_TAST_ROOT}
COPY data/chroma ${LAMBDA_TAST_ROOT}/data/chroma
