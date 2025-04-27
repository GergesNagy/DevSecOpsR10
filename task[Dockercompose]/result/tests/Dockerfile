FROM node:18-slim

RUN apt-get update -qq && apt-get install -y \
    ca-certificates \
    bzip2 \
    curl \
    libfontconfig \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN yarn global add phantomjs-prebuilt

WORKDIR /app
COPY . .

CMD ["/bin/sh", "/app/tests.sh"]

