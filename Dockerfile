FROM continuumio/anaconda3

ENV TESSERACT_API_REPO https://github.com/ceia/chatbot-tesseract.git
ENV PORT 8080

ARG username=marcos.v.silva@live.com
ARG password=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
# 30 days of personal acess work

RUN apt update
RUN apt-get install tesseract-ocr -y
RUN apt-get install ffmpeg libsm6 libxext6  -y
# RUN mkdir Projects && cd Projects
# RUN git clone https://username:password@github.com/ceia/chatbot-tesseract.git