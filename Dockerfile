FROM python:3.11.3-slim
ARG INSTALL_LIBS=prod

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install ubuntu packages
RUN apt-get update && \
    apt-get install --no-install-recommends -y make gcc python-dev && \
    apt clean && \
    apt autoclean && \
    rm -rf /var/lib/apt/lists/*

# Copy files to new image
WORKDIR /opt/starwars_api
COPY . /opt/starwars_api

# Install library dependencies
RUN echo Building mode: install-$INSTALL_LIBS
RUN make install-$INSTALL_LIBS

# Clean unused files
RUN make clean

# Run flask in dev mode
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "-w", "4", "starwars_api.base:create_app()"]
