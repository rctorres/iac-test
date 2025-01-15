FROM python:3.12-slim

#Installing SO related programs
RUN apt-get update && apt-get install -y \
    jq \
    && rm -rf /var/lib/apt/lists/*

#Setting EST time zone
RUN ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

ENV PYTHONUNBUFFERED=1
ENV APP_DIR=/work
ENV PYTHONPATH=$APP_DIR/api:$APP_DIR/common

WORKDIR $APP_DIR

#Setting a password (root) for the root user in case we needto use it with the image loaded.
RUN echo 'root:root' | chpasswd

COPY api/ api/
COPY common/ common/
copy VERSION .

#Setting up supervisor
RUN mv ./api/config/supervisor /etc/

#Installing pip requirements
RUN pip install --no-cache-dir -r ./api/config/requirements.pip
RUN rm -f ./api/config/requirements.pip

ENTRYPOINT supervisord -c /etc/supervisor/supervisord.conf
