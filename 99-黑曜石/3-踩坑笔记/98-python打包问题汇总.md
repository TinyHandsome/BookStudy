# Python 打包问题汇总

## Nuitka

- gcc 环境安装

  :bulb: 不过 nuitka 打包的时候，只要网没问题，会自动下载

  参考链接：https://www.cnblogs.com/larkwins/p/18182175

  [MinGW-w64](http://mingw-w64.org/)、[GCC](https://gcc.gnu.org/)安装：https://winlibs.com/

  下载后的文件：`winlibs-x86_64-posix-seh-gcc-14.2.0-llvm-19.1.7-mingw-w64ucrt-12.0.0-r3.7z`，解压后直接配置路径和 bin 路径即可。

- 命令样例：`nuitka --standalone --onefile --enable-plugin=tk-inter --output-dir=out --remove-output --show-progress --show-memory --plugin-enable=numpy --windows-icon-from-ico=./ikun.ico app.py`

  - `--standalone`：使得打包结果与本地的Python环境无关，即使得打包结果具备可移植性。
  - `--onefile`：使得打包结果为一个可执行文件，而不是一个文件夹。
  - `--lto`：用于启用链接时间优化。链接时间优化是一种编译器优化技术，它可以在编译和链接阶段对整个程序进行优化，而不仅仅是对单个源文件进行优化。通过启用lto，您可以让编译器在链接时对生成的目标代码进行更深入的优化，提高程序的性能和执行效率。
  - `--remove-output`：在打包结束后，清理打包过程中生成的临时文件。
  - `--enable-plugin=`：启用插件，等号后跟插件名。在要打包的Python代码使用了一些特殊的包时，需要启用插件，Nuitka才能够正确打包。如：如在代码中使用了PySide6，就需要加上`--enable-plugin=pyside6`。具体的插件列表可以使用`nuitka --plugin-list`来查看。
  - `--disable-console`：在运行打包后的程序时，不会弹出控制台，而是直接运行GUI程序。
  - `--include-package-data=`：包含给定软件包名称中的数据文件，等号后软件包名称。有的时候Nuitka并不能正确分析出一些Python软件包所需要使用的数据文件，在运行程序时提示FileNotFoundError等错误，此时就需要使用该选项。如：`--include-package-data=ultralytics`
  - `--include-data-files=`：按文件名包含数据文件，等号后的格式为<SRC=DEST>。SRC指的是文件夹的路径，DEST指的是文件夹相对于打包结果的路径，其中DEST只能使用相对路径。如：`--include-data-files=/Users/admin/Downloads/yolov5n.pt=./yolov5n.pt`
  - `--include-data-dir=`：包含文件夹中的数据文件，等号后的格式为<SRC=DEST>。使用方法与`--include-data-files=`相同。

