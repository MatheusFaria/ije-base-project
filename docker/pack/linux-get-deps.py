readelf -d /usr/lib/x86_64-linux-gnu/libasound.so
readelf -d /game/build/game/game

Dynamic section at offset 0x2d78 contains 33 entries:
  Tag        Type                         Name/Value
 0x0000000000000001 (NEEDED)             Shared library: [libSDL2-2.0.so.0]
 0x0000000000000001 (NEEDED)             Shared library: [libSDL2_image-2.0.so.0]
 0x0000000000000001 (NEEDED)             Shared library: [libSDL2_ttf-2.0.so.0]
 0x0000000000000001 (NEEDED)             Shared library: [libSDL2_mixer-2.0.so.0]
 0x0000000000000001 (NEEDED)             Shared library: [libstdc++.so.6]
 0x0000000000000001 (NEEDED)             Shared library: [libm.so.6]
 0x0000000000000001 (NEEDED)             Shared library: [libgcc_s.so.1]
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
 0x000000000000000c (INIT)               0x1150
 0x000000000000000d (FINI)               0x21a4
 0x0000000000000019 (INIT_ARRAY)         0x202d58
 0x000000000000001b (INIT_ARRAYSZ)       16 (bytes)
 0x000000000000001a (FINI_ARRAY)         0x202d68
 0x000000000000001c (FINI_ARRAYSZ)       8 (bytes)
 0x000000006ffffef5 (GNU_HASH)           0x298
 0x0000000000000005 (STRTAB)             0x820
 0x0000000000000006 (SYMTAB)             0x2f8
 0x000000000000000a (STRSZ)              1053 (bytes)
 0x000000000000000b (SYMENT)             24 (bytes)
 0x0000000000000015 (DEBUG)              0x0
 0x0000000000000003 (PLTGOT)             0x203000
 0x0000000000000002 (PLTRELSZ)           816 (bytes)
 0x0000000000000014 (PLTREL)             RELA
 0x0000000000000017 (JMPREL)             0xe20
 0x0000000000000007 (RELA)               0xd00
 0x0000000000000008 (RELASZ)             288 (bytes)
 0x0000000000000009 (RELAENT)            24 (bytes)
 0x000000006ffffffb (FLAGS_1)            Flags: PIE
 0x000000006ffffffe (VERNEED)            0xcb0
 0x000000006fffffff (VERNEEDNUM)         2
 0x000000006ffffff0 (VERSYM)             0xc3e
 0x000000006ffffff9 (RELACOUNT)          4
 0x0000000000000000 (NULL)               0x0
