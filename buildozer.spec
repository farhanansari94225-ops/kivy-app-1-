name: Build APK
on: [push, workflow_dispatch]

jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      
      - name: Clear Buildozer Cache
        run: rm -rf ~/.buildozer
      
      - name: Build with Buildozer
        uses: digreatbrian/buildozer-action@v2
        with:
          python-version: '3.10'
          buildozer-cmd: buildozer android debug
      
      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: myapp-apk
          path: bin/*.apk
