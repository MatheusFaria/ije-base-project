from debian:9

run apt-get update && \
    apt-get install -y \
        cmake g++ gcc build-essential nasm \
        g++-mingw-w64 mingw-w64-tools mingw-w64-x86-64-dev

run mkdir -p /game/build/libs /game/build/game /game/code /game/packs /game/libs /game/cmake
run apt-get install -y vim

add ./libs /game/libs
add ./cmake /game/cmake

env TOOLSET=x86_64-w64-mingw32 \
    PREFIX=/game/build/libs \
    BUILD_ARCH=x86_64-linux \
    CROSSPATH=$PREFIX/$TOOLSET
# env TOOLSET=i686-w64-mingw32 \
#     PREFIX=/game/build/libs \
#     BUILD_ARCH=i386-linux

# Windows SDL2 static lib build
run cd /game/libs/SDL2-2.0.8 && mkdir build-win64 && cd build-win64 && \
    export CC="$TOOLSET-gcc -static-libgcc" && \
    ../configure --target=$TOOLSET --host=$TOOLSET --build=$BUILD_ARCH --prefix=$PREFIX/$TOOLSET && \
    make && make install

run apt-get install -y tree

# Windows SDL2_image static lib build
run cd /game/libs/zlib-1.2.11 && \
    sed -i '/PREFIX =/c\PREFIX = ${TOOLSET}-' win32/Makefile.gcc && \
    export CROSSPATH=$PREFIX/$TOOLSET && \
    export prefix=$CROSSPATH/   && \
    export DESTDIR=$CROSSPATH/  && \
    export INCLUDE_PATH=include && \
    export LIBRARY_PATH=lib     && \
    export BINARY_PATH=bin      && \
    make install -f win32/Makefile.gcc

run tree $PREFIX/$TOOLSET

run cd /game/libs/libpng-1.6.34 && mkdir build-win64/ && cd build-win64/ && \
    export CROSSPATH=$PREFIX/$TOOLSET && \
    export CFLAGS="-I${CROSSPATH}/include" && \
    export CPPFLAGS="-I${CROSSPATH}/include" && \
    export LDFLAGS="-L${CROSSPATH}/lib"    && \
    ../configure --target=$TOOLSET --host=$TOOLSET --build=$BUILD_ARCH --prefix=$CROSSPATH && \
    make && make install

run tree $PREFIX/$TOOLSET

# run cd /game/libs/libjpeg-turbo-1.5.3 && mkdir build-win64/ && cd build-win64/ && \
#     export CROSSPATH=$PREFIX/$TOOLSET && \
#     export CFLAGS="-I${CROSSPATH}/include" && \
#     export LDFLAGS="-L${CROSSPATH}/lib"    && \
#     ../configure --target=$TOOLSET --host=$TOOLSET --build=$BUILD_ARCH --prefix=$CROSSPATH --without-simd --without-turbojpeg && \
#     make && make install

run cd /game/libs/libjpeg-turbo-1.5.3 && mkdir build-win64/ && cd build-win64/ && \
    export CROSSPATH=$PREFIX/$TOOLSET && \
    cmake -G"Unix Makefiles" -DCMAKE_SYSTEM_NAME=Windows -DCMAKE_SYSTEM_PROCESSOR=X86 \
          -DCMAKE_C_COMPILER=${TOOLSET}-gcc -DCMAKE_RC_COMPILER=${TOOLSET}-windres    \
          -DWITH_SIMD=FALSE -DCMAKE_INSTALL_PREFIX=${CROSSPATH} .. && \
    make && make install

run tree $PREFIX/$TOOLSET

run cd /game/libs/SDL2_image-2.0.3 && mkdir build-win64 && cd build-win64 && \
    export CROSSPATH=$PREFIX/$TOOLSET && \
    export PKG_CONFIG_PATH=${CROSSPATH}/lib/pkgconfig && \
    export PATH=${CROSSPATH}/bin:$PATH && \
    export CFLAGS="-I${CROSSPATH}/include" && \
    export LDFLAGS="-L${CROSSPATH}/lib" && \
    export LIBPNG="${CROSSPATH}/lib/libpng.a" && \
    export CC="$TOOLSET-gcc -static-libgcc" && \
    ../configure --target=$TOOLSET --host=$TOOLSET --build=$BUILD_ARCH --prefix=$CROSSPATH --disable-webp --disable-jpg --disable-jpg-shared && \
    make && make install


