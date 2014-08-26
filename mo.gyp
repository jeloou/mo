{
  "includes": [
     "common.gypi"
  ],
  "targets": [{
    "target_name": "mo",
    "type": "executable",
    "dependencies": [
      "deps/uv/uv.gyp:libuv"
    ],
    "sources": [
      "src/mo.c"
    ]
  }]
}