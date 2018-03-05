FROM debian:9

RUN apt-get update && \
    apt-get install -y sudo cmake g++ build-essential \
                       libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev \
                       libsdl2-ttf-dev

# Replace 1000 with your user / group id
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

USER developer
ENV HOME /home/developer

run mkdir $HOME/game-build
workdir $HOME/game-build

CMD  cmake /game && sudo make install && /usr/games/game
