FROM python:3.11-slim-buster

ENV USER chall
ENV PORT 5000

RUN apt update -y && apt install -y build-essential curl python3-pip wget unzip

## chrome
RUN apt-get update \
    && apt-get install -y wget gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf libxss1 --no-install-recommends\
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

## chrome driver
RUN apt-get update -y && apt-get install -y libnss3
RUN wget https://storage.googleapis.com/chrome-for-testing-public/`curl -sS https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE`/linux64/chromedriver-linux64.zip && unzip chromedriver-linux64.zip && rm chromedriver-linux64.zip

# Add user
RUN adduser --disabled-password $USER

# Add files
COPY --chown=root:root app /app

WORKDIR /app
RUN chmod 705 run.sh
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

USER $USER
EXPOSE $PORT

ENTRYPOINT ["/bin/bash"]
CMD ["./run.sh"]
