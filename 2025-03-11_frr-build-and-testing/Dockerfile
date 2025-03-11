FROM ubuntu:24.04

# Install dependencies details available from frr documentation:
# https://docs.frrouting.org/projects/dev-guide/en/latest/building-frr-for-ubuntu2404.html

RUN apt-get update && apt-get install -y \
    git \
    bash \
    autoconf \
    automake \
    libtool \
    make \
    libjson-c-dev \
    python3-dev \
    libelf-dev \
    libreadline-dev \
    texinfo \
    pkg-config \
    libpam0g-dev \
    bison \
    flex \
    libc-ares-dev \
    python3-sphinx \
    install-info \
    build-essential \
    libsnmp-dev \
    perl \
    libcap-dev \
    libelf-dev \
    libunwind-dev \
    protobuf-c-compiler \
    libprotobuf-c-dev \
    libpcre2-dev \
    cmake \
    libgrpc++-dev \
    protobuf-compiler-grpc \
    libzmq5 \
    libzmq3-dev
WORKDIR /app

# Install libyang from source
RUN git clone https://github.com/CESNET/libyang.git
WORKDIR /app/libyang
RUN git checkout v2.1.128
RUN mkdir build
WORKDIR /app/libyang/build
RUN cmake --install-prefix /usr -D CMAKE_BUILD_TYPE:String="Release" ..
RUN make
RUN make install

WORKDIR /app

RUN git clone https://github.com/FRRouting/frr.git
WORKDIR /app/frr

RUN /app/frr/bootstrap.sh
RUN /app/frr/configure

RUN groupadd -r -g 92 frr
RUN groupadd -r -g 85 frrvty
RUN adduser --system --ingroup frr --home /var/run/frr/ --gecos "FRR suite" --shell /sbin/nologin frr
RUN usermod -a -G frrvty frr

CMD ["echo", "Welcome to the FRR in Ubuntu 24.04 Docker Image"]