# Windows SDL2_ttf static lib build

run cd /game/libs/freetype-2.9 && mkdir build-win64 && cd build-win64 && \
    CROSSPATH=$PREFIX/$TOOLSET && PKG_CONFIG_PATH=${CROSSPATH}/lib/pkgconfig && \
    export PATH=${CROSSPATH}/bin:$PATH && \
    export CFLAGS="-I${CROSSPATH}/include" && \
    export LDFLAGS="-L${CROSSPATH}/lib" && \
    export LIBPNG="`libpng-config --libs`" && \
    export LIBPNG_CFLAGS="`libpng-config --cflags`" && \
    export LIBPNG_LDFLAGS="`libpng-config --ldflags`" && \
    ../configure --target=$TOOLSET --host=$TOOLSET --build=$BUILD_ARCH --prefix=$CROSSPATH && \
    make && make install

run cd /game/libs/SDL2_ttf-2.0.14 && mkdir build-win64 && cd build-win64 && \
    CROSSPATH=$PREFIX/$TOOLSET && PKG_CONFIG_PATH=${CROSSPATH}/lib/pkgconfig && \
    export PATH=${CROSSPATH}/bin:$PATH && \
    export CFLAGS="-I${CROSSPATH}/include/freetype2" && \
    export LDFLAGS="-L${CROSSPATH}/lib -lfreetype" && \
    export CC="$TOOLSET-gcc -static-libgcc" && \
    ../configure --target=$TOOLSET --host=$TOOLSET --build=$BUILD_ARCH \
                 --prefix=$CROSSPATH --with-freetype-prefix=$CROSSPATH  \
                 --with-freetype-exec-prefix=$CROSSPATH && \
    make && make install


# Windows SDL2_mixer static lib build

run cd /game/libs/libogg-1.3.3 && mkdir build-win64 && cd build-win64 && \
    export CROSSPATH=$PREFIX/$TOOLSET && \
    ../configure --target=$TOOLSET --host=$TOOLSET --build=$BUILD_ARCH \
                 --prefix=$CROSSPATH && \
    make && make install

run cd /game/libs/libvorbis-1.3.5 && mkdir build-win64 && cd build-win64 && \
    export CROSSPATH=$PREFIX/$TOOLSET && \
    export CFLAGS="-I${CROSSPATH}/include" && \
    export LDFLAGS="-L${CROSSPATH}/lib" && \
    export CC="$TOOLSET-gcc -static-libgcc" && \
    ../configure --target=$TOOLSET --host=$TOOLSET --build=$BUILD_ARCH \
                 --prefix=$CROSSPATH  && \
    make && make install

run cd /game/libs/SDL2_mixer-2.0.2 && mkdir build-win64 && cd build-win64 && \
    CROSSPATH=$PREFIX/$TOOLSET && \
    export PKG_CONFIG_PATH=${CROSSPATH}/lib/pkgconfig && \
    export PATH=${CROSSPATH}/bin:$PATH && \
    export CFLAGS="-I${CROSSPATH}/include" && \
    export LDFLAGS="-L${CROSSPATH}/lib" && \
    export CC="$TOOLSET-gcc -static-libgcc" && \
    ../configure --target=$TOOLSET --host=$TOOLSET --build=$BUILD_ARCH \
                 --prefix=$CROSSPATH --disable-music-mp3-smpeg && \
    make && make install

# Game specific build
add . /game/code/

run cd /game/build/game && \
       cmake -DCOMPILER_PREFIX=$TOOLSET \
             -DCMAKE_TOOLCHAIN_FILE=/game/cmake/mingw-toolchain.cmake \
             /game/code && \
       make

run apt-get install -y zip && zip -r /game/game.zip /game/build/game/game.exe /game/build/game/assets

cmd cp /game/game.zip /game/packs/ && sleep infinity
